[SIGNAL]

[DEFINITION]
signal-cli + phone number
modes:
- link (QR)
- register (SMS)
status: planned

[SETUP_LINK] (recommended)
1 install signal-cli
2 link:
signal-cli link -n "GenosOS" → scan QR
3 config:
config set channels.signal.account → +NUMBER
config set channels.signal.enabled → true

[SETUP_REGISTER]
1 register:
signal-cli -a +NUMBER register
(+captcha if needed)

2 verify:
signal-cli -a +NUMBER verify CODE

3 config (same as link)

[WARNINGS]
- use dedicated bot number
- personal number → ignores own messages
- register → de-auth main app

[DIAGNOSTIC]
- cli not found → check install/path
- daemon error → restart server
- auth fail → re-link account

[CONFIG]
channels.signal.account (E.164)
channels.signal.cliPath=signal-cli
channels.signal.textChunkLimit=4000
