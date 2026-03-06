---
name: aerobase-flight-deals
description: Find cheap flights, monitor prices, and alert on price drops
metadata: {"openclaw": {"emoji": "💰", "primaryEnv": "AEROBASE_API_KEY", "user-invocable": true, "homepage": "https://aerobase.app"}}
---

# Flight Deals

Find cheap flights and monitor prices.

## API Endpoints

**GET /api/v1/deals**
Search flight deals.

Query params:
- `origin` — departure airport
- `destination` — destination airport
- `max_price` — max price in USD
- `min_score` — minimum jetlag score
- `date_from` / `date_to` — travel dates
- `cabin` — economy, business, first
- `sort` — value_score, price, jetlag_score

Returns deals with:
- Route and dates
- Price
- Jetlag score
- Booking link

## Features

- Price drop alerts
- Jetlag scoring on deals
- Sort by value (price + jetlag combined)

## Rate Limits

- **Free tier**: 5 API requests per day
- **Premium tier**: Unlimited requests

## Configuration

```bash
export AEROBASE_API_KEY="your_api_key_here"
```

Get your API key at: https://aerobase.app/connect
