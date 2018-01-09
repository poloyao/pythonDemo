import serial #pip install pyserial 小心与serial 冲突
import time
import threading
import datetime
# 用于显示表格
from prettytable import PrettyTable
import sys
import random

class PostThread:
    def __init__(self):
        self._running = True
    
    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
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

def UpdatePost(comid, mark,isShow = True):

    if  mark == '1':
        portList[comid-1][4] = b'\xAA\x01\x0d' 
        portList[comid-1][3] = '遮挡'
        if isShow:
            ShowTable()
        print (str(datetime.datetime.now()) + '  遮挡')
    else:
        portList[comid-1][4] = b'\xAA\x00\x0d'
        portList[comid-1][3] = '放开'
        if isShow:
            ShowTable()
        print (str(datetime.datetime.now()) + '  放开')

def UpdatePostAll(comid,mark):
    for item in portList:
        if mark == '1':
            item[4] = b'\xAA\x01\x0d'
            item[3] = '遮挡'
        else:
            item[4] = b'\xAA\x00\x0d'
            item[3] = '放开'
    ShowTable()


#随机改变串口状态，最低持续时间3秒
def RandomPostStatus():
    ranInt = random.randint(0,1)
    #print(ranInt)
    UpdatePost(1,str(ranInt),False)
    ranInt = random.randint(0,1)
    #print(ranInt)
    UpdatePost(2,str(ranInt),False)
    ranInt = random.randint(0,1)
    #print(ranInt)
    UpdatePost(3,str(ranInt),False)
    ranInt = random.randint(0,1)
    #print(ranInt)
    UpdatePost(4,str(ranInt),False)
    ranInt = random.randint(0,1)
    #print(ranInt)
    UpdatePost(5,str(ranInt),False)
    print("-----------------------")


class RandomPostThread:
    def __init__(self):
        self._running = True
    
    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            RandomPostStatus()
            time.sleep(3)

    
    

portList = [
    [1, '速度',  'com10','放开',b'\xAA\x00\x0d'],
    [2, '外检',  'com12','放开',b'\xAA\x00\x0d'],
    [3, '探平衡','com14','放开',b'\xAA\x00\x0d'],
    [4, '底盘',  'com16','放开',b'\xAA\x00\x0d'],
    [5, '制动',  'com18','放开',b'\xAA\x00\x0d']
    ]

s1 = serial.Serial(portList[0][2], 9600)
s2 = serial.Serial(portList[1][2], 9600)
s3 = serial.Serial(portList[2][2], 9600)
s4 = serial.Serial(portList[3][2], 9600)
s5 = serial.Serial(portList[4][2], 9600)

ShowTable() 

# thr = threading.Thread(target=postThread)
# thr.start()
        
def main():
    RandomPostStatus()
    tar = PostThread()
    thr = threading.Thread(target=tar.run)
    thr.start()

    tar2 = RandomPostThread()
    thr2 = threading.Thread(target=tar2.run)
    thr2.start()

    while True:
        print('输入项目ID 与 是否遮挡标记组合。[1]表示遮挡光电,[2]表示放开光电\n操作全部端口则使用 11，12组合\n退出请输入exit()')
        readInput = input('请输入组合标记：')
        if readInput == 'exit()':
            print('已退出程序')
            tar.terminate()
            return
        if readInput.__len__() != 2:
            print("输入标记不完整，请重新输入\n")
            continue
    
        id = readInput[0]
        if id == '0':
            UpdatePostAll(readInput[1])
        elif id == '1':
            UpdatePost(1,readInput[1])
        elif id == '2':
            UpdatePost(2,readInput[1])        
        elif id == '3':
            UpdatePost(3,readInput[1])        
        elif id == '4':
            UpdatePost(4,readInput[1])        
        elif id == '5':
            UpdatePost(5,readInput[1])

if __name__ == '__main__':
    main()

