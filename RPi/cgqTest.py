
# from gpiozero import OutputDevice
# from gpiozero import InputDevice
import time

# hcsr04_Out = OutputDevice(17)
# hcsr04_in = InputDevice(27)

def checkdist():
    hcsr04_Out.on()
    time.sleep(0.000015)
    hcsr04_Out.off()
    while not hcsr04_in.is_active:
        pass
    t1 = time.time()
    while hcsr04_in.is_active:
        pass    
    t2 = time.time()
    dist = (t2-t1)*340/1.93
    print('%0.2f m' %cdist)
    return dist

#持续检测距离，并核实
def checkdistEx():
    #print("1")
    time.sleep(0.05)
    dist = checkdist()
    result = False
    if dist < 4:        
        t1 = time.time()        
        count = 0
        for num in range(0,8):
            #print(num)
            time.sleep(0.05)
            dist2 = checkdist()
            print(dist)
            if dist2 > 4:
                count = count + 1
            #print(count)        
        if count < 3:            
            result = True
    #print(result)
    return result

        



time.sleep(2)



try:
    # while True:
    #     dist = checkdist()
    #     if dist < 4:
    #         print('距离: %0.2f m' %dist)
    while True:
        result = checkdistEx()
        #if result：

except:
    pass


