# Claude Code — Useful Notes

## Context Window per Terminal Session
Each terminal running Claude Code gets its own independent 200k token context window. They do not share a pool.

| Terminal | Context Window |
|----------|---------------|
| Terminal 1 | 0 – 200k tokens |
| Terminal 2 | 0 – 200k tokens |
| Terminal 3 | 0 – 200k tokens |

So if you open 3 terminals, you effectively have 3 × 200k = 600k tokens available across sessions.

## Checking Context Usage with `/context`
Run `/context` inside Claude Code to see how your 200k token budget is being used in the current session.

Example output:
```
Context Usage
⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛀ ⛀ ⛀   Sonnet 4.6
⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   claude-sonnet-4-6
⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   17.3k/200k tokens (9%)

                        Estimated usage by category
⛁ System prompt:       6.1k tokens (3.0%)
⛁ System tools:        9.3k tokens (4.7%)
⛁ Skills:              689 tokens (0.3%)
⛁ Messages:            1.3k tokens (0.7%)
⛶ Free space:          149.5k (74.8%)
⛝ Autocompact buffer:  33k tokens (16.5%)
```

## Breakdown

- **System prompt** — Claude's base instructions loaded at startup (~6k, fixed)
- **System tools** — built-in tool definitions (Read, Edit, Bash, etc.) (~9k, fixed)
- **Skills** — any loaded slash-command skills (~0.3k, fixed)
- **Messages** — your actual conversation history (grows as you chat)
- **Free space** — remaining tokens available for the session
- **Autocompact buffer** — reserved space so Claude can summarize and compress old messages before hitting the limit

## Why a Fresh Terminal Still Shows ~17k Tokens

Even in a brand new session, Claude Code pre-loads things automatically that consume tokens right away:

| Category | Tokens |
|----------|--------|
| System prompt | ~6k |
| System tools | ~9k |
| Skills | ~0.3k |
| Messages (empty) | ~8 tokens |
| **Total** | **~15–17k** |

This is fixed overhead — not your usage. Only the **Messages** category grows as you actually chat with Claude. So don't be surprised when a fresh terminal already shows 17k — that's completely normal.

## Fresh Terminal vs. Active Session

| | Messages Tokens | Total |
|---|---|---|
| Fresh terminal | ~8 tokens | ~15–17k |
| Active session (long chat) | 1k–3k+ | 18k+ |

Everything else (system prompt, tools, skills) stays the same across sessions. Only Messages grows as you converse.

## Key Takeaway
Every terminal = its own fresh 200k context window. Start a new terminal when you want a clean slate or need to run a parallel workstream without using up your current session's tokens. The autocompact buffer kicks in automatically when you're running low — Claude summarizes old messages to free up space.
