import jieba

excludes = {"  ", "就是","不是","两个","一个","如果","这个","那个"}
jpm = open('water.txt','rb').read()
#jieba.enable_parallel(4)
words = jieba.lcut(jpm)
counts = {}

for word in words:
    if len(word) ==1:
        continue

    counts[word] = counts.get(word, 0) +1
    if word in excludes:
        del counts[word]

items = list(counts.items())

items.sort(key=lambda x:x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))