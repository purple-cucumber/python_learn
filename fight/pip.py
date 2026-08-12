import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
response = requests.get(url)
response.encoding = 'utf-8'   # 确保以UTF-8读取

with open("pride_prejudice.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("下载完成，已保存为 pride_prejudice.txt")