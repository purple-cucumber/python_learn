# user = ['admin','optimus','megatron','hot rod','soundwave']
# name = 'jazz'
# if name in user:
#     print("Hello admin,would you like to see a status report")
# else :
#     print(f"{name},Thank you for logging in again.")
# user = []
# name = 'jazz'
# if user:
#     print(f"{name},Thank you for logging in again.")
# else:
#     print("we need to find some users")
#5.10
# user = ['Admin','optimus','megatron','hot rod','soundwave']
# current_user = user[:]
# user_need = ['admin','OPTIMUS','lili','starscream','prowl']
# list_upper = []
# list_lower = []
# for i in range(5):
#     list_upper.append(user[i].upper())
#     list_lower.append(user[i].lower())
# for name in user_need:
#     if name in user:
#         print("需要输入别的用户名")
#     elif name in list_lower:
#         print("需要输入别的用户名")
#     elif name in list_upper:
#          print("需要输入别的用户名")
#     else:
#         print(f"{name}这个名字没有被使用")
#5.11
num = list(range(1,10))
print(num)
for i in num:
    if i ==1:
        print(f"{i}st")
    elif i==2 or i ==3 :
        print(f"{i}nd")
    else :
        print(f"{i}th")