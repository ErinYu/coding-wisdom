#!/usr/bin/env python3
"""
Initialize wisdom storage structure for coding-wisdom skill.

Usage:
    python3 init_wisdom.py [--path <path>]

Creates the directory structure for storing wisdom items:
    wisdom/
    ├── development/
    ├── debug/
    ├── trivial/
    └── nonconsensus/
"""

import os
import sys
from pathlib import Path
from datetime import datetime


# Category definitions
CATEGORIES = [
    "development",    # Development principles
    "debug",          # Debug principles
    "trivial",        # Trivial user features
    "nonconsensus"    # Non-consensus tips
]


def init_wisdom(path="."):
    """
    Initialize wisdom storage structure.

    Args:
        path: Base path for wisdom storage (default: current directory)

    Returns:
        Path to wisdom directory, or None if error
    """
    # Determine wisdom directory path
    wisdom_dir = Path(path).resolve() / "wisdom"

    # Check if already initialized
    if wisdom_dir.exists():
        # Verify structure
        existing_dirs = set([d.name for d in wisdom_dir.iterdir() if d.is_dir()])
        expected_dirs = set(CATEGORIES)

        if existing_dirs == expected_dirs:
            print(f"✅ Wisdom storage already initialized at: {wisdom_dir}")
            return wisdom_dir
        else:
            print(f"⚠️  Wisdom directory exists but structure incomplete.")
            print(f"   Expected: {expected_dirs}")
            print(f"   Found: {existing_dirs}")
            response = input("Recreate missing directories? (y/n): ")
            if response.lower() != 'y':
                return None

    # Create wisdom directory
    try:
        wisdom_dir.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created wisdom directory: {wisdom_dir}")
    except Exception as e:
        print(f"❌ Error creating wisdom directory: {e}")
        return None

    # Create category subdirectories
    for category in CATEGORIES:
        category_dir = wisdom_dir / category
        try:
            category_dir.mkdir(exist_ok=True)
            print(f"✅ Created category: {category}/")
        except Exception as e:
            print(f"❌ Error creating {category}/: {e}")
            return None

    # Create README in wisdom directory
    readme_path = wisdom_dir / "README.md"
    readme_content = f"""# Coding Wisdom Collection

Initialized: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Categories

- **development/** - Development principles and high-level approaches
- **debug/** - Debugging principles and systematic troubleshooting
- **trivial/** - Trivial but user-caring features and details
- **nonconsensus/** - Non-consensus tips and counter-intuitive practices

## File Format

Each wisdom item follows this naming convention:
`{{category}}/{{YYYY-MM-DD}}-{{slug}}.md`

Example: `development/2026-03-05-write-tests-after-implementation.md`

## Adding Wisdom

Use the capture script:
```bash
python3 scripts/capture_wisdom.py
```

Or manually create files following the template in `references/wisdom-template.md`.
"""

    try:
        readme_path.write_text(readme_content)
        print(f"✅ Created README.md")
    except Exception as e:
        print(f"❌ Error creating README.md: {e}")

    print(f"\n✅ Wisdom storage initialized at: {wisdom_dir}")
    print("\nNext steps:")
    print("1. Capture wisdom: python3 scripts/capture_wisdom.py")
    print("2. Search wisdom: python3 scripts/search_wisdom.py --summary")

    return wisdom_dir


def main():
    # Parse arguments
    path = "."
    if len(sys.argv) > 1:
        if sys.argv[1] == "--path" and len(sys.argv) > 2:
            path = sys.argv[2]
        elif sys.argv[1] in ["-h", "--help"]:
            print("Initialize wisdom storage structure for coding-wisdom skill.")
            print("\nUsage:")
            print("  python3 init_wisdom.py [--path <path>]")
            print("\nArguments:")
            print("  --path <path>  Base path for wisdom storage (default: current directory)")
            sys.exit(0)

    print("🚀 Initializing coding wisdom storage...")
    print()

    result = init_wisdom(path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
