[SERVER]

[ARCHITECTURE]
Bun standalone runtime (no browser needed)
HTTP + WebSocket on port 4400
static files: client/ (thin UI layer)
all intelligence server-side

[BOOT]
bun run server
→ http://localhost:4400
→ ws://localhost:4400/ws

flow:
1 HTTP/WS server starts
2 browser auth (WebAuthn/mnemonic)
3 SQLite init (per-account)
4 local models load (chat + embed + STT + whisper)
5 channels auto-boot (if enabled)
6 SIP register (if configured)

[WEBSOCKET]
persistent connection /ws
JSON request/response with IDs

request: { id, action, ...params }
response: { id, success, result }

~27 handlers:
tools, chat, streaming, memory, config,
agents, sessions, channels, voice, talk,
backup, skills, cron, templates, etc.

[HTTP]
/health → status check
/_media/{file} → TTS audio (audio/ogg)
/api/channels/* → channel REST API
/api/voice/* → voice call API

[TOOLS]
exec, read, write, ls, web_fetch
all via WS → sandbox validates → executes

[SANDBOX]
3-layer CBR model:
- exec: allowlist + metachar filter
- read/write: path validation + workspace confinement
- web_fetch: SSRF protection + internal IP block
- config: per-key read/write/auth policies

[DIAGNOSTIC]
- port in use → lsof -i :4400
- WS not connecting → check server running
- auth fail → WebAuthn/mnemonic
- tools timeout → default 30s (exec)
- local models slow → first request uses cloud fallback
