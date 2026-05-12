"""
Qwen3 Voice Server — TTS (voice cloning) + ASR (speech recognition).
Runs on port 8890. OpenAI-compatible endpoints.
TTS: Streams PCM chunks as generated. Pre-caches voice references.
ASR: OpenAI-compatible /v1/audio/transcriptions endpoint.
"""

import os, io, time, warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore")

from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
import uvicorn
import numpy as np

MODEL = None
ASR_MODEL = None
MODEL_PATH = os.environ.get("QWEN3_TTS_MODEL", os.path.expanduser("~/.genos/models/Qwen3-TTS-12Hz-0.6B-Base-8bit"))
ASR_MODEL_PATH = os.environ.get("QWEN3_ASR_MODEL", os.path.expanduser("~/.genos/models/Qwen3-ASR-0.6B-8bit"))
VOICES_DIR = os.environ.get("QWEN3_TTS_VOICES", "voices")

# Pre-cached voice data: { name: { wav_path, ref_text } }
VOICE_CACHE = {}

app = FastAPI(title="Qwen3-TTS Server")

@app.on_event("startup")
async def load():
    global MODEL, ASR_MODEL
    from mlx_audio.tts.utils import load_model
    print(f"[qwen3-tts] Loading TTS: {MODEL_PATH}")
    t0 = time.time()
    MODEL = load_model(MODEL_PATH)
    print(f"[qwen3-tts] TTS loaded in {time.time()-t0:.1f}s")

    # Load ASR model if available
    if os.path.isdir(ASR_MODEL_PATH):
        from mlx_audio.stt.utils import load_model as load_stt
        print(f"[qwen3-asr] Loading ASR: {ASR_MODEL_PATH}")
        t1 = time.time()
        ASR_MODEL = load_stt(ASR_MODEL_PATH)
        print(f"[qwen3-asr] ASR loaded in {time.time()-t1:.1f}s")
    else:
        print(f"[qwen3-asr] ASR model not found at {ASR_MODEL_PATH}, skipping")

    # Pre-cache all voice references
    if os.path.isdir(VOICES_DIR):
        for f in os.listdir(VOICES_DIR):
            if not f.endswith(".wav"):
                continue
            name = f.replace(".wav", "")
            wav_path = os.path.join(VOICES_DIR, f)
            txt_path = os.path.join(VOICES_DIR, f"{name}.txt")
            ref_text = "."
            if os.path.exists(txt_path):
                with open(txt_path, "r") as tf:
                    ref_text = tf.read().strip() or "."
            VOICE_CACHE[name] = {"wav_path": wav_path, "ref_text": ref_text}
            print(f"[qwen3-tts] cached voice: {name}")
    print(f"[qwen3-tts] {len(VOICE_CACHE)} voices cached")

@app.get("/v1/audio/voices")
async def list_voices():
    return {"voices": sorted(VOICE_CACHE.keys())}

@app.post("/v1/audio/speech")
async def speech(request: Request):
    """OpenAI-compatible TTS with real streaming voice cloning."""
    import mlx.core as mx

    body = await request.json()
    text = body.get("input", "")
    voice = body.get("voice", "reference")
    response_format = body.get("response_format", "wav")
    speed = body.get("speed", 1.0)

    if not text.strip():
        # Diagnostic: log what was actually received so we can trace empty-input bugs
        sample = repr(text[:200]) if text else "<empty>"
        print(f"[qwen3-tts] 400 rejected · voice={voice!r} len={len(text)} content={sample}")
        return JSONResponse({"error": "No input text"}, status_code=400)

    cached = VOICE_CACHE.get(voice)
    if not cached:
        print(f"[qwen3-tts] 404 voice not found · voice={voice!r} available={sorted(VOICE_CACHE.keys())}")
        return JSONResponse({"error": f"Voice '{voice}' not found"}, status_code=404)

    t0 = time.time()

    if response_format == "pcm":
        # Real streaming — yield PCM chunks as model generates them
        def pcm_stream():
            total_samples = 0
            try:
                results = MODEL.generate(
                    text=text, voice="af_heart",
                    ref_audio=cached["wav_path"], ref_text=cached["ref_text"],
                    speed=speed, stream=True, streaming_interval=0.20,
                    verbose=False
                )
                for result in results:
                    audio = result.audio if hasattr(result, 'audio') else result
                    if audio is None:
                        continue
                    if isinstance(audio, mx.array):
                        samples = np.array(audio.tolist(), dtype=np.float32).flatten()
                    else:
                        samples = np.array(audio, dtype=np.float32).flatten()
                    pcm16 = (np.clip(samples, -1, 1) * 32767).astype(np.int16)
                    total_samples += len(pcm16)
                    yield pcm16.tobytes()
            except Exception as e:
                print(f"[qwen3-tts] stream error: {e}")
            elapsed = time.time() - t0
            print(f"[qwen3-tts] '{voice}' {len(text)} chars → {total_samples} samples in {elapsed:.1f}s")

        return StreamingResponse(pcm_stream(), media_type="audio/pcm")
    else:
        # Non-streaming WAV
        from mlx_audio.tts.generate import generate_audio
        import shutil
        temp_dir = f"temp_{int(time.time() * 1000)}"
        try:
            generate_audio(
                model=MODEL, text=text,
                ref_audio=cached["wav_path"], ref_text=cached["ref_text"],
                speed=speed, output_path=temp_dir, verbose=False
            )
            output_file = os.path.join(temp_dir, "audio_000.wav")
            if not os.path.exists(output_file):
                return JSONResponse({"error": "Generation failed"}, status_code=500)
            with open(output_file, "rb") as f:
                audio_data = f.read()
            shutil.rmtree(temp_dir, ignore_errors=True)
            elapsed = time.time() - t0
            print(f"[qwen3-tts] '{voice}' {len(text)} chars → {len(audio_data)} bytes in {elapsed:.1f}s")
            return StreamingResponse(io.BytesIO(audio_data), media_type="audio/wav")
        except Exception as e:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
            return JSONResponse({"error": str(e)}, status_code=500)

@app.post("/v1/audio/transcriptions")
async def transcriptions(file: UploadFile = File(...), model: str = Form("qwen3-asr"), language: str = Form(None)):
    """OpenAI-compatible STT endpoint — Whisper drop-in replacement."""
    if not ASR_MODEL:
        return JSONResponse({"error": "ASR model not loaded"}, status_code=503)

    from mlx_audio.stt.generate import generate_transcription
    import tempfile, shutil

    t0 = time.time()
    # Save uploaded audio to temp file
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    try:
        content = await file.read()
        tmp.write(content)
        tmp.close()

        result = generate_transcription(model=ASR_MODEL, audio=tmp.name, verbose=False)
        elapsed = time.time() - t0

        # Extract text from result
        text = ""
        if isinstance(result, str):
            text = result
        elif isinstance(result, dict):
            text = result.get("text", "")
        elif hasattr(result, 'text'):
            text = result.text
        else:
            text = str(result)

        print(f"[qwen3-asr] {len(content)} bytes → '{text[:60]}...' in {elapsed:.1f}s")
        return {"text": text.strip()}
    except Exception as e:
        print(f"[qwen3-asr] error: {e}")
        return JSONResponse({"error": str(e)}, status_code=500)
    finally:
        os.unlink(tmp.name)

@app.get("/v1/models")
async def models():
    models_list = [{"id": "qwen3-tts", "object": "model", "owned_by": "qwen"}]
    if ASR_MODEL:
        models_list.append({"id": "qwen3-asr", "object": "model", "owned_by": "qwen"})
    return {"object": "list", "data": models_list}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8890)
