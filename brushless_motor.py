import time
import pigpio
from adafruit_servokit import ServoKit

pi = pigpio.pi()
kit = ServoKit(channels=8)

motor = 4

while motor <= 400:
    key = input()
    if key == "ready":
        pi.set_PWM_dutycycle(motor, 0)
        time.sleep(3)
    if key == "go":
        pi.set_PWM_dutycycle(motor, 225)
        time.sleep(3)
    if key == "set":
        pi.set_PWM_dutycycle(motor, 128)
        time.sleep(3)
    if key == "a":
        kit.servo[0].angle = 100
        #time.sleep(1)
    if key == "aa":
        kit.servo[0].angle = 0
        #time.sleep(1)
pi.stop()
