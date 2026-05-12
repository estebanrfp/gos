[HEYGEN]

[DEFINITION]
AI avatar video generation
script + voice → video
use web_fetch + x-api-key

[SETUP]
1 create account
2 get API key
3 store key:
config set env.HEYGEN_API_KEY → key
4 verify:
GET /v2/avatars

[API]
base: https://api.heygen.com
headers:
- x-api-key
- Content-Type: application/json

[ENDPOINTS]
avatars:
GET /v2/avatars

voices:
GET /v2/voices

create_video:
POST /v2/video/generate

status:
GET /v1/video_status.get?video_id={id}

asset:
POST /v1/asset (multipart)

[FLOW]
script → TTS → create video
→ poll status → get URL
→ (optional) upload/share

[CREDITS]
~1/min standard
~6/min avatar IV
video URL expires (7d)

[DIAGNOSTIC]
- 401 → invalid key
- failed → check error (credits/audio)
- low quality → resolution/plan (720p free)
