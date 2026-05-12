# Changelog

## 0.1.1 — 2026-05-12

Fix release. The v0.1.0 bundle could not boot: the bundled server reads runtime assets (system prompts, blueprints, skills, voice clone seeds, templates) from sibling directories of `dist/` via `join(import.meta.dir, '..', X)`, and those directories were absent from the published repo. v0.1.1 ships them.

### Fixed

- Ship `prompts/`, `blueprints/`, `skills/`, `voices/`, `templates/` at the repo root so the bundle finds them at install time.
- Move `qwen3-server.py` and `qwen3-requirements.txt` into `dist/` (they're loaded via `__dirname` of the bundle, which is `dist/` at install time).
- Update `bun run build` to keep all runtime assets in sync automatically — single source of truth in the development repo, mirrored on every build.
- README: `pip install -r dist/qwen3-requirements.txt` (path corrected).

### No breaking changes

API surface, install flow, and architecture are unchanged from v0.1.0. v0.1.0 is retroactively unusable; anyone who downloaded it should re-clone or update to v0.1.1.

## 0.1.0 — 2026-05-12

First public release. **Superseded by 0.1.1 — do not use.**

### Highlights

- **Local-first runtime** — chat, vision, voice and embeddings run on-device. Cloud (Anthropic / OpenAI / Gemini) is opt-in via ⌘L.
- **Persistent semantic memory** — encrypted at rest (AES-256-GCM), knowledge graph with auto-linked edges, context injected per turn with zero prompt overhead.
- **Multi-channel agent** — WhatsApp, Telegram, Discord, Slack, iMessage, browser chat, all from one runtime with per-channel tool restrictions.
- **Real-time voice** — browser microphone (Talk Local) and direct SIP phone calls with per-agent voice cloning.
- **Multi-agent coordination** — A2A delegation, multi-participant rooms, autonomous echo conversations.
- **Capability-based sandbox** — declarative input validation per tool, workspace confinement, secret redaction.
- **Per-account isolation** — encrypted SQLite, mnemonic-derived keys, WebAuthn identity, per-account channels and workspaces.
- **Full-state backup engine** — immutable manifests, per-account iCloud sync, standard formats.
