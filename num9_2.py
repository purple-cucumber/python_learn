class Restaurant :
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        pass
    def describe_resturant(self):
        print(f"{self.restaurant_name} is a good restaurant,we have dishes of {self.cuisine_type} !")
    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open.")
    def show_num(self):
        print(f"{self.number_served} people have eaten in the restaurant.")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,number):
        self.number_served += number

restaurant_1 = Restaurant("mcdonlord","fastfood")
restaurant_1.show_num()
restaurant_1.set_number_served(15)
restaurant_1.show_num()
restaurant_1.increment_number_served(32)
restaurant_1.show_num()
# 9.5
class User:
    def __init__(self,first_name,last_name,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.login_attempts = 0
        pass
    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.sex}.")
    def greet_user(self):
        print(f"{self.first_name} {self.last_name} welcome!!")
    def reset_login_attempts(self):
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts += 1

User_1 = User('lili','yan','female')
print(f"{User_1.login_attempts}")
User_1.increment_login_attempts()

print(f"{User_1.login_attempts}")
User_1.increment_login_attempts()
print(f"{User_1.login_attempts}")
User_1.increment_login_attempts()
User_1.reset_login_attempts()
print(f"{User_1.login_attempts}")