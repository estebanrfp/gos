[ADVANCED]

[DEFINITION]
server advanced features:
shell env, media, diagnostics

[SHELL]
- captures env ($PATH, locale, vars)
- exec matches user shell
- fix PATH issues → restart server

[MEDIA]
- files → content-hash names
- deduplication by default

[DIAGNOSTIC]
- check server logs

steps:
1 port busy → lsof :4400
2 exec path wrong → restart server
3 WS disconnected → check crash/logs
4 channel fail → channel status

[HEALTH]
GET /health → ok
WS ping → pong(ts)
