# from bottle import route,run,template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>hello {{name}} </b>!',name = name)

# run(host='0.0.0.0')



from bottle import get,post,run,request,template
from gpiozero import LED,Button
from gpiozero import OutputDevice
import time


led = LED(17)
led1 = LED(27)
led2 = LED(22)


def operateLed(currentLed):
    if currentLed.is_active == False:
        currentLed.on()
    else:
        currentLed.off()
    return currentLed

@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    result = request.body.read().decode
    print("按下了按钮: "+result)
    if len(result) == 1:        
        if result == "0":
            operateLed(led)
        elif result == '1':
            operateLed(led1)
        else:
            operateLed(led2)   
    else:
        if result[0] == "0":
            operateLed(led)
            time.sleep(1)
            operateLed(led)
        elif result[0] == '1':
            operateLed(led1)
            time.sleep(1)
            operateLed(led1)
        else:
            operateLed(led2) 
            time.sleep(1)
            operateLed(led2)   
    return "OK"


run(host="0.0.0.0")

# 设置设备参数，高低电平，初始化常开常闭等
# relay = gpiozero.OutputDevice(17,active_high=False)
# relay.on()
# relay.off()






