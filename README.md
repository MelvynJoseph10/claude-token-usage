# Claude Token Usage — How Context Windows Work

A quick reference for understanding how Claude Code manages token usage across terminal sessions.

---

## Each Terminal Gets Its Own 200k Context Window

This is a common misconception — terminals do **not** share a token pool. Each session is completely independent.

| Terminal | Context Window |
|----------|---------------|
| Terminal 1 | 0 – 200k tokens |
| Terminal 2 | 0 – 200k tokens |
| Terminal 3 | 0 – 200k tokens |

Open 3 terminals → 3 × 200k = 600k tokens effectively available in parallel.

---

## Check Your Token Usage with `/context`

Run `/context` inside Claude Code to see a breakdown of your current session's token usage.

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

---

## Token Categories Explained

| Category | What It Is |
|----------|-----------|
| **System prompt** | Claude's base instructions loaded at startup (~6k, fixed) |
| **System tools** | Built-in tool definitions like Read, Edit, Bash (~9k, fixed) |
| **Skills** | Loaded slash-command skills (~0.3k, fixed) |
| **Messages** | Your actual conversation history — grows as you chat |
| **Free space** | Remaining tokens available for the session |
| **Autocompact buffer** | Reserved space so Claude can compress old messages before hitting the limit |

---

## Fresh Terminal vs. Active Session

| | Messages tokens | Total |
|-|----------------|-------|
| Fresh terminal | ~8 tokens | ~16k |
| Active session (long chat) | 1k–3k tokens | ~17k+ |

The system prompt, tools, and skills are the same in every session. Only **Messages** grows as you converse.

---

## Key Takeaways

- `/context` shows your token usage — run it anytime
- Every terminal = its own fresh 200k window
- Start a new terminal for a clean slate or to run parallel workstreams
- The autocompact buffer kicks in automatically when you're running low — Claude summarizes old messages to free up space

---

## How to Use `/context`

1. Open Claude Code in any terminal
2. Type `/context` and press Enter
3. You'll see a visual breakdown of your current session's token usage

---

## Statusline Script (`statusline.py`)

A Python script that displays a live token usage bar in your terminal statusline.

**Output looks like:**
```
claude-sonnet-4-6 | [████░░░░░░░░░░░░░░░░] 9% | 17k/200k tokens
```

**Setup:**
```bash
# Place the script in your Claude config directory
cp statusline.py ~/.claude/statusline.py
chmod +x ~/.claude/statusline.py

# Run it
python3 ~/.claude/statusline.py
```

The script reads token usage data from Claude Code's JSON output and renders a progress bar with model name, percentage used, and token counts.
