"""
compare-dirs.py

This script recursively compares the **subdirectory structure** of two given directories.
It prints a tree-style report showing which subdirectories are:

- ✅ Present in both directories
- 🟦 Present only in the first directory (dir1)
- 🟥 Present only in the second directory (dir2)

Key Features:
-------------
- Skips going deeper if a subdirectory is missing in one of the two paths
- Useful for detecting structural divergence before merging two similar projects
- Customizable by updating `dir1` and `dir2` paths to your local folder names

"""

import os
from pathlib import Path

# ✅ Make sure these are Path objects, not strings!
dir1 = Path("/Users/haniehhabibi/Web2Learn/Projects/BrevApping/BrevApp")
dir2 = Path("/Users/haniehhabibi/Web2Learn/Projects/BrevApping/european-digital-credentials")

# 🧾 Store output lines
output = []

def compare_subdirs(path1: Path, path2: Path, rel_path: Path = Path()):
    full_path1 = path1 / rel_path
    full_path2 = path2 / rel_path

    subdirs1 = {p.name for p in full_path1.iterdir() if p.is_dir()} if full_path1.exists() else set()
    subdirs2 = {p.name for p in full_path2.iterdir() if p.is_dir()} if full_path2.exists() else set()

    all_subdirs = sorted(subdirs1 | subdirs2)

    for subdir in all_subdirs:
        sub_path = rel_path / subdir

        if subdir in subdirs1 and subdir in subdirs2:
            output.append(f"✅ {sub_path}")
            compare_subdirs(path1, path2, sub_path)
        elif subdir in subdirs1:
            output.append(f"🟦 {sub_path} (only in BrevApp)")
        elif subdir in subdirs2:
            output.append(f"🟥 {sub_path} (only in EDCI)")

# 🔍 Run comparison
compare_subdirs(dir1, dir2)

# 🖨️ Print results
for line in output:
    print(line)
