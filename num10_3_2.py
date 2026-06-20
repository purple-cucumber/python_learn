# 10.8无法读取不存在的文件，读才是存在错误的指令
from pathlib import Path
try:
    path_1 = Path('hw10_3\cat.txt')
    path_2 = Path('hw10_3\dog.txt')
    contents_1 = path_1.read_text()
    contents_2 = path_2.read_text()
except FileNotFoundError:
    pass
else:
    
    print(contents_1)
    contents_2 = path_2.read_text()
    print(contents_2)

