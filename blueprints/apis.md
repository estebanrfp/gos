[APIS]

[DEFINITION]
service credentials (non-AI)
stored: encrypted config (env.*) or process.env

[CONFIG]
- config set env.KEY → value (AES-GCM encrypted)
- via config tool or CONFIG_UPDATE
- available in agent context

[ENV]
- process.env vars
- set before start / .env

[EXAMPLES]
GOOGLE_SERVICE_ACCOUNT_JSON
TAVILY_API_KEY
STRIPE_API_KEY
HUBSPOT_API_KEY
HEYGEN_API_KEY

[RULES]
- NEVER store in code/git
- NEVER hardcode keys
- AI creds → providers config
- service keys → env.* or process.env
