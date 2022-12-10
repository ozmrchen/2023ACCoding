from glob import glob

full_text = ""

files = glob("*.md")
for file in files:
    full_text += f"# {file}\n\n"
    text = open(file, "r").read()
    full_text += text
    full_text += "\n\n"

print(full_text)

with open("2022-12-12 Combined Daily Notes.md", "w") as FILE:
    FILE.write(full_text)
    