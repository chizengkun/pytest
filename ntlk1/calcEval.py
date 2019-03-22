#coding:utf-8
import jieba
import os
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

#reload(sys)

npath = os.getcwd()
filename = npath +'\\ntlk1\gg.txt'
print(filename)
gg = open(filename,'rb').read()
words = jieba.lcut( gg)
''' counts = {}
excludes = {" ", "我们","不是","两个","一个","如果","这个","那个"}
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
'''

imgfile = npath +'\\ntlk1\\1.jpg'
#使用词云显示
back_ground = imread(imgfile)
wc = WordCloud(background_color="white",max_words=1000, mask=back_ground, max_font_size=100,random_state=42, font_path="C:/Windows/Fonts/STFANGSO.ttf",)
wcword = ' '.join( words)
wc.generate( wcword)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_ground)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('19th.png')