# 8.12
def sanwiches_make(*Ingredients):
    for v in Ingredients:
        print(f"I will make {v} sanwich.")
sanwiches_make("Sausage","cheese")
sanwiches_make("Wagyu")
sanwiches_make("Tuna")
# 8.13
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Zining','Zhang',
                             location = 'Guangzhou',
                             field = 'Computer',
                             hobby = 'drawing')
print(user_profile)

def make_car(Brand,Appearance,**data):
    data['Brand'] = Brand
    data['Appearance'] = Appearance
    return data
car = make_car('subaru', 'outback' , color = 'blue',tow_package = True)
print(car)

