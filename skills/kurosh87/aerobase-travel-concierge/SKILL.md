---
name: aerobase-travel-concierge
description: Complete AI travel concierge - flights, hotels, lounges, awards, activities, deals, and wallet. Powered by Aerobase.
metadata: {"openclaw": {"emoji": "🤖", "primaryEnv": "AEROBASE_API_KEY", "user-invocable": true, "homepage": "https://aerobase.app"}}
---

# Aerobase Travel Concierge ⭐ ALL-IN-ONE

Your personal AI travel agent that never sleeps. **This is the complete package** — all Aerobase skills in one installation.

## Why This Skill?

**Everything you need for travel:**
- ✈️ Flights with jetlag scoring
- 🏆 Awards across 24+ programs  
- 🏧 Lounges with recovery scores
- 🏨 Hotels with day-use
- 🎫 Tours & activities
- 💰 Flight deals
- 💳 Points & wallet
- 😴 **Jetlag recovery plans** (PREMIUM)

**One install = full capabilities**

## What You Get

### Core Features
- Flight search with 0-100 jetlag scoring
- Award search across 24 airline programs
- Airport lounge discovery with recovery scores
- Hotel search with day-use options
- Viator tours and activities
- Flight deals via Kiwi
- Credit card and transfer strategy
- Gmail loyalty balance scanning

### PREMIUM: Recovery Plans
Personalized jetlag recovery plans included:
- Pre-trip preparation schedule
- In-flight strategies  
- Day-by-day recovery timeline
- Light exposure timing
- Sleep and diet adjustments

## Example Conversations

```
User: "Find business class awards from SFO to NRT next week"
→ Searches 24 programs
→ Shows miles cost + availability
→ Scores each for jetlag

User: "Create a recovery plan for my Paris trip"
→ Generates day-by-day schedule
→ Optimizes for your chronotype
→ Includes flight strategies

User: "What's my total points balance?"
→ Scans Gmail for loyalty emails
→ Aggregates all programs
→ Shows total value
```

## API Documentation

Full API docs: https://aerobase.app/developers

OpenAPI spec: https://aerobase.app/api/v1/openapi

## API Endpoints Included

### Flights
- `POST /api/v1/flights/score` — Jetlag scoring (0-100)
- `POST /api/v1/flights/search` — Search with scoring
- `POST /api/v1/flights/compare` — Compare options

### Awards
- `POST /api/v1/awards/search` — 24+ programs
- `GET /api/transfer-bonuses` — Current bonuses

### Lounges
- `GET /api/v1/lounges` — Recovery-scored lounges

### Hotels
- `GET /api/v1/hotels` — Day-use, jetlag-friendly

### Activities
- `GET /api/v1/tours` — Viator integration

### Deals
- `GET /api/v1/deals` — Price alerts

### Wallet
- `GET /api/v1/credit-cards` — Transfer partners
- Gmail loyalty scanning

### Recovery (PREMIUM)
- `POST /api/v1/recovery/plan` — Full recovery plan

## Subscription

**This skill includes PREMIUM features:**
- Unlimited API requests
- Personalized recovery plans
- All skills in one package

Get started: https://aerobase.app/concierge/pricing

## Free vs Premium

| Feature | Free | Premium |
|---------|------|---------|
| API requests/day | 5 | Unlimited |
| Jetlag scoring | Limited | Unlimited |
| Recovery plans | ❌ | ✅ |
| Price alerts | Basic | Advanced |
| Gmail scanning | ❌ | ✅ |

## Get Started

1. Get API key: https://aerobase.app/connect
2. Install skill: `clawhub install aerobase-travel-concierge`
3. Set key: `export AEROBASE_API_KEY="your_key"`

**Or get the full AI agent:** https://aerobase.app/concierge/pricing
