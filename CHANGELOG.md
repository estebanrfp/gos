# Changelog

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
