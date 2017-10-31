#http://search.smzdm.com/?c=home&s=xps
import re
import requests
from bs4 import BeautifulSoup
import time
import urllib.request as ur  
import urllib.parse as up  
from http.cookiejar import CookieJar  
from urllib import parse

 
def main():
    tag = input('待搜索的关键词:')
    if tag != '':
        post_data = get_post_data() 
        opener = build_openner() 
        ur.install_opener(opener)
        url = 'http://search.smzdm.com/?c=home&s=xps'

        # 直接get无法获取js加载的信息
        # res = requests.get(url)
        # print(res.text)

        req = ur.Request(url,post_data,headers=hdr) #ur.Request(url, post_data, hdr)  
        res = ur.urlopen(req)
        res = res.read()
        #print(res.decode())
        analysisHtml(res.decode())
        # response = opener.open(req)  
        # page = response.read()  
        # print(page.decode('utf_8'))


    else:
        main()

def analysisHtml(html):
    pic_url = re.findall('"feed-row-wide"',html,re.S)
    soup = BeautifulSoup(html,'lxml')
    #print(soup.prettify())
    h5list = soup.find_all('h5')
    for h5 in h5list:
        print(h5.text)

    # taglist = soup.find_all('div', attrs={'class': re.compile("(z-feed-content)|()")})  
    # for trtag in taglist:  
    #     tdlist = trtag.find_all('h5')
    while True:
        time.sleep(1)
        
# post数据  
def get_post_data():  
    data = dict()  
    data['c'] = 'home'  
    data['s'] = 'xps'        
    return up.urlencode(data).encode('utf_8') 
     

# cookie上创建一个opener  
def build_openner():  
    cookie = CookieJar()  
    cookie_handler = ur.HTTPCookieProcessor(cookie)  
    opener = ur.build_opener(cookie_handler)  
    return opener  

hdr = {'Accept':'*/*',  
#'Accept-Encoding':'gzip, deflate', #对于某些页面压缩后会出现读取问题 
'Accept-Language':'zh-CN,zh;q=0.8',  
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',  
'X-Requested-With':'XMLHttpRequest'}  




if __name__ == '__main__':
    print("启动张大妈搜索器")
    main()