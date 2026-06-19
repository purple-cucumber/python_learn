# 7.8
# sandwich_order = ['番茄三明治','香肠三明治','金枪鱼三明治']
# finished_sanwich = []
# while sandwich_order:
#     sandwich = sandwich_order.pop()
#     print(f'我做了你的{sandwich}')
#     finished_sanwich.append(sandwich)
# print("---finish---")
# for v in finished_sanwich:
#     print(f"{v}")
# 7.9
# sandwich_order = ['番茄三明治','烟熏肉三明治','烟熏肉三明治','香肠三明治','金枪鱼三明治','烟熏肉三明治']
# print("烟熏肉三明治卖完了desu")
# finished_sanwich = []
# while '烟熏肉三明治' in sandwich_order:
#     sandwich_order.remove('烟熏肉三明治')
# print(sandwich_order)
# 7.10
active = True
search = {}
while active:
    name = input("who are you?")
    place = input("where would you go?")
    search[name] = place
    yes_or_no = input("if sb want to tell about yourselves?")
    if yes_or_no == 'no':
        active = False
print("--------finish---------")
for k, v in search.items():
    print(f"\n{k} would like to go to {v}.")