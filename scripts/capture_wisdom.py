#!/usr/bin/env python3
"""
Capture coding wisdom and store it in the wisdom collection.

Usage:
    python3 capture_wisdom.py [--interactive]
    python3 capture_wisdom.py --category <category> --title <title> ...

Interactive mode prompts for all fields. Command-line mode accepts arguments.
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime


# Category definitions
CATEGORIES = ["development", "debug", "trivial", "nonconsensus"]

# Common tags for suggestions
COMMON_TAGS = [
    "testing", "performance", "ux", "ui", "debugging",
    "architecture", "api", "database", "frontend", "backend",
    "security", "refactoring", "pragmatic", "tdd", "design"
]


def slugify(text):
    """Convert text to kebab-case slug."""
    # Convert to lowercase and replace spaces/hyphens
    text = text.lower().strip()
    # Replace non-alphanumeric with hyphens
    text = re.sub(r'[^\w\s-]', '-', text)
    # Replace multiple spaces/hyphens with single hyphen
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def get_category():
    """Prompt user to select a category."""
    print("\n📝 Capture Coding Wisdom")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print("What type of wisdom did you discover?\n")

    for i, cat in enumerate(CATEGORIES, 1):
        name = cat.capitalize()
        if cat == "development":
            desc = "Approach, methodology, or philosophy for building software"
        elif cat == "debug":
            desc = "Systematic approach to finding and fixing issues"
        elif cat == "trivial":
            desc = "Small details that matter to users"
        else:  # nonconsensus
            desc = "Counter-intuitive but effective practice"
        print(f"  {i}. {name}: {desc}")

    while True:
        choice = input("\nSelect category (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice, please enter 1-4")


def get_field(prompt, required=True):
    """Prompt user for a field value."""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required. Please enter a value.")


def get_tags():
    """Prompt user for tags."""
    print("\n💡 Common tags:", ", ".join(COMMON_TAGS[:10]))
    print("   Enter comma-separated tags (or press Enter to skip):")

    while True:
        tags_input = input("Tags: ").strip()
        if not tags_input:
            return []

        tags = [t.strip().lower() for t in tags_input.split(',')]
        # Filter out empty tags
        tags = [t for t in tags if t]
        if tags:
            return tags
        print("Please enter at least one tag, or press Enter to skip.")


def create_wisdom_file(category, title, context, wisdom, why, when_apply=None, when_not=None, tags=None):
    """
    Create a wisdom file with the given content.

    Args:
        category: One of CATEGORIES
        title: Short, memorable title
        context: What led to this discovery
        wisdom: The principle/tip explanation
        why: Why it works
        when_apply: When to apply (optional)
        when_not: When NOT to apply (optional)
        tags: List of tags for categorization

    Returns:
        Path to created file, or None if error
    """
    # Find skill root (look for SKILL.md)
    script_path = Path(__file__).resolve()
    skill_dir = script_path.parent.parent
    wisdom_dir = skill_dir / "wisdom"

    # Verify wisdom directory exists
    if not wisdom_dir.exists():
        print(f"❌ Wisdom directory not found: {wisdom_dir}")
        print(f"   Run 'python3 scripts/init_wisdom.py' first")
        return None

    category_dir = wisdom_dir / category
    if not category_dir.exists():
        print(f"❌ Category directory not found: {category_dir}")
        return None

    # Generate filename
    date_str = datetime.now().strftime('%Y-%m-%d')
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    file_path = category_dir / filename

    # Build YAML frontmatter
    frontmatter = [
        "---",
        f"category: {category}",
    ]

    if tags:
        tags_list = ", ".join(tags)
        frontmatter.append(f"tags: [{tags_list}]")

    frontmatter.extend([
        f"context: {slugify(context)}",
        f"date: {date_str}",
        "---",
    ])

    # Build content
    content_lines = [
        "\n".join(frontmatter),
        "",
        f"# {title}",
        "",
        f"**Context:** {context}",
        "",
        "**The Principle:**",
        wisdom,
        "",
    ]

    if when_apply:
        content_lines.extend([
            "**When to Apply:**",
            when_apply,
            "",
        ])

    if when_not:
        content_lines.extend([
            "**When NOT to Apply:**",
            when_not,
            "",
        ])

    content_lines.extend([
        "**Why It Works:**",
        why,
    ])

    # Write file
    try:
        file_path.write_text("\n".join(content_lines))
        return file_path
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return None


def capture_interactive():
    """Run interactive capture mode."""
    print("\n🚀 Starting interactive wisdom capture...\n")

    # Step 1: Category
    category = get_category()

    # Step 2: Title
    print(f"\n📌 Selected: {category.capitalize()}")
    title = get_field("Title (short, memorable): ")

    # Step 3: Context
    context = get_field("\nWhat context led to this discovery? ")

    # Step 4: The wisdom
    wisdom = get_field("\nExplain the principle/tip clearly: ")

    # Step 5: Why it works
    why = get_field("\nWhy does this work? (Rationale): ")

    # Step 6: When to apply
    when_apply = get_field("\nWhen to apply this? (press Enter to skip): ", required=False)

    # Step 7: When NOT to apply
    when_not = get_field("\nWhen NOT to apply this? (press Enter to skip): ", required=False)

    # Step 8: Tags
    tags = get_tags()

    # Create the file
    print("\n💾 Saving wisdom...")
    file_path = create_wisdom_file(
        category=category,
        title=title,
        context=context,
        wisdom=wisdom,
        why=why,
        when_apply=when_apply if when_apply else None,
        when_not=when_not if when_not else None,
        tags=tags if tags else None
    )

    if file_path:
        print(f"\n✅ Wisdom captured successfully!")
        print(f"   Location: {file_path}")
        print(f"   Category: {category}")
        print(f"   Title: {title}")
        if tags:
            print(f"   Tags: {', '.join(tags)}")
        return file_path
    else:
        print("\n❌ Failed to capture wisdom")
        return None


def main():
    # Parse arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help"]:
            print("Capture coding wisdom and store it in the wisdom collection.\n")
            print("Usage:")
            print("  python3 capture_wisdom.py [--interactive]")
            print("  python3 capture_wisdom.py --category <cat> --title <title> ...\n")
            print("Interactive mode prompts for all fields.")
            print("Command-line mode: --category, --title, --context, --wisdom, --why, --tags")
            sys.exit(0)
        elif sys.argv[1] == "--interactive":
            result = capture_interactive()
            sys.exit(0 if result else 1)
        else:
            # Command-line mode (simplified - just show help for now)
            print("Command-line mode not fully implemented.")
            print("Use --interactive for prompts, or see --help")
            sys.exit(1)
    else:
        # Default to interactive
        result = capture_interactive()
        sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
