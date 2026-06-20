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

Ice_1 = IceCreamStand("ICE QUEEN","icecream")
Ice_1.flavors_introduce()

# 9.7
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
Admin_1 = Admin('lili','yan','woman')
# Admin_1.show_privileges()
Admin_1.privileges.show_privileges()

# 9.9
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_rading = 0
        pass
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):
        print(f"thie car has {self.odometer_rading} miles on it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_rading:
            self.odometer_rading = mileage
        else:
            print(f"you can't roll back an odometer!")
        
    def increment_odometer(self,miles):
        self.odometer_rading +=miles
class Battery():
    def __init__(self,battery_size =40):
        self.battery_size = battery_size
        pass
    def decribe_battery(self):
        print(f"this car has a {self.battery_size}")
    def get_range(self):
        if self.battery_size ==40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"\nthis car can go about {range} miles on a full charge.")
    def upgrad_battery(self):
        if self.battery_size != 65:
            self.battery_size =65
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
ElectricCar_1 =  ElectricCar('china','tesla','2022')
ElectricCar_1.battery.get_range()
ElectricCar_1.battery.upgrad_battery()
ElectricCar_1.battery.get_range()