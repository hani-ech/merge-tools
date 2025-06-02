"""
compare-structure.py

This script compares the **complete set of subdirectory paths** between two given directories.
It lists which subdirectories are:

- Only in the first directory (path_a)
- Only in the second directory (path_b)
- Present in both

Unlike recursive diff tools that inspect contents, this focuses purely on **directory structure**.

Useful during refactoring or merging of codebases to assess how folder structures differ
(e.g., between a legacy fork and an upstream update).

"""

import os
from pathlib import Path

def get_all_dirs(root):
    return set(str(p.relative_to(root)) for p in Path(root).rglob("*") if p.is_dir())

# Set your paths here
path_a = "/Users/haniehhabibi/Web2Learn/Projects/BrevApping/BrevApp"
path_b = "/Users/haniehhabibi/Web2Learn/Projects/BrevApping/european-digital-credentials"

dirs_a = get_all_dirs(path_a)
dirs_b = get_all_dirs(path_b)

only_in_a = dirs_a - dirs_b
only_in_b = dirs_b - dirs_a
in_both = dirs_a & dirs_b

print("\n📁 Only in BrevApp:")
for d in sorted(only_in_a):
    print(f"  {d}")

print("\n📁 Only in EDCI:")
for d in sorted(only_in_b):
    print(f"  {d}")

print("\n📁 In Both:")
for d in sorted(in_both):
    print(f"  {d}")
