import requests,time,random

k = 1
for i in range(100):
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&word=%E5%AF%8C'
    html = requests.get(url)
    html.encoding = 'utf-8'
    for j in range(30):
        img_url = html.json()['data'][j]['middleURL']
        data = requests.get(img_url).content
        with open('') as f:
            f.write(data)
        k += 1
        time.sleep(random.random())