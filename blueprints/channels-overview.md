[CHANNELS]
WhatsApp — Baileys (QR linking, multi-device)
Telegram — grammY (bot token, long polling)
Discord — discord.js (bot token + Message Content Intent)
Slack — @slack/bolt (Socket Mode, no webhooks)
iMessage — macOS native (Messages.app DB + osascript)
Voice — direct SIP trunk (Telnyx) + local Whisper + Gemma 4 + Kokoro. Use `voice` tool. For specialized voice → create dedicated agent.

[CONFIG]
stored encrypted in DB via `config` tool (dot-keys: channels.whatsapp, channels.telegram, etc.)

schema per channel:
- enabled: bool
- allowFrom: [phone/chatId]
- botToken: string (telegram)
- token: string (discord/slack)

[SETUP]

WhatsApp:
1. use `channel` tool → start whatsapp
2. QR appears in browser → scan with phone
3. auth persists in ~/.genos/{address}/channels/

Telegram:
1. t.me/BotFather → /newbot → copy token
2. config set channels.telegram.botToken → token
3. config set channels.telegram.enabled → true
4. use `channel` tool → start telegram

[TOOL]
use `channel` tool for all operations:
- status → all channel states
- start/stop → connect/disconnect
- config → view/update settings
- send → message to phone/chatId (default: owner)

[AUTO_BOOT]
channels with enabled: true start on server boot
WhatsApp auto-reconnects (3s delay)
Telegram restarts polling on disconnect

[DIAGNOSTIC]
1. channel status → check running state
2. not running → check config (enabled + credentials)
3. WhatsApp disconnected → stop + start → re-scan QR
4. Telegram error → verify botToken with BotFather
5. running but no response → check LLM provider config
