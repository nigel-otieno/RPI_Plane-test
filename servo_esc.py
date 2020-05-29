import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
angle = 0

while angle <= 120:
    key = input()
    if key == "a":
        kit.servo[0].angle = 100
    if key == "x":
        kit.servo[0].angle = 0
    if key == "q":
        kit.servo[1].angle = 100
    if key == "w":
        kit.servo[1].angle = 0


    
