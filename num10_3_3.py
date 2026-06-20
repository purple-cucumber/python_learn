from pathlib import Path
path = Path('hw10_3/book.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print("没有找到哦")
else:
    lines = contents.splitlines()
    words = 0
    words_the = 0
    for v in range(len(lines)):
        lines[v] = lines[v].lower()
        n = lines[v].count('the')
        m = lines[v].count('the ')
        print(f"the line has {n} 'the' words and {m} 'the ' words")
        words += n
        words_the += m 
    print(f"the text has {words} words,and {words_the} words")   
        