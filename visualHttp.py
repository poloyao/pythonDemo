import urllib.request as ur
import urllib.parse as up
import re
from http.cookiejar import CookieJar
import time

def post_data():
    data = dict()
    name = input('name:')
    pws = input('password:')
    data['username'] = name
    data['password'] = pws
    post_data = up.urlencode(data).encode('utf_8')
    return post_data

def build_openner():
    cookie = CookieJar()
    cookie_handler = ur.HTTPCookieProcessor(cookie)
    opener = ur.build_opener(cookie_handler)
    return opener

def get_hdr():
    hdr = {'Accept':'*/*',  
    'Accept-Encoding':'gzip, deflate',  
    'Accept-Language':'zh-CN,zh;q=0.8',  
    #'Connection':'keep-alive',  
    #'Content-Length':'95',  
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  
    #'Host':'www.zhihu.com',  
    #'Origin':'http://www.zhihu.com',  
    #'RA-Sid':'DEADFC42-20150104-093648-9e5c2d-88ba9a',  
    #'Referer':'http://www.zhihu.com/',  
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',  
    'X-Requested-With':'XMLHttpRequest'}  
    return hdr


def main():
    data = post_data()
    hdr = get_hdr()
    opener = build_openner()
    ur.install_opener(opener)


    url = 'http://www.mtyypt.com/index/index/login.html'
    req = ur.Request(url,data,hdr)
    response = opener.open(req)  
    page = response.read()  
    pageIndex = page.decode('utf-8')
    if len(re.findall('index.html',pageIndex)) > 0:
        print('ok')
        print(pageIndex)
    else:
        print('login error')

    

if __name__ == '__main__':
    main()
    while True:
        if((input("是否退出 YES / NO:")).upper() == "YES"):
            break
