---
name: openclaw-shield-upx
description: "Security monitoring for OpenClaw agents — check Shield health, review events, inspect vault. Use when: user asks about security status, Shield health, event logs, or redaction vault. NOT for: general OS hardening, firewall config, or network security."
homepage: https://www.upx.com/en/lp/openclaw-shield-upx
source: https://www.npmjs.com/package/@upx-us/shield
metadata: {"openclaw": {"requires": {"config": ["plugins.entries.shield"]}, "homepage": "https://clawhub.ai/brunopradof/openclaw-shield-upx", "emoji": "🛡️"}}
---

# OpenClaw Shield

Security monitoring for OpenClaw agents by [UPX](https://www.upx.com). Shield runs as a plugin inside the OpenClaw gateway, capturing agent activity and sending redacted telemetry to the UPX detection platform.

## Getting started

Shield requires the `@upx-us/shield` plugin and an active subscription.

- **Plugin**: [@upx-us/shield](https://www.npmjs.com/package/@upx-us/shield)
- **Subscribe / Free 30-day trial**: [upx.com/en/lp/openclaw-shield-upx](https://www.upx.com/en/lp/openclaw-shield-upx)
- **Dashboard**: [uss.upx.com](https://uss.upx.com)

## Commands

| Command | What it does |
|---|---|
| `openclaw shield status` | Plugin health, connection state, event counts, last sync |
| `openclaw shield flush` | Force an immediate sync to the platform |
| `openclaw shield logs` | Recent events from the local buffer (last 24h) |
| `openclaw shield logs --last 20` | Show last N events |
| `openclaw shield logs --type TOOL_CALL --since 1h` | Filter by event type or time window |
| `openclaw shield logs --format json` | JSON output |
| `openclaw shield vault show` | Agent and workspace inventory, redaction summary (hashed IDs) |
| `openclaw shield cases` | List open security cases |
| `openclaw shield cases show <ID>` | Full case detail with events, rule, playbook |
| `openclaw shield cases resolve <ID>` | Resolve a case (--resolution, --root-cause, --comment) |
| `openclaw shield monitor` | Case notification cron — status, --on, --off, --interval |

## When to use this skill

- "Is Shield running?" → `openclaw shield status`
- "What did Shield capture recently?" → `openclaw shield logs`
- "How many agents are on this machine?" → `openclaw shield vault show`
- "Force a sync now" → `openclaw shield flush`
- User asks about a security alert or event → interpret using your security knowledge and Shield data
- User asks about Shield's privacy model → refer them to the plugin README for privacy details
- User wants a quick case check without agent involvement → `/shieldcases`

## Status interpretation

After running `openclaw shield status`, check:

- **Connected** → healthy, nothing to do
- **Disconnected** → gateway may need a restart
- **High failure count** → platform connectivity issue, usually self-recovers; try `openclaw shield flush`
- **Rising quarantine** → possible version mismatch, suggest checking for plugin updates

## RPCs

Cases are created automatically when detection rules fire. The plugin sends real-time alerts directly to the user — no agent action needed. Use `shield.cases_list` only when the user asks about open cases.

**Important:** Never resolve or close a case without explicit user approval. Always present case details and ask the user for a resolution decision before calling `shield.case_resolve`.

| RPC | Params | Purpose |
|---|---|---|
| `shield.status` | — | Health, counters, case monitor state |
| `shield.flush` | — | Trigger immediate poll cycle |
| `shield.events_recent` | `limit`, `type`, `sinceMs` | Query local event buffer |
| `shield.events_summary` | `sinceMs` | Event counts by category |
| `shield.subscription_status` | — | Subscription tier, expiry, features |
| `shield.cases_list` | `status`, `limit`, `since` | List open cases + pending notifications |
| `shield.case_detail` | `id` | Full case with events, rule, playbook |
| `shield.case_resolve` | `id`, `resolution`, `root_cause`, `comment` | Close a case |
| `shield.cases_ack` | `ids` | Mark cases as notified |

**Resolve values:** `true_positive`, `false_positive`, `benign`, `duplicate`
**Root cause values:** `user_initiated`, `misconfiguration`, `expected_behavior`, `actual_threat`, `testing`, `unknown`

## Presenting data

RPC responses include a `display` field with pre-formatted text. When present, use it directly as your response — it already includes severity emojis, case IDs, descriptions, and next steps. Only format manually if `display` is absent.

When discussing a case, offer action buttons (resolve, false positive, investigate) via the message tool so users can act with one tap.

## Notes

- Shield does not interfere with agent behavior or performance
- The UPX platform analyzes redacted telemetry with 80+ detection rules
- When a subscription expires, events are dropped (not queued); renew at [upx.com/en/lp/openclaw-shield-upx](https://www.upx.com/en/lp/openclaw-shield-upx)
