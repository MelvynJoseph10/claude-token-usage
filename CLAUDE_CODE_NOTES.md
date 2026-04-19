# Claude Code — Useful Notes

## Context Window per Terminal Session

Each terminal running Claude Code gets its **own independent 200k token context window**. They do **not** share a pool.

| Terminal | Context Window |
|----------|---------------|
| Terminal 1 | 0 – 200k tokens |
| Terminal 2 | 0 – 200k tokens |
| Terminal 3 | 0 – 200k tokens |

So if you open 3 terminals, you effectively have 3 × 200k = 600k tokens available across sessions.

---

## Checking Context Usage with `/context`

Run `/context` inside Claude Code to see how your 200k token budget is being used in the current session.

**Example output:**

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

**Breakdown:**
- **System prompt** — Claude's base instructions loaded at startup
- **System tools** — built-in tool definitions (Read, Edit, Bash, etc.)
- **Skills** — any loaded slash-command skills
- **Messages** — your actual conversation history (grows as you chat)
- **Free space** — remaining tokens available for the session
- **Autocompact buffer** — reserved space so Claude can summarize and compress old messages before hitting the limit

### Fresh terminal vs. active session

A brand-new terminal shows ~8 tokens in Messages (almost nothing). An active session with a long conversation will show 1k–2k+ tokens in Messages. Everything else (system prompt, tools, skills) stays roughly the same across sessions.

---

## Key Takeaway

> Every terminal = its own fresh 200k context window. Start a new terminal when you want a clean slate or need to run a parallel workstream without using up your current session's tokens.
