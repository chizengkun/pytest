#encoding: utf-8 

import jieba
import pkuseg
import sys
import os
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

#reload(sys)
#sys.setdefaultencoding("utf-8")
excludes = {"将军","却说","荆州","二人","不可","不能",
            "如此","商议","如何","左右","军马","军士",
            "引兵","次日"}

def getTop( words):
     counts = {}
     for word in words:
          if len(word) ==1:
               continue

          counts[word] = counts.get(word, 0) +1
          if word in excludes:
               del counts[word]

     items = list(counts.items())
     items.sort(key=lambda x:x[1], reverse=True)
     return items

def ShowImgHotWord(items, maxwords):
     
     npath = os.getcwd()
     imgfile = npath +'\\ntlk1\\cloud.jpg'
     back_ground = imread(imgfile)
     wc = WordCloud(background_color="white",max_words=maxwords, mask=back_ground, max_font_size=100,random_state=42, font_path="C:/Windows/Fonts/STZHONGS.ttf",)
     #print(items)
     wcword = ' '.join( items)
     wc.generate_from_text( wcword)
# 基于彩色图像生成相应彩色
     image_colors = ImageColorGenerator(back_ground)
     wc.recolor( color_func=image_colors)
# 显示图片
     plt.imshow(wc)
# 关闭坐标轴
     plt.axis('off')
     plt.show()
# 绘制词云
#     plt.figure()
#     plt.imshow(wc.recolor(color_func=image_colors))
#     plt.axis('off')
# 保存图片
     wc.to_file('123.png')

def printTop(items, icount):
     #取icount的热词
     words = []
     for i in range(icount):
          word, count = items[i]
          print("{0:<10}{1:>5}".format(word, count))

def calcTop50():
     npath = os.getcwd()
     filename = npath +'\\ntlk1\\area1.txt'
     txt = open(filename, encoding="utf-8").read()
     seg = pkuseg.pkuseg()
     
     #ctxt = jieba.lcut(txt)
     ctxt = seg.cut( txt)
     items = getTop( ctxt)
     #printTop(items, 50)
     ShowImgHotWord( ctxt, 50)

if __name__ == '__main__':
     calcTop50()
     #pkuseg.test('threekingdoms.txt', 'output.txt')
     #txt = open("output.txt", "rb").read()
     #print(txt)