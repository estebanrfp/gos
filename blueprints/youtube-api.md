[YOUTUBE]

[DEFINITION]
YouTube Data API v3 + Analytics
use web_fetch + OAuth Bearer

[SETUP]
1 enable APIs:
- YouTube Data API v3
- YouTube Analytics API

2 OAuth:
- grant youtube scope

3 store credentials:
config set (encrypted)

4 verify:
GET /channels?part=snippet,statistics&mine=true

[API]
data: https://www.googleapis.com/youtube/v3
analytics: https://youtubeanalytics.googleapis.com/v2

[ENDPOINTS]
channel:
GET /channels?part=snippet,statistics,contentDetails&mine=true

videos:
GET /search?forMine=true&type=video&order=date

upload:
POST /upload/.../videos (resumable, 2-step)

update:
PUT /videos

thumbnail:
POST /upload/.../thumbnails/set

playlists:
GET/POST /playlists
POST /playlistItems

comments:
GET /commentThreads
POST /comments

[ANALYTICS]
GET /reports
ids=channel==MINE
metrics: views,likes
dimensions: video

[QUOTA]
10k/day
read=1
write=50
upload=1600
search=100

[DIAGNOSTIC]
- 401 → token expired
- 403 → API disabled / quota / scope
- upload fail → file/format/url
- no analytics → delay 24–48h
