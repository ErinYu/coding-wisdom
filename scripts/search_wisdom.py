#!/usr/bin/env python3
"""
Search and browse the coding wisdom collection.

Usage:
    python3 search_wisdom.py --summary
    python3 search_wisdom.py --category <category>
    python3 search_wisdom.py --tags <tag1,tag2>
    python3 search_wisdom.py --search "<query>"
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime


# Category definitions
CATEGORIES = ["development", "debug", "trivial", "nonconsensus"]

CATEGORY_NAMES = {
    "development": "Development Principles",
    "debug": "Debug Principles",
    "trivial": "Trivial User Features",
    "nonconsensus": "Non-Consensus Tips"
}


def get_wisdom_dir():
    """Find the wisdom directory."""
    script_path = Path(__file__).resolve()
    skill_dir = script_path.parent.parent
    wisdom_dir = skill_dir / "wisdom"

    if not wisdom_dir.exists():
        print(f"❌ Wisdom directory not found: {wisdom_dir}")
        print(f"   Run 'python3 scripts/init_wisdom.py' first")
        sys.exit(1)

    return wisdom_dir


def parse_wisdom_file(file_path):
    """Parse a wisdom file and extract metadata."""
    content = file_path.read_text()
    lines = content.split('\n')

    metadata = {
        "path": file_path,
        "category": file_path.parent.name,
        "title": None,
        "tags": [],
        "date": None,
        "excerpt": None
    }

    in_frontmatter = False
    in_content = False
    content_lines = []

    for line in lines:
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
            else:
                in_frontmatter = False
                in_content = True
                continue

        if in_frontmatter:
            if line.startswith("tags: ["):
                tags_str = line[6:].rstrip("]")
                metadata["tags"] = [t.strip() for t in tags_str.split(",")]
            elif line.startswith("date: "):
                metadata["date"] = line[6:].strip()

        elif in_content:
            if line.startswith("# ") and not metadata["title"]:
                metadata["title"] = line[2:].strip()
            elif line.startswith("**Context:**"):
                content_lines.append(line)
            elif line.startswith("**The Principle:**"):
                content_lines.append(line)
            elif content_lines and not line.startswith("**"):
                # Add content lines (limited)
                if len(content_lines) < 5:
                    content_lines.append(line)

    metadata["excerpt"] = " ".join(content_lines[:3]) if content_lines else ""

    return metadata


def show_summary():
    """Show summary of all categories."""
    wisdom_dir = get_wisdom_dir()

    print("\n📚 Coding Wisdom Collection")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    total_count = 0
    latest_date = None

    for category in CATEGORIES:
        category_dir = wisdom_dir / category
        if category_dir.exists():
            files = list(category_dir.glob("*.md"))
            count = len(files)
            total_count += count

            # Get most recent file date
            latest = None
            if files:
                latest = max([f.stat().st_mtime for f in files])
                latest_date = datetime.fromtimestamp(latest).strftime('%Y-%m-%d')
            else:
                latest_date = "No items"

            print(f"  {CATEGORY_NAMES[category]:<30} ({count} items, last: {latest_date})")
        else:
            print(f"  {CATEGORY_NAMES[category]:<30} (0 items)")

    print(f"\n  {'Total:':<30} {total_count} items\n")


def search_by_category(category):
    """Search and display items in a specific category."""
    if category not in CATEGORIES:
        print(f"❌ Invalid category: {category}")
        print(f"   Valid categories: {', '.join(CATEGORIES)}")
        return

    wisdom_dir = get_wisdom_dir()
    category_dir = wisdom_dir / category

    if not category_dir.exists():
        print(f"❌ Category directory not found: {category}")
        return

    files = sorted(category_dir.glob("*.md"), reverse=True)

    if not files:
        print(f"\n📭 No wisdom found in {CATEGORY_NAMES[category]}\n")
        return

    print(f"\n📚 {CATEGORY_NAMES[category]}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    for i, file_path in enumerate(files, 1):
        metadata = parse_wisdom_file(file_path)

        print(f"{i}. {metadata['title'] or 'Untitled'}")
        print(f"   📁 {file_path.name}")
        if metadata['tags']:
            print(f"   🏷️  {', '.join(metadata['tags'])}")
        if metadata['excerpt']:
            # Clean excerpt for display
            excerpt = re.sub(r'\*\*', '', metadata['excerpt'])
            excerpt = excerpt[:100] + "..." if len(excerpt) > 100 else excerpt
            print(f"   📝 {excerpt}")
        print()

    print(f"Total: {len(files)} items\n")


def search_by_tags(tags):
    """Search for items with specific tags."""
    wisdom_dir = get_wisdom_dir()
    tags_set = set([t.strip().lower() for t in tags])

    results = []

    for category in CATEGORIES:
        category_dir = wisdom_dir / category
        if category_dir.exists():
            for file_path in category_dir.glob("*.md"):
                metadata = parse_wisdom_file(file_path)
                file_tags = set([t.lower() for t in metadata['tags']])

                # Check if any tag matches
                if tags_set & file_tags:
                    results.append(metadata)

    if not results:
        print(f"\n📭 No wisdom found with tags: {', '.join(tags)}\n")
        return

    print(f"\n🏷️  Wisdom with tags: {', '.join(tags)}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    for i, metadata in enumerate(results, 1):
        print(f"{i}. {metadata['title'] or 'Untitled'}")
        print(f"   📁 {metadata['path'].relative_to(wisdom_dir.parent)}")
        print(f"   🏷️  {', '.join(metadata['tags'])}")
        print(f"   📂 {CATEGORY_NAMES[metadata['category']]}")
        if metadata['excerpt']:
            excerpt = re.sub(r'\*\*', '', metadata['excerpt'])
            excerpt = excerpt[:100] + "..." if len(excerpt) > 100 else excerpt
            print(f"   📝 {excerpt}")
        print()

    print(f"Total: {len(results)} items\n")


def search_full_text(query):
    """Search for items containing the query text."""
    wisdom_dir = get_wisdom_dir()
    query_lower = query.lower()

    results = []

    for category in CATEGORIES:
        category_dir = wisdom_dir / category
        if category_dir.exists():
            for file_path in category_dir.glob("*.md"):
                content = file_path.read_text().lower()
                if query_lower in content:
                    metadata = parse_wisdom_file(file_path)
                    results.append(metadata)

    if not results:
        print(f"\n📭 No wisdom found containing: '{query}'\n")
        return

    print(f"\n🔍 Wisdom containing: '{query}'")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    for i, metadata in enumerate(results, 1):
        print(f"{i}. {metadata['title'] or 'Untitled'}")
        print(f"   📁 {metadata['path'].relative_to(wisdom_dir.parent)}")
        print(f"   📂 {CATEGORY_NAMES[metadata['category']]}")
        if metadata['excerpt']:
            excerpt = re.sub(r'\*\*', '', metadata['excerpt'])
            excerpt = excerpt[:100] + "..." if len(excerpt) > 100 else excerpt
            print(f"   📝 {excerpt}")
        print()

    print(f"Total: {len(results)} items\n")


def main():
    if len(sys.argv) < 2:
        show_summary()
        sys.exit(0)

    if sys.argv[1] in ["-h", "--help"]:
        print("Search and browse the coding wisdom collection.\n")
        print("Usage:")
        print("  python3 search_wisdom.py --summary")
        print("  python3 search_wisdom.py --category <category>")
        print("  python3 search_wisdom.py --tags <tag1,tag2>")
        print("  python3 search_wisdom.py --search '<query>'\n")
        print("Categories:")
        print(f"  {', '.join(CATEGORIES)}")
        sys.exit(0)

    arg = sys.argv[1]

    if arg == "--summary":
        show_summary()
    elif arg == "--category" and len(sys.argv) > 2:
        search_by_category(sys.argv[2])
    elif arg == "--tags" and len(sys.argv) > 2:
        tags = sys.argv[2].split(',')
        search_by_tags(tags)
    elif arg == "--search" and len(sys.argv) > 2:
        search_full_text(sys.argv[2])
    else:
        print("Invalid arguments. Use --help for usage.")
        sys.exit(1)


if __name__ == "__main__":
    main()
