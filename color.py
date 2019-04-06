import requests
import re
import os

url = 'https://www.114la.com/other/rgb.htm'
source = requests.get(url).content.decode('gbk')

color_block = re.search(' <table width="550" cellspacing="3">(.*?)  <script language="JavaScript" ', source, re.S).group(1)
color_list = re.findall('bgcolor="(.*?)"', color_block, re.S)
print(color_list)
color_str = ''.join(color_list)
os.makedirs('微微一笑很倾城', exist_ok=True)
# 如果没有微微一笑文件夹，就创建一个，如果有，则什么都不做"
color = 'sehao'
with open(os.path.join('微微一笑很倾城', color + '.txt'), 'w', encoding='utf-8') as f:
    f.write(color_str)

