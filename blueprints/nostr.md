[NOSTR]

[DEFINITION]
keypair (nsec/npub)
DMs only (NIP-04 encrypted)
no groups, no media
status: planned

[SETUP]
1 generate keys:
nak key generate → save nsec

2 set key:
config set env.NOSTR_PRIVATE_KEY → nsec

3 config:
config set channels.nostr.relays → ["wss://relay.damus.io","wss://relay.primal.net"]
config set channels.nostr.enabled → true

[RELAYS]
default:
- wss://relay.damus.io
- wss://relay.primal.net

use 2–3 relays

[PROFILE]
fields:
- name
- about
- picture (https)
- nip05

event: NIP-01 kind:0

[KEYS]
pub: npub / hex
priv: nsec / hex

[LIMITS]
- DMs only
- no attachments

[DIAGNOSTIC]
- relay fail → check wss / change relay
- no send → relay write/rate limit

[CONFIG]
channels.nostr.privateKey
channels.nostr.relays
channels.nostr.profile.name
channels.nostr.profile.about
