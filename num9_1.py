# 9.1 and 9.2
class Restaurant :
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        pass
    def describe_resturant(self):
        print(f"{self.restaurant_name} is a good restaurant,we have dishes of {self.cuisine_type} !")
    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open.")

restaurant_1 = Restaurant("mcdonlord","fastfood")
restaurant_2 = Restaurant("changlai","yue dishes")
restaurant_3 = Restaurant("KFC","Fried chickens")

print(f"{restaurant_1.restaurant_name} have dishes of {restaurant_1.cuisine_type}.")
print(f"{restaurant_2.restaurant_name} have dishes of {restaurant_2.cuisine_type}.")
print(f"{restaurant_3.restaurant_name} have dishes of {restaurant_3.cuisine_type}.")

restaurant_1.open_restaurant()
restaurant_1.describe_resturant()

restaurant_2.open_restaurant()
restaurant_2.describe_resturant()

restaurant_3.open_restaurant()
restaurant_3.describe_resturant()

# 9.3
class User:
    def __init__(self,first_name,last_name,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        pass
    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.sex}.")
    def greet_user(self):
        print(f"{self.first_name} {self.last_name} welcome!!")

User_1 = User('optimus','prime','male')
User_2 = User('bumble','bee','male')
User_3 = User("LILI",'YAN','female')

User_1.describe_user()
User_1.greet_user()

User_2.describe_user()
User_2.greet_user()
  
User_3.describe_user()
User_3.greet_user()  