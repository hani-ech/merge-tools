from pathlib import Path

#root_dir = Path("/Users/haniehhabibi/Web2Learn/Projects/BrevApping/european-digital-credentials/edci-commons")
root_dir = Path("/Users/haniehhabibi/Web2Learn/Projects/BrevApping/BrevApp/edci-commons")


for file in root_dir.rglob("*"):
    if file.is_file() and file.name != ".DS_Store":
        relative_path = file.relative_to(root_dir)
        print(relative_path.as_posix())