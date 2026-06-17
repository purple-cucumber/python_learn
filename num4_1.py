my_pizza = ['香肠披萨','至尊披萨','水果披萨']
for eat in my_pizza:
    print(f"我喜欢{eat}。")
print("我真的喜欢披萨！")
friend_pizza = my_pizza[:]#复制列表
my_pizza.append('和牛披萨')
friend_pizza.append('金枪鱼披萨')
for eat in my_pizza:
    print(f"我喜欢{eat}。")
print("我真的喜欢披萨！")
for eat in friend_pizza:
    print(f"朋友喜欢{eat}。")
print("朋友真的喜欢披萨！")

pet = ['dog','cat','mouse']
for great in pet :
    print(f"A {great} would make a great pet.")
print("any of these animals would make a great animals.")