[SLACK]

[DEFINITION]
Socket Mode (no webhooks)
requires:
- appToken (xapp-...)
- botToken (xoxb-...)

[SETUP]
1 create app (workspace)

2 enable Socket Mode:
→ create appToken (scope: connections:write)

3 bot scopes:
- chat:write
- channels:read/history
- groups:history
- im/mpim:history
- users:read
- app_mentions:read
- reactions:read/write
- pins:read/write
- emoji:read
- commands
- files:read/write

4 events:
- app_mention
- message.channels/groups/im/mpim
- reaction_added/removed

5 App Home:
enable Messages Tab

6 install:
→ get botToken (xoxb-...)

7 config:
config set channels.slack.appToken → xapp-...
config set channels.slack.botToken → xoxb-...
config set channels.slack.enabled → true

[CONFIG]
channels.slack.mode=socket
channels.slack.botToken
channels.slack.appToken
channels.slack.textChunkLimit=4000

[BEHAVIOR]
- responds to @mentions (default)

[DIAGNOSTIC]
- missing tokens → need xapp + xoxb
- no connection → enable Socket Mode
- auth fail → regenerate tokens
- no channel replies → requires mention
- DMs ignored → enable App Home Messages
