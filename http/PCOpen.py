#encoding:UTF-8

import requests
import datetime
import time
import sys

print('正在开机准备中，请勿关闭此界面')
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('系统当前时间为：' + now)
sckey = 'SCU19816T653afd50681bb2bd5cbd74082c7066a85a544fb059beb'
#判断是否为打卡期间 则提示打卡
timeTempMin = '073000'
timeTempMax = '085000'
timeMark = datetime.datetime.now().strftime('%H%M%S')
if timeTempMax > timeMark > timeTempMin:
    print('提示打卡:已到打卡时间，请确认是否已经打卡成功')
    postdata = {"text":"已到打卡时间，请确认是否已经打卡成功","desp":now}
    r = requests.post("https://sc.ftqq.com/" + sckey +".send",data=postdata)
    if eval(r.text)['errmsg'] == 'success':
        print('完成推送')
    else:
        print('推送失败！！！')
    time.sleep(5)
#time.sleep(10)
for i in range(10): 
    sys.stdout.write('|'+'\r') 
    time.sleep(0.05)
    sys.stdout.write('/' +'\r') 
    time.sleep(0.05)
    sys.stdout.write('-' +'\r') 
    time.sleep(0.05)
    sys.stdout.write('\\' +'\r') 
    time.sleep(0.05)
postdata = {"text":"单位电脑开机提示","desp":now}
r = requests.post("https://sc.ftqq.com/" + sckey +".send",data=postdata)
print(r.text)
if eval(r.text)['errmsg'] == 'success':
    print('完成准备')
else:
    print('推送失败！！！')
input('输入任意字符则3秒后退出 \n')
time.sleep(3)

