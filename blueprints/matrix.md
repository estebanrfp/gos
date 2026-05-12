[MATRIX]

[DEFINITION]
homeserver + accessToken
use full IDs (@user:server)
E2EE optional (required for encrypted rooms/Beeper)
status: planned

[SETUP]
1 get token:
POST /_matrix/client/v3/login
→ copy access_token

2 config:
config set channels.matrix.homeserver → URL
config set channels.matrix.accessToken → token
config set channels.matrix.enabled → true

3 E2EE (if needed):
verify device (Element)

[CONFIG]
channels.matrix.homeserver
channels.matrix.accessToken
channels.matrix.encryption=false
channels.matrix.textChunkLimit

[BEHAVIOR]
- responds to @mentions (default)

[DIAGNOSTIC]
- auth fail → check token
- no response → check room perms / mention
- encrypted fail → enable + verify E2EE
