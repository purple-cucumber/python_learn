from textblob import TextBlob

with open ('pride_prejudice.txt',encoding='utf8') as f:
    file_content = f.read()

# 2. 清理元数据，只保留正文
start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK 1342 ***"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK 1342 ***"
clean_text = file_content.split(start_marker)[1].split(end_marker)[0].strip()

book_pride = TextBlob(clean_text)
positive_sentence = []
negative_sentence = []

for i in book_pride.sentences:
    ##这个错误是因为 book_pride.sentences 是 TextBlob 对象的属性
    if i.sentiment.polarity > 0.9:
        positive_sentence.append(i)
    if i.sentiment.polarity < -0.9 :
        negative_sentence.append(i)
print("\n"+" The " + str(len(positive_sentence)) + " positive sentences are")
for i in positive_sentence:
    print("+ " + str(i.replace("\n", "").replace("      ", " ")))
print("\n"+"The " + str(len(negative_sentence)) + " negative sentences are")
for i in negative_sentence:
    print("- " + str(i.replace("\n", "").replace("      ", " ")))