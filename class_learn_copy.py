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