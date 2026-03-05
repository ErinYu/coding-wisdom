# Coding Wisdom Categories

Detailed definitions and examples for each wisdom category.

## Development Principles

**Definition:** High-level approaches, methodologies, and philosophies for building software. These are the "mindsets" that guide how you approach development work.

**What belongs here:**
- Approaches to code organization and architecture
- Philosophies about when to build vs. buy
- Principles about code readability and maintainability
- Mental models for thinking about software design
- Strategies for feature development

**Examples:**
- "Read existing code before writing new code"
- "Build the feature first, optimize later"
- "Delete code instead of commenting it out"
- "The best code is the code you don't write"

**What doesn't belong here:**
- Specific debugging techniques (use Debug Principles)
- UI/UX details (use Trivial User Features)
- Counter-intuitive tricks (use Non-Consensus Tips)

---

## Debug Principles

**Definition:** Systematic approaches to troubleshooting, finding, and fixing issues. These are the "methods" you use when something isn't working.

**What belongs here:**
- Systematic approaches to diagnosis
- Principles for reproducing bugs
- Strategies for isolating problems
- Methods for understanding error messages
- Approaches to fixing issues without breaking things

**Examples:**
- "Always reproduce the bug before fixing"
- "Change one thing at a time when debugging"
- "Read the error message from the bottom up"
- "Add logging before adding breakpoints"
- "The fastest way to find a bug is to prove what it's NOT"

**What doesn't belong here:**
- General development philosophies (use Development Principles)
- User-facing observations (use Trivial User Features)
- Coding tricks (use Non-Consensus Tips)

---

## Trivial User Features

**Definition:** Small, often-overlooked details that matter to users. These are the "delighters" that developers might dismiss as trivial but users genuinely care about.

**What belongs here:**
- UI details that provide confidence or feedback
- Small interactions that improve perceived performance
- Visual or behavioral polish users notice
- Edge cases that affect user experience
- Accessibility and usability details

**Examples:**
- "Button hover states provide user confidence"
- "Loading indicators should have meaning, not just spin"
- "Error messages should explain what to do next"
- "Success feedback should be immediate, even if processing isn't"
- "Empty states should guide users to the next action"

**What doesn't belong here:**
- Development philosophies (use Development Principles)
- Debugging techniques (use Debug Principles)
- Code-level tricks (use Non-Consensus Tips)

---

## Non-Consensus Tips

**Definition:** Counter-intuitive, unconventional, or controversial practices that work despite going against common wisdom. These are the "surprises" that contradict what you typically read or hear.

**What belongs here:**
- Practices that contradict conventional wisdom
- Approaches that seem wrong but work
- Controversial opinions backed by experience
- Timing-related or context-specific advice
- "Do the opposite of what X says" type insights

**Examples:**
- "Write tests after implementation works" (contradicts TDD)
- "Commit before tests pass to save work" (contradicts clean workflow)
- "Add comments for what the code DOES, not why" (contradicts common advice)
- "Use global state for this specific pattern" (contradicts best practices)
- "Copy-paste is OK for one-off scripts" (contradicts DRY)

**What doesn't belong here:**
- Standard development practices (use Development Principles)
- Debugging methods (use Debug Principles)
- User-facing details (use Trivial User Features)

---

## Choosing the Right Category

When capturing wisdom, ask:

1. **Is this a mindset or philosophy?** → Development Principles
2. **Is this about finding/fixing problems?** → Debug Principles
3. **Is this about what users notice/care about?** → Trivial User Features
4. **Is this counter-intuitive or controversial?** → Non-Consensus Tips

Uncertain? Choose Non-Consensus Tips—it's often the right home for surprising insights.
