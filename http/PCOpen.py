#encoding:UTF-8

import requests
import datetime
import time

print('正在开机准备中，请勿关闭此界面')
time.sleep(10)
now = datetime.datetime.now()
print('系统当前时间为：' + now)
postdata = {"text":"单位电脑开机提示","desp":now}
r = requests.post("https://sc.ftqq.com/SCU19816T7a23e7a4100df029bc8061e0348c0a845a5420ffd26a3.send",data=postdata)
print(r.text)
print('完成准备，退出')
