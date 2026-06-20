# 10.1
from pathlib import Path

path  = Path('learning_python.txt')
contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines()
for v in lines:
    print(v)

# 10.2 replace 不会修改而是返回 10.3

for v in lines:
    v = v.replace('Python','C')
    print(v)

for i in contents.splitlines():
    print(i)
# 10.3
