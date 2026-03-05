---
name: coding-wisdom
description: This skill should be used during or after coding tasks to systematically capture and organize development wisdom. Accumulates development principles, debug principles, trivial but user-caring features, and non-consensus coding tips from real coding experiences. Also retrieve relevant wisdom before starting new tasks.
---

# Coding Wisdom

Systematically capture and organize coding wisdom accumulated during development tasks. This skill transforms fleeting insights into a reusable knowledge base that improves over time.

## When to Use This Skill

**Use during/after coding when:**
- You discovered a pattern that worked well
- You debugged something in an insightful way
- You noticed a small detail that users care about
- You learned something counter-intuitive
- The user expresses discovery ("Ah, that's the pattern")

**Use before coding when:**
- Starting a new feature (search development principles)
- Investigating a bug (search debug principles)
- Making user-facing changes (search trivial user features)

## The Four Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Development Principles** | High-level approaches to building software | "Read existing code before writing new code" |
| **Debug Principles** | Systematic approaches to troubleshooting | "Always reproduce the bug before fixing" |
| **Trivial User Features** | Small details users care about | "Button hover states provide confidence" |
| **Non-Consensus Tips** | Counter-intuitive but effective practices | "Write tests after implementation works" |

## Mode Detection

Determine what the user wants:

- **Mode A: Capture Wisdom** — User just finished coding or expressed a discovery. Go to **Capture Mode**.
- **Mode B: Find Wisdom** — User is starting a new task. Go to **Search Mode**.
- **Mode C: Browse Wisdom** — User wants to explore accumulated wisdom. Go to **Browse Mode**.

---

## Capture Mode

Use this mode after coding sessions to capture what was learned.

### Step 1: Determine Category

**Ask all questions in a single AskUserQuestion call:**

```
question: "What type of wisdom did you discover?"
header: "Capture Wisdom"
options:
  - label: "Development Principle"
    description: "Approach, methodology, or philosophy for building software"
  - label: "Debug Principle"
    description: "Systematic approach to finding and fixing issues"
  - label: "Trivial User Feature"
    description: "Small details that matter to users"
  - label: "Non-Consensus Tip"
    description: "Counter-intuitive but effective practice"
```

### Step 2: Gather Wisdom Details

**Ask in a single AskUserQuestion call:**

```
question: "Provide a title for this wisdom (short, memorable)"
header: "Title"

Then ask:
question: "What context led to this discovery?"
header: "Context"

Then ask:
question: "Explain the principle/tip clearly"
header: "The Wisdom"

Then ask:
question: "Why does this work? What's the rationale?"
header: "Why It Works"

Then ask (multiSelect):
question: "Select relevant tags"
header: "Tags"
options:
  - label: "testing"
  - label: "performance"
  - label: "ux/ui"
  - label: "debugging"
  - label: "architecture"
  - label: "api"
  - label: "database"
  - label: "custom..."
```

### Step 3: Create Wisdom File

After gathering details, create a wisdom file:

```bash
python3 scripts/capture_wisdom.py \
  --category "{category}" \
  --title "{title}" \
  --context "{context}" \
  --wisdom "{wisdom}" \
  --why "{why}" \
  --tags "{tags}"
```

This creates `wisdom/{category}/{YYYY-MM-DD}-{slug}.md` with formatted content.

**Fallback:** If the script fails, manually create the file using the template in [references/wisdom-template.md](references/wisdom-template.md).

### Step 4: Confirm

Display what was captured:
- File path
- Category
- Title
- Tags

Ask: "Capture more wisdom?" — If yes, repeat from Step 1.

---

## Search Mode

Use this mode before starting new tasks to find relevant wisdom.

### Step 1: Determine Task Type

```
question: "What type of task are you starting?"
header: "Find Wisdom"
options:
  - label: "New Feature Development"
    description: "Search development principles"
  - label: "Bug Investigation"
    description: "Search debug principles"
  - label: "User-Facing Changes"
    description: "Search trivial user features"
  - label: "All Wisdom"
    description: "Browse everything"
```

### Step 2: Search and Display

```bash
# For category-based search
python3 scripts/search_wisdom.py --category {category}

# For tag-based search
python3 scripts/search_wisdom.py --tags {tag1,tag2}

# For full-text search
python3 scripts/search_wisdom.py --search "{query}"
```

**Fallback:** If script fails, use grep:
```bash
grep -r "{query}" wisdom/
```

Display results with:
- Title
- Category
- Excerpt of the wisdom
- File path for full reading

### Step 3: Offer to Read Full Content

If results are found, ask:
```
question: "Would you like to read any of these wisdom items in full?"
header: "Read Full"
options:
  - "Read all matching items"
  - "Read specific item (enter number)"
  - "Done searching"
```

---

## Browse Mode

Use this mode to explore accumulated wisdom by category.

### Step 1: Show Category Summary

First, get counts per category:
```bash
python3 scripts/search_wisdom.py --summary
```

Display:
```
Browse Wisdom
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Development Principles  (N items, last updated YYYY-MM-DD)
  Debug Principles        (N items, last updated YYYY-MM-DD)
  Trivial User Features   (N items, last updated YYYY-MM-DD)
  Non-Consensus Tips      (N items, last updated YYYY-MM-DD)
```

### Step 2: Category Selection

```
question: "Which category to browse?"
header: "Browse Wisdom"
options:
  - label: "Development Principles"
    description: "{count} items - last updated {date}"
  - label: "Debug Principles"
    description: "{count} items - last updated {date}"
  - label: "Trivial User Features"
    description: "{count} items - last updated {date}"
  - label: "Non-Consensus Tips"
    description: "{count} items - last updated {date}"
```

### Step 3: Display Category Items

List all items in selected category with:
- Title
- Date
- Tags
- Brief excerpt

Ask if user wants to read any item in full.

---

## Quick Reference

### Wisdom Storage Structure

```
wisdom/
├── development/     # Development principles
├── debug/           # Debug principles
├── trivial/         # Trivial user features
└── nonconsensus/    # Non-consensus tips
```

### Common Commands

```bash
# Initialize wisdom storage (run once)
python3 scripts/init_wisdom.py

# Capture wisdom interactively
python3 scripts/capture_wisdom.py

# Search by category
python3 scripts/search_wisdom.py --category development

# Search by tags
python3 scripts/search_wisdom.py --tags testing,debugging

# Get category summary
python3 scripts/search_wisdom.py --summary

# Full-text search
python3 scripts/search_wisdom.py --search "test"
```

### Manual Fallback (No Script)

If scripts fail, work directly:

**Create wisdom file:**
```bash
# Determine file path
CATEGORY="development"
DATE=$(date +%Y-%m-%d)
SLUG="write-tests-after-implementation" # kebab-case from title
FILE="wisdom/${CATEGORY}/${DATE}-${SLUG}.md"

# Create file with template
cat > "$FILE" << 'EOF'
---
category: development
tags: [testing, pragmatic]
context: rails-api-project
date: 2026-03-05
---

# Write Tests After Implementation Works

**Context:** Discovered during Rails API development after repeatedly rewriting tests during implementation changes.

**The Principle:**
Write tests after the implementation is working correctly, not before.

**Why It Works:**
- Tests document what the code actually does
- Avoids test rewrites during implementation discovery
- Catches edge cases you didn't anticipate

**When to Apply:**
- Exploratory development
- Integration with external services

**When NOT to Apply:**
- Well-defined business rules
EOF
```

**Search manually:**
```bash
# By category
ls -1 wisdom/development/

# By tag
grep -l "testing" wisdom/**/*.md

# Full text
grep -r "query" wisdom/
```

---

## Principles for Good Wisdom

When capturing wisdom, follow these guidelines:

**Make it generalizable:**
- Good: "Test after implementation when API surface is evolving"
- Bad: "Test after implementation in user_controller.rb line 42"

**Include context:**
- What were you working on?
- What problem led to this discovery?
- What assumptions did you have?

**Explain why:**
- Don't just state the principle
- Explain the reasoning behind it
- Note when it doesn't apply

**Keep it actionable:**
- What should someone do differently?
- When should they apply this?
- What are the trade-offs?

---

## Supporting Files

| File | Purpose | When to Use |
|------|---------|-------------|
| [scripts/init_wisdom.py](scripts/init_wisdom.py) | Initialize wisdom storage structure | First time using skill |
| [scripts/capture_wisdom.py](scripts/capture_wisdom.py) | Interactive wisdom capture | Capture mode |
| [scripts/search_wisdom.py](scripts/search_wisdom.py) | Search and browse wisdom | Search/browse mode |
| [references/categories.md](references/categories.md) | Detailed category definitions | Understanding categories |
| [references/wisdom-template.md](references/wisdom-template.md) | Template for manual wisdom creation | Script fallback |
