"""
This script performs a suffix-based comparison of file paths from two repositories stored in two different txt files.
It compares the paths by checking if one is a suffix of the other, meaning their trailing
directories and filenames match (even if the root paths differ). This is useful for identifying
shared file structure or common files across two differently organized projects.

The script prints all matching pairs of paths where the suffix of one matches the other.
"""

from pathlib import Path

# Load and normalize paths from two files
def load_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [Path(line.strip()) for line in f if line.strip()]

# Convert a Path to a list of parts (e.g., folders and filename)
def path_parts(path):
    return path.parts

# Check if one path is a suffix of another
def is_suffix_match(parts1, parts2):
    min_len = min(len(parts1), len(parts2))
    return parts1[-min_len:] == parts2[-min_len:]

# Load both path lists
file1 = "edci-viewer-brevApp.txt"
file2 = "edci-viewer-EDC.txt"

paths1 = load_paths(file1)
paths2 = load_paths(file2)

# Compare suffixes and store matches
matches = []

for p1 in paths1:
    for p2 in paths2:
        if is_suffix_match(path_parts(p1), path_parts(p2)):
            matches.append((str(p1), str(p2)))

# Print the matches
print("🎯 Matching Paths (Suffix-Based):\n")
for left, right in matches:
    print(f"BrevApp: {left}\n   EDCI: {right}\n")
