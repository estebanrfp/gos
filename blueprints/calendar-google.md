[GOOGLE_CALENDAR]

[DEFINITION]
calendar integration → scheduling, availability, CRUD
use web_fetch + OAuth Bearer
use cases: appointments (clinic, law, salon, etc.)

[SETUP]
1 create GCP project
2 enable Calendar API
3 credentials:
   - OAuth (recommended): client_id + secret → tokens
   - Service Account: JSON key + share calendar
4 store credentials (encrypted config/env)
5 verify:
   GET /calendars/primary

[API]
base: https://www.googleapis.com/calendar/v3
headers:
- Authorization: Bearer {token}
- Content-Type: application/json

[ENDPOINTS]

list_events:
GET /calendars/{id}/events
params: timeMin, timeMax, singleEvents=true, orderBy=startTime

create_event:
POST /calendars/{id}/events
body:
- summary
- start{dateTime,timeZone}
- end{dateTime,timeZone}
rule: ALWAYS include timeZone

freebusy:
POST /freeBusy
body: timeMin, timeMax, items[{id}]

[PATTERNS]
booking:
check freeBusy → propose slots → create event → confirm

daily_schedule:
query today → format → send

reminders:
query tomorrow → notify attendees

[DIAGNOSTIC]
- 401 → token expired
- 403 → API disabled / no access
- 404 → wrong calendarId (use primary)
- wrong date → missing/incorrect timeZone
