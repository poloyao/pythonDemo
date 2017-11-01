import re
import requests
from bs4 import BeautifulSoup
import time
import urllib.request as ur  
import urllib.parse as up  

 
def main():
    tag = 'xps'#input('待搜索的关键词:')
    if tag != '':
        post_data = get_post_data() 
        url = 'http://search.smzdm.com/?c=home&s=xps&order=score&mall_id=41'

        # 直接get无法获取js加载的信息
        # res = requests.get(url)
        # print(res.text)

        req = ur.Request(url,post_data,headers=hdr) #ur.Request(url, post_data, hdr)  
        res = ur.urlopen(req)
        res = res.read()
        analysisHtml(res.decode())
    else:
        main()

def analysisHtml(html):
    pic_url = re.findall('"feed-row-wide"',html,re.S)
    soup = BeautifulSoup(html,'lxml')
    #print(soup.prettify())
    h5list = soup.find_all('h5')
    queryList = list()
    for h5 in h5list:
        data = MyData(h5.text)
        if h5.text.split('\n\n').__len__() > 0:
            data.name = h5.text.split('\n\n')[0].strip()
        if h5.find_all('div').__len__() > 0:
            data.value = h5.find_all('div')[0].text
        # 没抓日期
        queryList.append(data)
    for queryIndex in range(queryList.__len__()):
        print(queryList[queryIndex].ShowItem())

class MyData:
    def __init__(self,a_name = None,a_value = None,a_date = None):
        self.name = a_name
        self.value = a_value
        self.date = a_date
    
    def ShowItem(self):
        showtext = ''
        if 'None' != str(self.name).strip(): 
            showtext = "描述:" + self.name 
            showtext += '\n\n'
        if 'None' != str(self.value).strip(): 
            showtext += "价值:" + self.value 
            showtext += '\n\n'
        if 'None' != str(self.date).strip(): 
            showtext += "发布日期:" + self.date 
        showtext += '----------------------------------------------'
        return showtext

        
# post数据  
def get_post_data():  
    data = dict()  
    data['c'] = 'home'  
    data['s'] = 'xps'        
    return up.urlencode(data).encode('utf_8') 
     

hdr = {'Accept':'*/*',  
#'Accept-Encoding':'gzip, deflate', #对于某些页面压缩后会出现读取问题 
'Accept-Language':'zh-CN,zh;q=0.8',  
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',  
'X-Requested-With':'XMLHttpRequest'}  




if __name__ == '__main__':
    print("启动张大妈搜索器")
    main()

