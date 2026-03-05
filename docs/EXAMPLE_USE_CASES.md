# Coding Wisdom Skill - Example Use Cases

This document provides example use cases for the official Claude Code plugin directory submission.

---

## Example 1: Capturing a Debug Principle After a Tricky Bug Fix

**User says:**
> "I just spent 2 hours debugging a race condition. Turned out I was changing multiple things at once. I should use coding-wisdom to capture what I learned."

**Skill response:**
```
What type of wisdom did you discover?

1. Development Principle - Approach, methodology, or philosophy for building software
2. Debug Principle - Systematic approach to finding and fixing issues  ← SELECT
3. Trivial User Feature - Small details that matter to users
4. Non-Consensus Tip - Counter-intuitive but effective practice

---

Title: Change One Thing at a Time When Debugging

Context: Hunting a race condition for 2 hours; was changing multiple variables simultaneously.

The Principle: Make only one change before testing. If you change multiple things, you can't isolate which change fixed (or caused) the problem.

Why It Works: Isolates the root cause, prevents introducing new bugs while fixing old ones, makes the fix reproducible.

When to Apply: Any debugging session where the cause isn't obvious.

Tags: debugging, systematic

✅ Wisdom captured to wisdom/debug/2026-03-05-change-one-thing-at-a-time.md
```

---

## Example 2: Capturing a Non-Consensus Testing Insight

**User says:**
> "I realized I waste so much time rewriting tests when the API keeps evolving. I started writing tests AFTER the implementation works and it's so much faster. Let me save this insight."

**Skill response:**
```
What type of wisdom did you discover?

1. Development Principle
2. Debug Principle
3. Trivial User Feature
4. Non-Consensus Tip - Counter-intuitive but effective practice  ← SELECT

---

Title: Write Tests After Implementation Works

Context: Rails API development, kept rewriting tests during implementation changes.

The Principle: Write tests after the implementation is working correctly, not before. Tests should codify actual behavior, not preconceived notions.

Why It Works: Tests document what the code actually does (not what you thought), avoids test rewrites during API evolution, catches edge cases you didn't anticipate.

When to Apply: Exploratory development where API surface is evolving, integration with external services.

When NOT to Apply: Well-defined business rules with clear acceptance criteria.

Tags: testing, pragmatic, tdd, counter-intuitive

✅ Wisdom captured to wisdom/nonconsensus/2026-03-05-write-tests-after-implementation.md
```

---

## Example 3: Capturing a User-Facing Detail

**User says:**
> "Users complained the button felt 'broken' even though it worked. Turns out they needed hover state feedback. Let me capture this."

**Skill response:**
```
What type of wisdom did you discover?

1. Development Principle
2. Debug Principle
3. Trivial User Feature - Small details that matter to users  ← SELECT
4. Non-Consensus Tip

---

Title: Button Hover States Provide User Confidence

Context: Users reported button felt "broken" despite working correctly; missing hover feedback caused uncertainty.

The Principle: Hover states aren't just decoration—they signal interactivity and confirm the element is clickable. Missing hover states make users doubt if something works.

Why It Works: Provides immediate visual feedback, reduces user hesitation, communicates interaction affordance.

When to Apply: Any interactive UI element, especially primary actions.

Tags: ux, ui, user-feedback, trivial-but-important

✅ Wisdom captured to wisdom/trivial/2026-03-05-button-hover-states.md
```

---

## Example 4: Searching Wisdom Before Starting a Bug Fix

**User says:**
> "I need to fix this authentication bug. Let me check if I've captured any debugging wisdom before."

**Skill response:**
```
What type of task are you starting?

1. New Feature Development
2. Bug Investigation  ← SELECT
3. User-Facing Changes
4. All Wisdom

---

🔍 Found 2 relevant items in Debug Principles:

1. "Change One Thing at a Time When Debugging"
   📁 wisdom/debug/2026-03-05-change-one-thing-at-a-time.md
   🏷️ debugging, systematic
   📝 Make only one change before testing. If you change multiple things...

2. "Reproduce the Bug Before Fixing"
   📁 wisdom/debug/2026-03-05-reproduce-before-fixing.md
   🏷️ debugging, reproduction
   📝 Always reproduce the bug in a clean environment before making changes...

Would you like to read any of these in full?
```

---

## Example 5: Browsing All Wisdom by Category

**User says:**
> "Show me all the debug wisdom I've collected."

**Skill response:**
```
📚 Coding Wisdom Collection
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Development Principles         (5 items, last: 2026-03-05)
  Debug Principles               (3 items, last: 2026-03-05)  ←
  Trivial User Features          (2 items, last: 2026-03-04)
  Non-Consensus Tips             (4 items, last: 2026-03-05)

  Total:                         14 items

---

Which category to browse?

1. Development Principles (5 items)
2. Debug Principles (3 items)  ← SELECT
3. Trivial User Features (2 items)
4. Non-Consensus Tips (4 items)

---

📚 Debug Principles

1. Change One Thing at a Time When Debugging
   📁 2026-03-05-change-one-thing-at-a-time.md
   🏷️ debugging, systematic

2. Reproduce the Bug Before Fixing
   📁 2026-03-05-reproduce-before-fixing.md
   🏷️ debugging, reproduction

3. Read Error Messages from Bottom to Top
   📁 2026-03-04-read-errors-bottom-up.md
   🏷️ debugging, error-handling

Total: 3 items
```

---

## Example 6: Capturing a Development Philosophy

**User says:**
> "I've learned that reading existing code before writing new code saves so much time. I should capture this principle."

**Skill response:**
```
What type of wisdom did you discover?

1. Development Principle - Approach, methodology, or philosophy for building software  ← SELECT
2. Debug Principle
3. Trivial User Feature
4. Non-Consensus Tip

---

Title: Read Existing Code Before Writing New Code

Context: Starting work on a new feature; spent 30 minutes reading related code first and discovered patterns that saved hours.

The Principle: Always read existing code in the relevant area before writing new code. You'll discover patterns, conventions, and often find a similar problem already solved.

Why It Works: Avoids reinventing the wheel, ensures consistency with existing patterns, reveals edge cases others already handled, prevents duplicate solutions.

When to Apply: Any time you're modifying or extending existing codebase.

Tags: development, code-reading, patterns, onboarding

✅ Wisdom captured to wisdom/development/2026-03-05-read-existing-code.md
```

---

## Example 7: Full-Text Search for Specific Topics

**User says:**
> "I need to work on database optimization. What wisdom do I have about performance?"

**Skill response:**
```
🔍 Searching for: "performance"

Found 3 matching items:

1. "Profile Before Optimizing" (Development Principles)
   📁 wisdom/development/2026-03-03-profile-before-optimizing.md
   🏷️ performance, optimization
   📝 Never optimize without profiling first. Measure twice, cut once...

2. "N+1 Queries Kill Performance" (Non-Consensus Tips)
   📁 wisdom/nonconsensus/2026-03-04-n-plus-one-queries.md
   🏷️ performance, database, rails
   📝 N+1 queries are the most common performance killer in ORMs...

3. "Database Index Checklist" (Debug Principles)
   📁 wisdom/debug/2026-03-02-index-checklist.md
   🏷️ database, performance, indexing
   📝 Before declaring a query slow, run EXPLAIN and check...

Would you like to read any of these in full?
```

---

## Key Characteristics Demonstrated

These examples show:

1. **Rich CLI Interaction** - Clear prompts with numbered options and descriptive labels
2. **Structured Capture** - Collects all relevant information (title, context, principle, why, when to apply, tags)
3. **Multiple Search Modes** - By category, by tags, full-text search
4. **Summary View** - Shows counts and recency for quick overview
5. **Persistent Storage** - Wisdom stored in organized markdown files for future reference
6. **Applicability** - Works across different coding scenarios (debugging, testing, UX, development)
