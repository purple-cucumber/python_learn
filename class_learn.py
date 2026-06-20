from class_learn_copy import User
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
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Strawberry','Chocolate','banana','Matcha']
    def flavors_introduce(self):
        for v in self.flavors:
            print(f'{v}')

class Admin(User):
    def __init__(self, first_name, last_name, sex):
        super().__init__(first_name, last_name, sex)
        # self.privileges = ['can add post','can delete post','can ban user']
        self.privileges = Privileges()
    # def show_privileges(self):
    #     for v in self.privileges:
    #         print(f'{v}')
            
class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
        pass
    def show_privileges(self):
        for v in self.privileges:
            print(f'{v}')