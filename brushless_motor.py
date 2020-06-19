import time
import pigpio
#from adafruit_servokit import ServoKit

pi = pigpio.pi()
#kit = ServoKit(channels=8)

motor = 4

while motor <= 2000:
    key = input()
    if key == "4":
        pi.set_servo_pulsewidth(4, 1000)    # off
        time.sleep(3)
    if key == "3":
        pi.set_servo_pulsewidth(4, 2000)    # off
        time.sleep(3)
    if key == "2":
        pi.set_servo_pulsewidth(4, 1100)    # off
        time.sleep(3)
    if key == "1":
        pi.set_servo_pulsewidth(4, 1500)    # off
        time.sleep(3)
        
    if key == "aaa":
        kit.servo[0].angle = 100
        #time.sleep(1)
    if key == "aa":
        kit.servo[0].angle = 180
        #time.sleep(1) 
    if key == "a":
        kit.servo[0].angle = 0
        #time.sleep(1)
        
    if key == "q":
        kit.servo[1].angle = 100
        #time.sleep(1)
    if key == "qq":
        kit.servo[1].angle = 180
        #time.sleep(1)
    if key == "qqq":
        kit.servo[1].angle = 0
        #time.sleep(1)
        
pi.stop()
