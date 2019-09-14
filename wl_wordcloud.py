# from wordcloud import WordCloud
# import PIL.Image as image
# import numpy as np
#
# with open(r'D:\python\wl_bf', encoding='utf-8') as fp:
#     text = fp.read()
#     # print(text)
#     mask = np.array(image.open(r'D:\python\logo3.jpg'))
#     wordcloud = WordCloud(
#         background_color='white',
#         max_words=1000,  # 显示的词的最大个数
#         max_font_size=100,  # 显示字体最大的尺寸
#         random_state=30,  # 有多少种配色
#         mask=mask,
#         font_path='C:\Windows\Fonts\STZHONGS.TTF'
#     ).generate(text)
#     image_produce = wordcloud.to_image()
#     image_produce.show()
#

#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:wujf
@file: word.py
@time: 2018/09/14 10:05
必须要安装 matplotlib
"""
import os
import cv2
# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)
import jieba
from wordcloud import WordCloud

import matplotlib.pyplot as plt

with open(r"D:\python\wl_bf", 'r', encoding='utf-8') as f:
    text = f.read()

# str  = " ".join(jieba.cut(text))
# color_mask = cv2.imread('logo3.jpg')
# print(type(str))

font = r"C:\\Windows\\Fonts\\STXINWEI.TTF"     #这里一定要些win10电脑里面的中文字体，否则遇到中文字体分不出来
s = WordCloud(
        background_color='white',  # 设置背景颜色，与图片的背景色相关
        # mask=backgroud_Image,  # 设置背景图片
        font_path='C:\Windows\Fonts\STXINWEI.TTF',  # 显示中文，可以更换字体
        # max_words=1500,  # 设置最大显示的字数
        min_font_size=35, # 最小字号
        max_font_size=160,  # 设置字体最大值
        random_state=1,  # 设置有多少种随机生成状态，即有多少种配色方案
        width=1600,
        height=1000,
        # colormap = 'Blues'
  ).generate(text)
s.to_file("cloud.png")
plt.imshow(s)
plt.axis("off")
plt.show()


# from wordcloud import WordCloud
# import cv2
# import jieba
#
# with open('D:\\python\\wl_bf', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# cut_text = " ".join(jieba.cut(text))
#
# color_mask = cv2.imread('logo.jpg')
#
# cloud = WordCloud(
#     # 设置字体，不指定就会出现乱码
#     font_path=" C:\\Windows\\Fonts\\STKAITI.TTF",
#     # font_path=path.join(d,'simsun.ttc'),
#     # 设置背景色
#     background_color='black',
#     # 词云形状
#     mask=color_mask,
#     # 允许最大词汇
#     max_words=2000,
#     # 最大号字体
#     max_font_size=40
# )
#
# wCloud = cloud.generate(cut_text)
# wCloud.to_file('cloud.jpg')
#
# import matplotlib.pyplot as plt
#
# plt.imshow(wCloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

#
# from os import path
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
#
# from wordcloud import WordCloud, STOPWORDS
#
# d = path.dirname(__file__)
#
# # Read the whole text.
# text = open(path.join(d, 'wl_bf.txt')).read()
#
# # read the mask image
# # taken from
# # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
# alice_mask = np.array(Image.open(path.join(d, "logo.png")))
#
# stopwords = set(STOPWORDS)
# stopwords.add("said")
#
# wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
#                stopwords=stopwords)
# # generate word cloud
# wc.generate(text)
#
# # store to file
# wc.to_file(path.join(d, "alice.png"))
#
# # show
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.axis("off")
# plt.show()