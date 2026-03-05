---
category: debug
tags: [debugging, systematic]
context: general-debugging
date: 2026-03-05
---

# Change One Thing at a Time When Debugging

**Context:** Learned after hunting for a bug that was actually caused by changing two things simultaneously.

**The Principle:**
When debugging, make only one change at a time before testing. Changing multiple things at once makes it impossible to isolate which change caused the effect (or fixed the bug).

**Why It Works:**
- Isolates the cause of the bug
- Prevents introducing new bugs while fixing old ones
- Makes the fix reproducible and understandable
- Builds confidence in what actually fixed the problem

**When to Apply:**
- Any debugging session where the bug isn't obvious
- When working on unfamiliar code
- When the fix involves multiple potential changes
