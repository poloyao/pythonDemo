import serial #pip install pyserial 小心与serial 冲突
import time
import threading
import datetime

def postThread():
    while True:
        if s.is_open == False:
            s.open()
        s.write(tx)
        time.sleep(0.1)

pName = input('输入待连接的串口名：\n')
s = serial.Serial(pName, 9600, timeout=2)
# print(s.is_open)
# if s.is_open == False:
#     s.open()
# #转码后写入
# # tx = '111111'.encode(encoding='utf_8')
# s.write(tx)
# s.close()

tx = b'\xAA\x00\x0d'

thr = threading.Thread(target=postThread)
thr.start()

while True:
    if  input('输入[1]表示遮挡光电,[2]表示放开光电:\n') == '1':
        tx = b'\xAA\x01\x0d' 
        print (str(datetime.datetime.now()) + '  遮挡')
    else:
        tx = b'\xAA\x00\x0d'
        print (str(datetime.datetime.now()) + '  放开')
    #print (datetime.datetime.now())


