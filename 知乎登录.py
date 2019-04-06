# from selenium import webdriver
import requests

url = 'https://www.zhihu.com/'

headers = {
    'cookie': 'xxxxxxxxxxxxxxxxxxx d_c0="AACnMSPzWg6xxxxxxxxxxxxxxxxxxxxxxxYdKURQEOFFbffQZ3XiVxDw; z_c0="2|1:0|10xxxxxxxxxxxxxxxxxxxxxxi4xSmFTdUFnQUFBQUFBQUtjeElfTmFEaVlBQUFCZ0FsVk5zUVptWFFEeUIwZG9ZNlQxbXZseVlRNWpMTkg1WUVlX1FB|70d01bb5cf60a7586ec57564ac54d8fd46752e62d6222c35cbae1a8571949410"; tst=r; q_c1=bf4b8d4c93934a76a5492278be85301a|1551415475000|1551415475000; __utmv=51854390.100--|2=registration_date=20160227=1^3=entry_date=20160227=1; __utma=51854390.1547648715.1551415517.1551772098.1553946394.3; __utmz=51854390.1553946394.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wanfar/activities; tgw_l7_route=4860b599c6644634a0abcd4d10d37251',
    'user-agent': 'Mozilla/xxxxxxxxxxxxx0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chromxxxxxxxxxxx Safari/537.36'
}
session = requests.session()
source = session.get(url, headers=headers, verify=False).content.decode()
print(source)
