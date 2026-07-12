class Employee():
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        pass
    def give_raise(self,salary_add = 5000):
        self.salary += salary_add