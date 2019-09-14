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
# 可添加不可直接返回结果的词,对应该词条在百度的编号
change_word_list = {'富贵竹':'348172', '虞美人':'6043','常青藤':'24431'}

def input_word(query_word):  # 构建url
    name = urllib.parse.quote(query_word)
    if query_word in change_word_list.keys():
        url = 'https://baike.baidu.com/item/'+name+'/'+change_word_list[query_word]
    else:
        url = 'http://baike.baidu.com/search/word?word=' + name
    return url

def get_and_extract(url):
    htmlx = requests.get(url, headers=headers).content.decode('utf-8')
    html = etree.HTML(htmlx)
    block = html.xpath('/html/body/div[@class="body-wrapper"]/div[@class="content-wrapper"]')[0]
    info = block.xpath('//div[@class="content"]/div[@class="main-content"]/div[@class="lemma-summary"]/div[@class="para"]')
    for i in info:
        info0 = i.xpath('string(.)')
        print(info0)

def go():
    query_word = input('请输入查询关键词：')
    url = input_word(query_word)
    get_and_extract(url)

if __name__ == '__main__':
    go()