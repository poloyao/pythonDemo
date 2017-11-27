import re
import requests
from bs4 import BeautifulSoup
import time
import urllib.request as ur  
import urllib.parse as up  



#https://dbd.jd.com/auctionList.html?searchParam=lego&enc=utf-8


def main():
    tag = '16941158'#input('夺宝岛id：\n')

    url = 'https://dbd.jd.com/auctionList.html?searchParam=lego&enc=utf-8'
    #result = requests.get(url)
    req = ur.Request(url)
    res = ur.urlopen(req)
    res = res.read()
    resed = res.decode()
    #pic_url = re.findall('red font24',resed,re.S)
    soup = BeautifulSoup(resed,'lxml')
    content = soup.find_all(id = 'auction3dangqianjia')
    ee = 1


if __name__ == '__main__':
    main()