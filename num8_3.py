# 8.6
# def city_country(city,country):
#     la = f'{city},{country}'
#     return la
# data = city_country('santiago','chile')
# print(f"'{data}'")
# 8.7
def make_album(singer,album):
    music = {singer:album}
    return music
# music_1 = make_album('lili','sing a song')
# music_2 = make_album('shya','hululu')
# music_3 = make_album('vsinger','vex')
# print(music_1)
# print(music_2)
# print(music_3)
# 8.8
while True:
    print("\n我们需要你的歌手和专辑")
    singer = input("歌手是？")
    album = input("专辑？")
    if singer == 'quit':
        break
    if album == 'quit':
        break
    data = make_album(singer,album)
    print(data)