from pathlib import Path
import json
path  = Path('hw10_4/favourite_num.json')
if path.exists():
    content  = path.read_text()
    num = json.loads(content)
    print(f"I know ypur favourite number! It's {num}")
else:
    num  = input("What's your favourite number?")
    content = json.dumps(num)
    path.write_text(content)
    print(f"{num} has been loaded.")