# GenosOS (GOS) — Agent Operating System

A standalone, local-first runtime for autonomous AI agents. Memory, multi-channel messaging, real-time voice, phone calls, and on-device language models — all running on your machine, with cloud as the exception, not the default.

---

[![License-SourceCode-Proprietary](https://img.shields.io/badge/Source%20Code-Proprietary-blue.svg?style=for-the-badge)](https://github.com/estebanrfp/gos/blob/main/LICENSE)
[![Production Build](https://img.shields.io/badge/Production%20Build-Free%20for%20personal%20%26%20commercial%20use-brightgreen.svg?style=for-the-badge)](https://github.com/estebanrfp/gos/blob/main/LICENSE)

![Project Status](https://img.shields.io/badge/status-beta-orange)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Apple%20Silicon-lightgrey)
![Runtime](https://img.shields.io/badge/runtime-Bun-black)

## Table of Contents

- [What is GenosOS](#what-is-genosos)
- [Highlights](#highlights)
- [Requirements](#requirements)
- [Installation](#installation)
- [First Run](#first-run)
- [Architecture Overview](#architecture-overview)
- [License](#license)
- [Author](#author)

## What is GenosOS

GenosOS is a server runtime that gives an LLM-driven agent the operating-system layer it needs to actually live in your workflow:

- **Persistent semantic memory** — every conversation contributes to a knowledge graph; relevant context is injected automatically on each turn, with zero prompt overhead for memory mechanics.
- **Multi-channel presence** — the same agent handles WhatsApp, Telegram, Discord, Slack, iMessage and browser chat, with channel-aware tool restrictions.
- **Real-time voice** — browser microphone and direct SIP phone calls, fully local pipeline (Qwen3-ASR + Qwen 3.6 35B-A3B + Qwen3-TTS), ~1-1.5s round-trip on cached turns.
- **Multi-agent coordination** — agent-to-agent delegation, multi-participant rooms with autonomous echo conversations, isolated per-agent memory and workspace.
- **Capability-based runtime sandbox** — every tool call validated against declarative policies; workspace confinement, allowlisted shell commands, secret redaction.
- **Local-first by design** — 5 local models cover chat, vision, voice and embeddings (~37 GB RAM). Cloud (Anthropic/OpenAI/Gemini) is opt-in via ⌘L.

## Highlights

- **Encrypted memory at rest** — AES-256-GCM derived from your own mnemonic, keys never leave the machine.
- **Per-account isolation** — each Ethereum address is an independent account with its own encrypted database, workspace, and channel sessions.
- **WebAuthn + mnemonic identity** — no passwords, no shared secrets, no cloud auth.
- **Direct SIP trunk** for phone calls — no Twilio, no Cloudflare tunnel, no vendor lock-in.
- **Zero frameworks** on the client — vanilla JS + DOM API + CSS. No build step required to develop the UI.
- **Full-state backup engine** — immutable manifests, per-account iCloud sync, standard tar.gz + SQLite (no proprietary formats).

## Requirements

- **Hardware**: Apple Silicon Mac (M1/M2/M3/M4), 64 GB RAM recommended for the full local stack
- **OS**: macOS 14+
- **Runtime**: [Bun](https://bun.sh) `>=1.2.0`
- **Python**: 3.11+ (for the Qwen3 MLX server — TTS + ASR)
- **System packages** via Homebrew:
  - `llama.cpp` — chat + embedding models
  - `ffmpeg` — audio conversion
  - `cliclick` — Computer Use tool (optional)

## Installation

```sh
# 1. Clone
git clone https://github.com/estebanrfp/gos.git
cd gos

# 2. Install system dependencies
brew install bun llama.cpp ffmpeg cliclick

# 3. Install JavaScript runtime dependencies
bun install

# 4. Install Python dependencies for the MLX TTS/ASR server
pip install -r dist/qwen3-requirements.txt

# 5. Start GenosOS
bun start
```

## First Run

On first boot, the setup wizard will:

1. Open `http://localhost:4400` in your browser
2. Prompt for a mnemonic passphrase (used to derive your encryption key — it never leaves your machine)
3. Detect missing GGUF models and auto-download them from HuggingFace (~33 GB total)
4. Start `llama-server` for chat and embeddings, and launch the Python MLX server for voice
5. Land you in your first agent's chat session

After first run, every subsequent boot is fast — models load once, channels reconnect automatically.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│  Channels: WhatsApp · Telegram · Discord · Slack · iMessage │
│  Voice: Browser mic (Talk Local) · SIP phone calls          │
│  UI: Browser chat at http://localhost:4400                  │
└─────────────────────────────┬───────────────────────────────┘
                              │
                  ┌───────────▼───────────┐
                  │   GenosOS Server      │  Bun, single process,
                  │   :4400 (WS + HTTP)   │  encrypted SQLite store
                  └───────────┬───────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
  ┌─────▼─────┐         ┌─────▼─────┐         ┌─────▼─────┐
  │ llama-    │         │ qwen3-    │         │ node-     │
  │ server    │         │ server.py │         │ llama-cpp │
  │ :8081     │         │ :8890     │         │ (embed)   │
  │           │         │           │         │ in-proc   │
  │ Qwen 3.6  │         │ Qwen3-TTS │         │ Qwen3-Emb │
  │ 35B-A3B   │         │ Qwen3-ASR │         │           │
  └───────────┘         └───────────┘         └───────────┘
```

All intelligence, all encryption, all routing — runs locally. Cloud APIs (Anthropic, OpenAI, Gemini) are available as an opt-in boost (⌘L) but are not required for any feature.

## License

The minified production build in `dist/` is **free for personal and commercial use** — integrate, distribute, resell. The source code is **proprietary**; reverse-engineering, decompilation, or modification of the bundle is not permitted.

See [LICENSE](./LICENSE) for the full terms.

## Author

Esteban Fuster Pozzi (@estebanrfp) — Full Stack JavaScript Developer
