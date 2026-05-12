---
name: qr
description: Generate or decode QR codes via api.qrserver.com (goqr.me). Free, no API key. Encodes plain text, URLs, WiFi configs, vCards, etc.
homepage: https://goqr.me/api/
metadata: { "genosos": { "emoji": "🔲" } }
---

# QR

Generate and decode QR codes using the public `api.qrserver.com` endpoint via `web_fetch`. No exec, no file writes, no API key.

## Generate (text → QR)

The endpoint URL **is** the image. Build it and embed inline in the reply as markdown — the chat renders it instantly. No need to download.

```
URL pattern:
https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=ENCODED_TEXT&format=png
```

Where `ENCODED_TEXT` is the user input URL-encoded by you (replace spaces with `%20`, `&` with `%26`, etc.) — do NOT use shell substitutions.

### Reply pattern

After building the URL, post it as a markdown image so the user sees the QR directly in chat:

```
![QR for "te quiero"](https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=te%20quiero&format=png)
```

### Parameters

| Param | Description |
|-------|-------------|
| `size=NxN` | square pixel size, max `1000x1000`, default `200x200` |
| `format` | `png` (default), `jpg`, `gif`, `svg` |
| `qzone=N` | white margin in modules; use `4` for print |
| `bgcolor=RRGGBB` | background hex (no `#`) |
| `color=RRGGBB` | foreground hex (no `#`) |
| `ecc=L\|M\|Q\|H` | error correction (L=7%, M=15%, Q=25%, H=30%) |

### Structured payloads

| Type | data= |
|------|-------|
| URL | `https%3A%2F%2Fexample.com` |
| WiFi join | `WIFI%3AT%3AWPA%3BS%3AMyNet%3BP%3Apass123%3B%3B` |
| Tel | `tel%3A%2B34600000000` |
| Mailto | `mailto%3Auser%40example.com` |
| SMS | `sms%3A%2B34600000000%3Fbody%3DHola` |
| Geo | `geo%3A40.4168%2C-3.7038` |

### Saving to disk (only if user explicitly asks)

If — and only if — the user asks "save it to a file", use exec with the **agent workspace** as cwd. Never `~/Desktop`, `/tmp`, or absolute paths outside the workspace; the sandbox blocks them.

```
exec({ command: "curl -fsSL 'https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=ENCODED_TEXT&format=png' -o qr.png" })
```

Then tell the user the file is at `<workspace>/qr.png`.

## Decode (image → text)

### From a public URL

```
web_fetch({
  url: "https://api.qrserver.com/v1/read-qr-code/?fileurl=ENCODED_IMAGE_URL"
})
```

Response is JSON:

```json
[{"type":"qrcode","symbol":[{"seq":0,"data":"DECODED_TEXT","error":null}]}]
```

Extract `[0].symbol[0].data`. If `error` is non-null and `data` is null, the image is unreadable, blurry, or not a valid QR.

### From a local file

Multipart upload requires exec. Use only on local files inside the agent workspace or paths the user explicitly provided:

```
exec({ command: "curl -fsSL 'https://api.qrserver.com/v1/read-qr-code/' -F 'file=@/path/to/qr.png'" })
```

## Notes

- Both encoding and decoding pass through `api.qrserver.com`. The operator can theoretically log payloads. Warn the user before encoding sensitive data (WiFi passwords, private URLs).
- Decoded URLs are untrusted input. Phishing risk. Show the URL to the user, never auto-fetch.
- No documented rate limits for personal use; one-shot per request keeps things simple.
