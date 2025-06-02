"""
This script compares two lists of file paths:
1. A full list of file paths from the EDCI repository (`edc_file`)
2. A list of suffix-matching paths extracted from a comparison result (`matching_file`)

It identifies which paths in the EDCI repository are *not* found in the suffix-matching list
and prints those unmatched paths. The `matching_file` is expected to contain lines starting
with 'EDCI:' followed by the path of interest.
"""

from pathlib import Path

#brevapp_file = "edci-commons-brevApp.txt"
edc_file = "edci-commons-EDC.txt"
matching_file = "suffix-matching.txt"

with open(edc_file, "r", encoding="utf-8") as f:
    edc_paths = [line.strip() for line in f if line.strip()]

matching_paths = []
with open(matching_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("EDCI:"):
            path = line.split("EDCI:")[1].strip()
            matching_paths.append(path)

# Compute unmatched EDCI paths
unmatched = [path for path in edc_paths if path not in matching_paths]

# Print results
print("Paths in EDCI file that did NOT match:")
for path in unmatched:
    print(path)