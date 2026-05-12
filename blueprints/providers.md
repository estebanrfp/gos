[PROVIDERS]

[ARCHITECTURE]
local-first: Gemma 4 26B-A4B (default)
cloud: activated via ⌘L or `boost` tool
embeddings: 100% local (Qwen3-Embedding-8B, 4096d, in-process)

[LOCAL]
chat: Gemma 4 26B-A4B (Q4, port 8081)
stt: Whisper large-v3-turbo (port 8090) + Gemma 4 E4B fallback (port 8082)
embed: Qwen3-Embedding-8B (in-process, 0ms latency)
tts: Kokoro (24kHz, streaming)

[CLOUD_PROVIDERS]

anthropic:
- default: claude-sonnet-4-6
- boost: claude-opus-4-6
- auth: token (subscription) or api_key

openai:
- default: gpt-5.4
- boost: o3
- auth: api_key (sk-proj-...)

google:
- default: gemini-2.5-pro
- boost: gemini-3-pro-preview
- auth: api_key (AIza...)

[SMART_ROUTING]
boost tool auto-escalates:
- anthropic: sonnet → opus
- openai: gpt-5.4 → o3
- google: 2.5-pro → 3-pro

user picks provider, system picks model

[CONFIG]
credentials: providers.{name}.credentials[]
format: { id, type (token|api_key), value }
stored encrypted in genosconfig
manage via `swap_provider` tool or /providers command

[EMBED_CACHE]
hash-based (same input → same vector)
stored in embed_cache index
persists across sessions
local only (no cloud fallback)

[DIAGNOSTIC]
- 401 → invalid key/token
- 429 → rate limit
- no embeddings → check local model loaded
- wrong model → check active provider
- no streaming → check SSE connection
- local not ready → cloud fallback auto-activates
