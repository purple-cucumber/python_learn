from pathlib import Path
import json
num = input("what's your favourite num.")
path = Path('hw10_4/favourite_num.json')
content = json.dumps(num)
path.write_text(content)
fetch = path.read_text()
num = json.loads(fetch)
print(f"I know your favourite number! It's {num}.")