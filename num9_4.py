# 9.10被导入的模块里最好不要有直接执行的代码
from class_learn import Restaurant
resturant_1 = Restaurant('KFC','Fried Chickens')
resturant_1.describe_resturant()
# 9.11
from class_learn import Admin
Admin1 = Admin('lili','yan','female')
Admin1.privileges.show_privileges()