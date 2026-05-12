# Changelog

## 0.1.3 — 2026-05-12

README overhaul. Same bundle, better install experience.

- Apple Silicon-only warning surfaced upfront (was buried in Requirements)
- Disk space requirement (~35 GB) called out before the install starts
- Total setup time estimate (30 min - 2h, model download dominates)
- `python@3.11` added to the brew install line so users without Python don't stall at step 4
- `pip install` changed to `python3 -m pip install` for portability across system Python / venv setups
- New "Verify the install" section — `curl` health check on port 4400
- New "Troubleshooting" section covering the 7 most likely first-time errors (port in use, externally-managed Python, Intel Mac, HuggingFace stall, missing PATH entry, lost mnemonic)
- Mnemonic explained as BIP39 12/24 words, with the irreversibility warning made explicit

No code, bundle, or asset changes.

## 0.1.2 — 2026-05-12

First public release.

### Highlights

- **Local-first runtime** — chat, vision, voice and embeddings run on-device. Cloud (Anthropic / OpenAI / Gemini) is opt-in via ⌘L.
- **Persistent semantic memory** — encrypted at rest (AES-256-GCM), knowledge graph with auto-linked edges, context injected per turn with zero prompt overhead.
- **Multi-channel agent** — WhatsApp, Telegram, Discord, Slack, iMessage, browser chat, all from one runtime with per-channel tool restrictions.
- **Real-time voice** — browser microphone (Talk Local) and direct SIP phone calls with per-agent voice cloning.
- **Multi-agent coordination** — A2A delegation, multi-participant rooms, autonomous echo conversations.
- **Capability-based sandbox** — declarative input validation per tool, workspace confinement, secret redaction.
- **Per-account isolation** — encrypted SQLite, mnemonic-derived keys, WebAuthn identity, per-account channels and workspaces.
- **Full-state backup engine** — immutable manifests, per-account iCloud sync, standard formats.

### Bundle

- `dist/server.min.js` — single-file server bundle (~364 KB), Bun runtime, all dependencies marked external
- `dist/index.html` + chunks — code-split browser client (~180 KB total)
- `dist/qwen3-server.py` + `dist/qwen3-requirements.txt` — Python MLX server for Qwen3-TTS and Qwen3-ASR
- `prompts/`, `blueprints/`, `skills/`, `voices/`, `templates/` — runtime assets loaded by the bundle
