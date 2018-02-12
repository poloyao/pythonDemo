

from gpiozero import OutputDevice
from gpiozero import AngularServo
import time
import random
relay = OutputDevice(18,active_high=False)
relay.on()
#relay.off()

s = AngularServo(23, min_angle=-45, max_angle=45)
s.angle = 0.0
time.sleep(1)

# s.angle = 180
# time.sleep(2)
# s.angle = 0.0
# time.sleep(1)
count = 0
while True:
    if count < 30:
        time.sleep(1)
        s.angle = random.randint(0,40)
        print(s.angle)
        count = count + 1
    else:
        break

# sg90角度范围90度

# while True:
#     if s.angle < 45:
#         time.sleep(1)
#         s.angle = s.angle + 5
#         print(s.angle)
#     else:
#         break
# while True:
#     if s.angle > -45:
#         time.sleep(1)
#         s.angle = s.angle - 5
#         print(s.angle)
#     else:
#         break

s.angle = 0

time.sleep(3)

        