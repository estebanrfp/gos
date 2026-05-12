[HUBSPOT]

[DEFINITION]
CRM via Private App
use web_fetch + Bearer pat-...
no OAuth

[SETUP]
1 create account
2 create Private App:
scopes:
- contacts read/write
- deals read/write
- companies read/write
- owners read

→ copy token (pat-...)

3 store key:
config set env.HUBSPOT_API_KEY → key

4 verify:
GET /crm/v3/objects/contacts?limit=1

[API]
base: https://api.hubapi.com

headers:
- Authorization: Bearer {key}
- Content-Type: application/json

[ENDPOINTS]
contacts: CRUD
contacts/search: filterGroups
deals: GET/POST
companies: GET/POST
associations:
PUT /crm/v4/objects/{from}/{id}/associations/{to}/{id}

[LIMIT]
100 req / 10s

[PATTERNS]
- inbound → search contact (phone/email)
- log → create note + associate
- deals → check stage / stale

[DIAGNOSTIC]
- 401 → invalid token (pat-)
- 403 → missing scopes
- 429 → rate limit
- not found → search email → phone
