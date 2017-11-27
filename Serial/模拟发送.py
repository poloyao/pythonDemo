import serial #pip install pyserial 小心与serial 冲突
import time
import threading
import datetime
# 用于显示表格
from prettytable import PrettyTable


def postThread():
    while True:
        # if s.is_open == False:
        #     s.open()
        s1.write(portList[0][4])
        s2.write(portList[1][4])
        s3.write(portList[2][4])
        s4.write(portList[3][4])
        s5.write(portList[4][4])
        #s.write(tx)
        time.sleep(0.1)

def ShowTable():
    x = PrettyTable(['ID','速度','串口','遮挡状态','text'])
    x.padding_width = 3
        
    for i in range(portList.__len__()):
        x.add_row(portList[i])

    print(x)

def UpdatePost(comid, mark):

    if  mark == '1':
        portList[comid-1][4] = b'\xAA\x01\x0d' 
        portList[comid-1][3] = '遮挡'
        ShowTable()
        print (str(datetime.datetime.now()) + '  遮挡')
    else:
        portList[comid-1][4] = b'\xAA\x00\x0d'
        portList[comid-1][3] = '放开'
        ShowTable()
        print (str(datetime.datetime.now()) + '  放开')
    
portList = [
    [1, '速度',  'com10','放开',b'\xAA\x00\x0d'],
    [2, '外检',  'com12','放开',b'\xAA\x00\x0d'],
    [3, '探平衡','com14','放开',b'\xAA\x00\x0d'],
    [4, '底盘',  'com16','放开',b'\xAA\x00\x0d'],
    [5, '制动',  'com18','放开',b'\xAA\x00\x0d']
]

#pName = input('输入待连接的串口名：\n')
s1 = serial.Serial(portList[0][2], 9600)
s2 = serial.Serial(portList[1][2], 9600)
s3 = serial.Serial(portList[2][2], 9600)
s4 = serial.Serial(portList[3][2], 9600)
s5 = serial.Serial(portList[4][2], 9600)

ShowTable()   

# #转码后写入
# # tx = '111111'.encode(encoding='utf_8')

#tx = b'\xAA\x00\x0d'

thr = threading.Thread(target=postThread)
thr.start()

while True:
    print('输入项目ID 与 是否遮挡标记组合。[1]表示遮挡光电,[2]表示放开光电\n')
    readInput = input('请输入组合标记：')
    if readInput.__len__() != 2:
        print("输入标记不完整，请重新输入\n")
        continue
    id = readInput[0]
    if id == '1':
        UpdatePost(1,readInput[1])
    elif id == '2':
        UpdatePost(2,readInput[1])        
    elif id == '3':
        UpdatePost(3,readInput[1])        
    elif id == '4':
        UpdatePost(4,readInput[1])        
    elif id == '5':
        UpdatePost(5,readInput[1])
        


