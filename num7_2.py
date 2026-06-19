# 7.4
# data = ''
# while data != 'quit':
#     data = input("please input your food")
#     print(data)
# 7.5
# user = ''
# while 1:
#     user = input("how old are you?")
#     user = int(user)
#     if user < 3:
#         print("it's free")
#     elif user < 12:
#         print("need 10 yuan")
#     else:
#         print("need 15 yuan")
#7.6
user = ''
active = True
while active:
    user = input("how old are you?")
    if user == 'quit':
        break
    user = int(user)
    if user < 3:
        print("it's free")
    elif user < 12:
        print("need 10 yuan")
    elif user == 32:
        print("happy 32!!")
        active = False
    else:
        print("need 15 yuan")
# 7.7
while 1:
    print("mop 99")