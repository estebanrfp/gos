[DISCORD]

[DEFINITION]
bot via discord.js
token (base64-like, not hex)
snowflake IDs = string

[SETUP]
1 create app → Bot → set username

2 intents (CRITICAL):
- Message Content (required → 4014 if missing)
- Server Members (recommended)
- Presence (optional)

3 token:
Bot → Reset Token → copy
WARNING:
- use Bot Token only
- NOT Public Key / App ID (hex → fails)

4 install:
scopes: bot, applications.commands
permissions:
- Send Messages (min)
- + View Channels, Read History, Embed, Files, Reactions (recommended)

5 IDs:
enable Developer Mode
→ copy Server ID, User ID

6 config:
config set channels.discord.token → token
config set channels.discord.enabled → true

[CONFIG]
channels.discord.token
channels.discord.guilds.{ID}:
- requireMention (default true)
channels.discord.textChunkLimit=2000

[DIAGNOSTIC]
- 4014 → Message Content Intent missing
- 401 → wrong token (check Bot Token)
- generic issues → check channels config
