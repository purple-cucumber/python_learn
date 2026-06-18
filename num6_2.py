#6.4
# data = {'for' : 'foryun','if':'条件','[]':'列表'}
# for k,v in data.items():
#     print(f"{k} is {v}")
# data['>'] = '大于'
# data['<'] = '小于'
# for k,v in data.items():
#     print(f"{k} is {v}")
# 6.5
# rivers = {'egypt': 'nile','china':'changjiang','america':'yamaxun'}
# for k,v in rivers.items():
#     print(f"The {v} runs through {k}")
# for k in rivers.keys():
#     print(k)
# for v in rivers.values():
# #     print(v)
# user_0 = {'username' : 'efermi','first':'enrico','last':'fermi'}
# name = ['lili','optimus','efermi']
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

names = ['john', 'jen', 'phil', 'alice', 'eric']
for name in names:
    if name in favorite_languages.keys():
        print("thanks")
    else:
        print("i invite you to take a visit.")
