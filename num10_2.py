from pathlib import Path
# 去掉开头/
path = Path('hw10_2/guset.txt')
name = input("请输入名字。")
path.write_text(name)
print("请多写一点")
path = Path('hw10_2/guest_book.txt')
contents = ''
while 1:
    name = input("继续输入")
    contents += f"{name}\n"
    path.write_text(contents)