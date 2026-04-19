#!/usr/bin/env python3
import json, sys, select

data = {}
try:
    if select.select([sys.stdin], [], [], 0.2)[0]:
        raw = sys.stdin.read()
        if raw.strip():
            data = json.loads(raw)
except Exception:
    pass

model = data.get("model", {}).get("display_name", "Claude")
ctx = data.get("context_window", {})
pct = ctx.get("used_percentage", 0)
max_tokens = ctx.get("context_window_size", 200000)
used = int(max_tokens * pct / 100)

if not data:
    print("Claude | [░░░░░░░░░░░░░░░░░░░░] 0% | 0k/200k tokens | Ready")
    sys.exit(0)

bar_width = 20
filled = int(bar_width * pct / 100)
bar = "█" * filled + "░" * (bar_width - filled)

def fmt(n):
    return f"{n/1000:.0f}k" if n >= 1000 else str(n)

print(f"{model} | [{bar}] {pct}% | {fmt(used)}/{fmt(max_tokens)} tokens")
