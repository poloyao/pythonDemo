# pymssql
## 安装
需要先在本地安装**pymssql**，但如果直接使用pip安装会报错误，无法安装。需要先下载whl文件后，本地手动pip安装
[PyMssql下载地址](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql)
- 注意本地python的版本位数，安装步骤可遵从[微软建议](https://docs.microsoft.com/en-us/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development)
- 注意host地址的格式，192.168.1.1:1000 
- 注意传入及获取的数据格式转换为utf-8，编码中文乱码
- 如果先要显示中文数据，则需要将指定元祖内容重新编码
```
for i in range(reslist.__len__()):
    row = list(reslist[i])
    row[2] = row[2].encode('latin-1').decode('gbk')
    reslist[i] = row
```

### 生成随机数方法
```
name =  ''.join(random.sample(string.ascii_letters + string.digits, 6))
```




