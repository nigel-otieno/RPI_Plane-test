import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
#key = input()

#To change servo total range
#kit.servo[0].actuation_range = 16
#while kit.servo[0].angle <= 180:
    #if key == "a":
        #kit.servo[0].angle = 90
    #if key == "aa":
        #kit.servo[0].angle = 0
kit.servo[0].angle = 90
time.sleep(1)
kit.servo[0].throttle = 180
time.sleep(1)



    
