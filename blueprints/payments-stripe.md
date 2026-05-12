[STRIPE]

[DEFINITION]
payments via Stripe
use web_fetch + Bearer token
START in test mode

[SETUP]
1 create account
2 get API key:
- sk_test_ (test)
- sk_live_ (prod → later)

3 store key:
config set env.STRIPE_API_KEY → key

4 webhook:
URL → /hooks/stripe
events:
- payment_intent.succeeded
- checkout.session.completed
- charge.refunded
store signing secret (whsec_...)

5 verify:
GET /v1/balance

[API]
base: https://api.stripe.com/v1
auth: Bearer {key}

NOTE:
form-encoded bodies (NOT JSON)

[ENDPOINTS]
- payment_links
- prices
- checkout/sessions
- customers (+search)
- invoices (+items → finalize)
- refunds
- balance

[PATTERNS]
- payment link → pay → webhook → notify
- subscriptions → recurring charges
- invoice → items → finalize → send → webhook

[SECURITY]
NEVER store card data (PCI)
use Checkout / Payment Links only

[TEST]
cards:
- 4242... → success
- 4000...0002 → decline

[DIAGNOSTIC]
- 401 → invalid key
- webhook fail → check public URL + secret
- wrong amount → cents (5000 = €50)
- test vs live → isolated data
