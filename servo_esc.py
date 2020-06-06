import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
#key = input()
angle = 0

#kit.servo[0].angle =180
while angle <= 150:
    key = input()
    if key == "a":
        kit.servo[0].angle = 100
        #time.sleep(1)
    if key == "aa":
        kit.servo[0].angle = 0
        #time.sleep(1)
    if key == "q":
        kit.servo[1].angle = 100
        #time.sleep(1)
    if key == "qq":
        kit.servo[1].angle = 0
        #time.sleep(1)
    if key == "s":
        kit.continuous_servo[2].throttle = 0
        #time.sleep(1)
    if key == "ss":
        kit.continuous_servo[2].throttle = 1
        #time.sleep(1)
    
