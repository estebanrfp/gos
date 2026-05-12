[HEARTBEATS]

[DEFINITION]
periodic checks (auto)
use HEARTBEAT.md (short checklist)

[HEARTBEAT_vs_CRON]
heartbeat:
- batch checks
- conversational context
- flexible timing (~30min)
- fewer API calls

cron:
- exact timing
- isolated task
- one-shot / direct output

[CHECKS] (rotate 2–4x/day)
- email (urgent?)
- calendar (next 24–48h)
- mentions
- weather (if relevant)

[HISTORY]
check:
sessions_history(agent:main:heartbeat)

[REACH_OUT]
- urgent email
- event <2h
- interesting finding
- >8h silence

[STAY_QUIET]
- 23:00–08:00 (unless urgent)
- user busy
- no new info
- last check <30min

[PROACTIVE]
- review memory files
- check projects (git)
- update docs
- commit/push
- update MEMORY.md

[MEMORY_MAINT]
periodic:
- review memory/YYYY-MM-DD.md
- distill → MEMORY.md
- remove outdated
- daily = raw, MEMORY.md = curated
