import re

with open("kama.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"\b(\w)|(\w)\b"

matches = re.findall(pattern, text)

letters = [m[0] if m[0] else m[1] for m in matches]

print(" ".join(letters))
