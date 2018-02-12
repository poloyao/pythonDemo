import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

#感应器侦测函数


def detct():
    #因为是仅仅试验，所以只让它循环运行100次
    for i in range(1, 101):
        #如果感应器针脚输出为True，则打印信息并执行蜂鸣器函数
        if GPIO.input(12) == True:
            print("Someone isclosing!")
        #否则将蜂鸣器的针脚电平设置为HIGH
        else:
            print("Noanybody!")
        time.sleep(2)


time.sleep(5)
detct()
GPIO.cleanup()
