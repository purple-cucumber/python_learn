name = ['lili','jiji','haha']
print(f"我邀请{name[0]}、{name[1]}、{name[2]}来吃饭。")
name[2] = 'lulu'
print(f"我邀请{name[0]}、{name[1]}、{name[2]}来吃饭。")
print(len(name))
add_name = ['ada','like','earth']
name.extend(add_name)
print(name)
name.insert(1,'prime')
print(len(name
          ))
print(name)
print("删人吧")
for i in range(5):
    name_remove = name.pop()
    print(f"我很抱歉，你来不了了，{name_remove}.")
print(len(name))
print(f"欢迎{name}来我家")
del name[1]
del name[0]
print(name)