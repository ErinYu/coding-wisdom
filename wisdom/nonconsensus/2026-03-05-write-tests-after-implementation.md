---
category: nonconsensus
tags: [testing, pragmatic, tdd]
context: rails-api-project
date: 2026-03-05
---

# Write Tests After Implementation Works

**Context:** Discovered during Rails API development after repeatedly rewriting tests during implementation changes.

**The Principle:**
Write tests after the implementation is working correctly, not before. This allows the test to codify the actual behavior rather than a preconceived notion of how it should work.

**When to Apply:**
- Exploratory development where the API surface is evolving
- Integration with external services where contracts are uncertain

**When NOT to Apply:**
- Well-defined business rules with clear acceptance criteria

**Why It Works:**
- Tests document what the code actually does, not what you thought it would do
- Avoids test rewrites during implementation discovery
- Catches edge cases you didn't anticipate when writing the test first
