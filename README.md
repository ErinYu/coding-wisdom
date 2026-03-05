# Coding Wisdom for Claude Code

> Systematically capture and organize coding wisdom accumulated during development tasks.

A Claude Code skill that helps you build a personal knowledge base of coding insights. Capture development principles, debug approaches, user-caring details, and non-consensus tips that emerge during real coding work.

## Features

- **📝 Capture Mode** - Record wisdom after coding sessions with rich interactive prompts
- **🔍 Search Mode** - Find relevant wisdom before starting new tasks
- **📚 Browse Mode** - Explore accumulated wisdom by category
- **🏷️ Tag System** - Organize wisdom with searchable tags

## Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Development Principles** | High-level approaches to building software | "Read existing code before writing new code" |
| **Debug Principles** | Systematic approaches to troubleshooting | "Change one thing at a time when debugging" |
| **Trivial User Features** | Small details users care about | "Button hover states provide user confidence" |
| **Non-Consensus Tips** | Counter-intuitive but effective practices | "Write tests after implementation works" |

## Installation

### Option 1: Install from GitHub (recommended)

1. Clone this repository to your local skills directory:
```bash
cd ~/.claude/skills
git clone https://github.com/your-username/coding-wisdom.git
```

2. Restart Claude Code

3. The skill will be automatically available

### Option 2: Manual Installation

1. Copy the `coding-wisdom/` folder to `~/.claude/skills/`
2. Restart Claude Code

## Usage

### Capture Wisdom

After completing a coding task, capture what you learned:

1. Invoke the skill: "Use coding-wisdom to capture something I learned"
2. Select the category (Development, Debug, Trivial, Non-Consensus)
3. Answer the prompts:
   - Title (short, memorable)
   - Context (what led to this discovery)
   - The Principle (clear explanation)
   - Why It Works (rationale)
   - Tags (for categorization)

### Search Wisdom

Before starting a new task, find relevant insights:

```bash
# View summary of all wisdom
python3 ~/.claude/skills/coding-wisdom/scripts/search_wisdom.py --summary

# Search by category
python3 ~/.claude/skills/coding-wisdom/scripts/search_wisdom.py --category debug

# Search by tags
python3 ~/.claude/skills/coding-wisdom/scripts/search_wisdom.py --tags testing,debugging

# Full-text search
python3 ~/.claude/skills/coding-wisdom/scripts/search_wisdom.py --search "test"
```

### Command-Line Interface

```bash
# Interactive capture
python3 scripts/capture_wisdom.py --interactive

# Get help
python3 scripts/search_wisdom.py --help
```

## File Structure

```
coding-wisdom/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── SKILL.md                 # Main skill instructions
├── scripts/
│   ├── init_wisdom.py       # Initialize wisdom storage
│   ├── capture_wisdom.py    # Interactive capture script
│   └── search_wisdom.py     # Search by category/tags
├── references/
│   ├── categories.md        # Detailed category definitions
│   └── wisdom-template.md   # Template for manual creation
├── wisdom/
│   ├── development/         # Development principles
│   ├── debug/               # Debug principles
│   ├── trivial/             # Trivial user features
│   └── nonconsensus/        # Non-consensus tips
├── LICENSE
└── README.md
```

## Wisdom Storage Format

Each wisdom item is stored as a markdown file:

```markdown
---
category: nonconsensus
tags: [testing, pragmatic]
context: rails-api-project
date: 2026-03-05
---

# Write Tests After Implementation Works

**Context:** Discovered during Rails API development after repeatedly rewriting tests.

**The Principle:**
Write tests after the implementation is working correctly, not before.

**When to Apply:**
- Exploratory development where the API surface is evolving
- Integration with external services where contracts are uncertain

**When NOT to Apply:**
- Well-defined business rules with clear acceptance criteria

**Why It Works:**
- Tests document what the code actually does
- Avoids test rewrites during implementation discovery
- Catches edge cases you didn't anticipate
```

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

Inspired by the Claude Code plugin ecosystem and the following skills:
- **file-todos** - File-based tracking system patterns
- **setup** - Rich CLI interaction patterns
- **dhh-rails-style** - Knowledge organization patterns
- **brainstorming** - Phase-based workflow patterns

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Mention `@coding-wisdom` in Claude Code conversations

---

**Made with ❤️ for the Claude Code community**
