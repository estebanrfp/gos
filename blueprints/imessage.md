[IMESSAGE]

[DEFINITION]
macOS only
read Messages.app DB + send via osascript
no external CLI

[REQUIREMENTS]
- macOS + Messages logged in
- Full Disk Access (Bun/Terminal)
- Automation permission (Messages.app)

[SETUP]
1 grant Full Disk Access:
→ ~/.bun/bin/bun

2 enable:
config set channels.imessage.enabled → true

3 optional:
config set channels.imessage.allowFrom → [ids]

[FLOW]
- poll chat.db (~5s)
- read via sqlite3
- send via osascript

[CONFIG]
channels.imessage.enabled
channels.imessage.allowFrom

[DIAGNOSTIC]
- permission denied → Full Disk Access (CRITICAL)
- no messages → check Messages.app active/login
- send fail → grant Automation permission
