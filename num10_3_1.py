# 10.6
from pathlib import Path

def Integer_trans(num_1,num_2):
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        print("输入的不是数字哦~")
    else:
        print(f"{num_1} and {num_2}")

# num_1 = input("请输入第一个数")
# num_2 = input("请输入第二个数")
# Integer_trans(num_1,num_2)
# 10.2
while True:
    num_1 = input("请输入第一个数")
    num_2 = input("请输入第二个数")
    Integer_trans(num_1,num_2)