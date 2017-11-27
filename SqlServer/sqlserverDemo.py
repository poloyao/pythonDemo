import os
import pymssql
import MSSQLHelper
from prettytable import PrettyTable
import random
import string

def ShowTable(sqlList,tabHeader):
    x = PrettyTable(tabHeader)
    #x.padding_width = 3
        
    for i in range(sqlList.__len__()):
        x.add_row(sqlList[i])

    print(x)


#host 注意格式
ms = MSSQLHelper.MSSQLHelper(host="192.168.1.1",user="sa",pwd="sa",db="sa")


name =  ''.join(random.sample(string.ascii_letters + string.digits, 6))
hphm = '辽' + ''.join(random.sample(string.ascii_letters + string.digits, 6))
insertSql = "INSERT CarInfo (Name,HPHM) values ('{}','{}')".format(name,hphm)
ms.ExecNonQuery(insertSql.encode('utf-8'))


reslist = ms.ExecQuery("select id,name,hphm from CarInfo")

for i in range(reslist.__len__()):
    row = list(reslist[i])
    row[2] = row[2].encode('latin-1').decode('gbk')
    reslist[i] = row

ShowTable(reslist,['ID','Name','HPHM'])

reslist = ms.ExecQuery("select * from WaitDetection")
ShowTable(reslist,['ID','CarID','流水号','线号','状态'])

