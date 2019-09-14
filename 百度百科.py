import urllib
import requests
from lxml import etree

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
}
query_word = input('请输入查询关键词：')
name = urllib.parse.quote(query_word)
url = 'http://baike.baidu.com/search/word?word=' + name
htmlx = requests.get(url, headers=headers).content.decode('utf-8')
html = etree.HTML(htmlx)
block = html.xpath('/html/body/div[@class="body-wrapper"]/div[@class="content-wrapper"]')[0]
info = block.xpath('//div[@class="content"]/div[@class="main-content"]/div[@class="lemma-summary"]/div[@class="para"]')
for i in info:
    info0 = i.xpath('string(.)')
    print(info0)