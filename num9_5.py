from random import *
class Die():
    def __init__(self,sides=6):
        self.sides = sides
        pass
    def roll_die(self):
        num = randint(1,self.sides)
        return num
side_6 = Die()
# for v in range(10):
#     print(side_6.roll_die())
# side_10 = Die(10)
# for v in range(10):
#     print(side_10.roll_die())

data = ['lili','prime','qiqi','mega','sudo',4,5,6,7,8,12,3,1,11,22]
print("if there are this information on the checklist you will win the prize!!")
for v in range(4):
    key = choice(data)
    print(f"{key}")
print("please check!")

my_ticket = [1,2,3,4,11,22,33,44,78,9,12,33,41]
prize_num = 2
time = 1
your_num = choice(my_ticket)
while your_num != prize_num:
    print(f"I got the {your_num},the times are {time}")
    your_num = choice(my_ticket)
    time += 1
print(f"the times are {time}")
