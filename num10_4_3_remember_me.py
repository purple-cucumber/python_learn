from pathlib import Path
import json
def get_stored_user_data(path,name):
    if path.exists():
        fetch = path.read_text()
        content = json.loads(fetch)
        if content['name'] == name:
            return content
        else:
            return None
    else:
        return None
def get_new_user_data(path):
    name = input("what is your name?")
    sex = input("what is your sex?")
    hobby = input("what is your hobby?")
    content = {'name':name,'sex':sex,'hobby':hobby}
    go = json.dumps(content)
    path.write_text(go)
    return content
def greeting_user():
    path = Path('hw10_4/user_data.json')
    name_in = input("what is your name?")
    user = get_stored_user_data(path,name_in)
    if user :
        print(f"{user['name']},welcome come back!!")
    else:
        user = get_new_user_data(path)
        print(f"thank you!{user['name']}!")
greeting_user()