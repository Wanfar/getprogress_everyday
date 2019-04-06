# from selenium import webdriver
import requests

url = 'https://www.zhihu.com/'

headers = {
    'cookie': '_zap=b006cab1-4209-44fa-a736-889cd8cc963e; d_c0="AACnMSPzWg6PTuVSGJr24BuH_wBROtDcvTY=|1539401703"; _xsrf=wEM2xqnOnDYdKURQEOFFbffQZ3XiVxDw; z_c0="2|1:0|10:1551415473|4:z_c0|92:Mi4xSmFTdUFnQUFBQUFBQUtjeElfTmFEaVlBQUFCZ0FsVk5zUVptWFFEeUIwZG9ZNlQxbXZseVlRNWpMTkg1WUVlX1FB|70d01bb5cf60a7586ec57564ac54d8fd46752e62d6222c35cbae1a8571949410"; tst=r; q_c1=bf4b8d4c93934a76a5492278be85301a|1551415475000|1551415475000; __utmv=51854390.100--|2=registration_date=20160227=1^3=entry_date=20160227=1; __utma=51854390.1547648715.1551415517.1551772098.1553946394.3; __utmz=51854390.1553946394.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wanfar/activities; tgw_l7_route=4860b599c6644634a0abcd4d10d37251',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
session = requests.session()
source = session.get(url, headers=headers, verify=False).content.decode()
print(source)
