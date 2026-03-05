# Wisdom Item Template

Use this template to manually create wisdom files when the capture script is unavailable.

## File Location

Wisdom files are stored in category-specific directories:

```
wisdom/
├── development/     # Development principles
├── debug/           # Debug principles
├── trivial/         # Trivial user features
└── nonconsensus/    # Non-consensus tips
```

## File Naming

Format: `{YYYY-MM-DD}-{slug}.md`

- Date: When the wisdom was captured
- Slug: Kebab-case version of the title

Examples:
- `2026-03-05-write-tests-after-implementation.md`
- `2026-03-05-button-hover-states.md`
- `2026-03-05-reproduce-before-fixing.md`

## Template

```markdown
---
category: development
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
- Critical code paths where behavior must be specified upfront

**Why It Works:**
- Tests document what the code actually does, not what you thought it would do
- Avoids test rewrites during implementation discovery
- Catches edge cases you didn't anticipate when writing the test first
```

## Field Explanations

### YAML Frontmatter

| Field | Description | Example |
|-------|-------------|---------|
| `category` | One of: development, debug, trivial, nonconsensus | `development` |
| `tags` | Comma-separated list of relevant tags | `[testing, pragmatic, tdd]` |
| `context` | Kebab-case description of the context | `rails-api-project` |
| `date` | When this wisdom was captured | `2026-03-05` |

### Content Sections

| Section | Description | Required |
|---------|-------------|----------|
| `# Title` | Short, memorable title | Yes |
| `**Context:**` | What led to this discovery | Yes |
| `**The Principle:**` | Clear explanation of the wisdom | Yes |
| `**When to Apply:**` | Usage guidance | Recommended |
| `**When NOT to Apply:**` | Counter-indications | Optional |
| `**Why It Works:**` | Rationale and reasoning | Yes |

## Best Practices

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

## Common Tags

| Tag | When to Use |
|-----|-------------|
| `testing` | Test-related wisdom |
| `performance` | Performance optimization |
| `ux` / `ui` | User experience/interface |
| `debugging` | Debug approaches |
| `architecture` | Design/architecture decisions |
| `api` | API design/usage |
| `database` | Database-related |
| `frontend` | Frontend-specific |
| `backend` | Backend-specific |
| `security` | Security considerations |
| `refactoring` | Code restructuring |
| `pragmatic` | Practical vs idealistic |
| `tdd` | Test-driven development |
| `design` | Design-related |
