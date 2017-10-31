import re
import requests

def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0

    print('找到关键词:'+keyword+'的图片，现在开始下载图片...')
    print('预计下载数量：' + str(len(pic_url)))
    for each in pic_url:
        print('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            pic = requests.get(each,timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        imgPath = 'E:/ABC/' + keyword +'_' + str(i) + '.jpg'
        fp = open(imgPath,'wb')
        fp.write(pic.content)
        fp.close()
        i +=1
    print('全部下载完成')
    

if __name__ == '__main__':
    word = input('input:')
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text,word)
    
