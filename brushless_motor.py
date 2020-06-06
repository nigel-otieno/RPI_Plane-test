import time
import pigpio
from adafruit_servokit import ServoKit

pi = pigpio.pi()
kit = ServoKit(channels=8)

angle = 0
SERVO = 4

while True & angle <=150:
    key = input()
    if key == "ready":
        pi.set_PWM_dutycycle(SERVO, 0)
        time.sleep(3)
    if key == "go":
        pi.set_PWM_dutycycle(SERVO, 225)
        time.sleep(3)
    if key == "set":
        pi.set_PWM_dutycycle(SERVO, 128)
        time.sleep(3)
    if key == "a":
        kit.servo[0].angle = 100
        time.sleep(1)
    if key == "aa":
        kit.servo[0].angle = 0
        time.sleep(1)
    if key == "q":
        kit.servo[1].angle = 100
        time.sleep(1)
    if key == "qq":
        kit.servo[1].angle = 0
        time.sleep(1)
pi.stop()
