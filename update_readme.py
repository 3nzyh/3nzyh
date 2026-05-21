import os
import re
import requests

USER = "3nzyh"
README = "README.md"

resp = requests.get(f"https://api.github.com/users/{USER}", timeout=30)
resp.raise_for_status()
data = resp.json()

count = data["public_repos"]
text = open(README, "r", encoding="utf-8").read()
text = text.replace("__PROJECT_COUNT__", f"{count}")
text = re.sub(r'projects\s+\d+', f"projects {count}", text, flags=re.I)

with open(README, "w", encoding="utf-8") as f:
    f.write(text)
