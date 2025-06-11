"""

This script recursively lists the **relative paths of all files** under a given root directory.

- Useful for:
  - Comparing file structures between projects
  - Creating file lists for further analysis or matching
"""

from pathlib import Path

#EDC
root_dir = Path("/Users/haniehhabibi/Web2Learn/Projects/BrevApping/european-digital-credentials/edci-viewer")

#BrevApp
#root_dir = Path("/Users/haniehhabibi/Web2Learn/Projects/BrevApping/BrevApp/edci-viewer")

for file in root_dir.rglob("*"):
    if file.is_file() and file.name != ".DS_Store":
        relative_path = file.relative_to(root_dir)
        print(relative_path.as_posix())