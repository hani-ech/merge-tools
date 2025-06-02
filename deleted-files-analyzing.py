"""
deleted-files-analyzing.py

This script parses a Git conflict summary (conflicts.txt) to extract and visualize cases where a file was
**deleted in the new branch but modified in HEAD** — typically resulting in a 'modify/delete' conflict.

It builds a **tree-like directory structure** from these paths to help developers quickly locate and understand
where such conflicts occurred in the project hierarchy.

Key Features:
-------------
- Parses lines matching the 'CONFLICT (modify/delete)' pattern
- Groups conflicts by folder using a nested dictionary
- Prints a visual tree of affected folders and files
- Highlights only files that were **deleted remotely but still modified locally**


"""

import re
from pathlib import Path
from collections import defaultdict

# Path to your conflicts.txt file
conflict_file_path = "conflicts.txt"  # Change if needed

# Regex pattern for modify/delete lines
pattern = re.compile(r"CONFLICT \(modify/delete\): (.+?) deleted in .* and modified in HEAD")

# Dictionary to store files grouped by folders
deleted_files_by_folder = defaultdict(list)

# Parse the conflict file
with open(conflict_file_path, "r", encoding="utf-8") as f:
    for line in f:
        match = pattern.match(line.strip())
        if match:
            full_path = Path(match.group(1))
            folder = full_path.parent
            filename = full_path.name
            deleted_files_by_folder[folder].append(filename)

# Build a tree structure
tree = {}

for folder, files in deleted_files_by_folder.items():
    parts = folder.parts
    current = tree
    for part in parts:
        current = current.setdefault(part, {})
    current["_files"] = files

# Recursive function to print the tree
def print_tree(tree, prefix=""):
    for idx, (key, value) in enumerate(sorted(tree.items())):
        if key == "_files":
            for f in value:
                print(f"{prefix}  └─ {f}")
            continue

        is_last = idx == len(tree) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{key}")
        extension = "    " if is_last else "│   "
        print_tree(value, prefix + extension)

# Print the final tree
print("📂 Conflict Tree (Deleted files still modified in HEAD)\n")
print_tree(tree)
