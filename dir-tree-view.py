"""
compare-tree-structure.py

This script compares the **directory trees** of two project folders and prints them **side by side** for easy visual inspection.
It provides a tree-like structure of each directory and highlights any structural divergence clearly and cleanly.

How to Use:
-----------
1. Set `dir1` and `dir2` to the paths you want to compare.
2. Adjust `exclude_dirs` if needed to ignore additional directories.
3. Run the script — you’ll see a visual diff of both structures printed to the console.

"""

import os
from pathlib import Path
from itertools import zip_longest

# Folders to exclude from both trees
exclude_dirs = {"docker_issuer", "docker_viewer", "docker_wallet", ".git"}

def get_dir_tree_lines(base_path, prefix=""):
    lines = []
    base_path = Path(base_path)
    subdirs = [p for p in sorted(base_path.iterdir()) if p.is_dir() and p.name not in exclude_dirs]
    total = len(subdirs)

    for i, subdir in enumerate(subdirs):
        connector = "└── " if i == total - 1 else "├── "
        line = prefix + connector + subdir.name
        lines.append(line)

        next_prefix = prefix + ("    " if i == total - 1 else "│   ")
        lines.extend(get_dir_tree_lines(subdir, next_prefix))
    return lines

# ✏️ Set your two base directories here
dir1 = "/Users/haniehhabibi/Web2Learn/Projects/BrevApping/BrevApp"
dir2 = "/Users/haniehhabibi/Web2Learn/Projects/BrevApping/european-digital-credentials"

tree1 = get_dir_tree_lines(dir1)
tree2 = get_dir_tree_lines(dir2)

# Side-by-side output
print(f"{'📁 BrevApp':<80} | 📁 EDCI")
print("=" * 160)
for left, right in zip_longest(tree1, tree2, fillvalue=""):
    print(f"{left:<80} | {right}")
