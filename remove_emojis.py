"""
Emoji & Symbol Remover for Project Files
==========================================
Removes all emojis, decorative Unicode symbols, and box-drawing
characters from .py, .md, and .txt files. Also cleans up leftover
whitespace from the removal.

Usage (Windows):
    py remove_emojis.py

Usage (macOS/Linux):
    python remove_emojis.py

Run from the root of each project repo.
"""

import os
import re

# Comprehensive pattern matching emojis, symbols, and box-drawing characters
EMOJI_AND_SYMBOLS = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # All emoji blocks (faces, animals, objects, etc.)
    "\U0001FA00-\U0001FAFF"  # Extended symbols and pictographs
    "\U00002600-\U000026FF"  # Misc symbols (sun, star, lightning, etc.)
    "\U00002700-\U000027BF"  # Dingbats (checkmarks, arrows, etc.)
    "\U00002500-\U0000257F"  # Box-drawing characters (lines, corners)
    "\U00002580-\U0000259F"  # Block elements
    "\U0000FE00-\U0000FE0F"  # Variation selectors
    "\U0000200D"             # Zero-width joiner (used in compound emojis)
    "\U000E0020-\U000E007F"  # Tags
    "]+"
)

# File extensions to process
EXTENSIONS = ('.py', '.md', '.txt')

# Directories to skip
SKIP_DIRS = {'.git', 'venv', 'env', '.venv', '__pycache__', 'node_modules', '.idea', '.vscode'}


def clean_line(line):
    """
    Remove emojis/symbols from a line and clean up leftover whitespace.

    Handles these cases:
        "  ## Features"      -> "## Features"         (emoji at start)
        "  Results:"         -> "  Results:"           (emoji before word)
        "Built with Python " -> "Built with Python"    (emoji at end)
        "print(f\"  Temp:\")"-> "print(f\"  Temp:\")"  (emoji inside strings)
    """
    # Replace emoji/symbol + surrounding spaces with a single space
    cleaned = EMOJI_AND_SYMBOLS.sub(' ', line)

    # Collapse multiple spaces into one (but preserve leading indentation intent)
    # First, record leading whitespace
    stripped = cleaned.lstrip(' ')
    leading_spaces = len(cleaned) - len(stripped)

    # Collapse multiple spaces in the content portion
    stripped = re.sub(r'  +', ' ', stripped)

    # Remove trailing whitespace
    stripped = stripped.rstrip()

    # Reconstruct with original indentation level (but cleaned)
    if leading_spaces > 0:
        # Normalize leading spaces: keep them but collapse if emoji removal created extras
        original_leading = len(line) - len(line.lstrip(' '))
        # Use the smaller of original or current leading spaces
        final_leading = min(original_leading, leading_spaces)
        result = ' ' * final_leading + stripped
    else:
        result = stripped

    # Preserve the original line ending
    if line.endswith('\r\n'):
        return result + '\r\n'
    elif line.endswith('\n'):
        return result + '\n'
    elif line.endswith('\r'):
        return result + '\r'
    return result


def process_file(filepath):
    """
    Remove emojis and clean whitespace from a single file.

    Returns True if the file was modified, False otherwise.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_lines = f.readlines()
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"  SKIP: {filepath} ({e})")
        return False

    cleaned_lines = [clean_line(line) for line in original_lines]

    # Check if anything changed
    if cleaned_lines == original_lines:
        return False

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
        return True
    except PermissionError as e:
        print(f"  ERROR: Cannot write {filepath} ({e})")
        return False


def main():
    """Walk through all project files and remove emojis/symbols."""
    print()
    print("=" * 50)
    print("  Emoji & Symbol Remover")
    print("=" * 50)
    print()

    modified_count = 0
    scanned_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk('.'):
        # Skip hidden and unnecessary directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for filename in files:
            if filename == 'remove_emojis.py':
                continue  # Don't process this script itself

            if filename.endswith(EXTENSIONS):
                filepath = os.path.join(root, filename)
                scanned_count += 1

                if process_file(filepath):
                    modified_count += 1
                    print(f"  CLEANED: {filepath}")
                else:
                    skipped_count += 1

    print()
    print("-" * 50)
    print(f"  Scanned:    {scanned_count} files")
    print(f"  Cleaned:    {modified_count} files")
    print(f"  Unchanged:  {skipped_count} files")
    print("-" * 50)
    print()

    if modified_count > 0:
        print("  Done! All emojis and symbols removed.")
    else:
        print("  No emojis or symbols found. Files are already clean.")
    print()


if __name__ == "__main__":
    main()