[BACKUP]

[DEFINITION]
smart backup engine
auto full/incremental
use: backup create (no params)

[ENGINE]
- first/no prev → full (SQLite snapshot)
- changes → incremental (gzipped JSONL)
- no changes → skip
- after 7 incrementals → new full
- auto copy → Desktop/GenosOS-Backups (iCloud)

[ACTIONS]
create → auto decide type
list → all backups + size
verify → SHA-256 integrity
restore file={full}

[FLOW]
restore:
- ALWAYS create backup first
- restore full + replay incrementals

[WHEN]
- user request (backup/save)
- before delete agents
- before config changes
- before restore

[ROTATION]
- keep: 1 cycle (full + ≤7 incr)
- + previous full
- old → auto prune
