import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 100)
p.start(0)
time.sleep(2)

p.ChangeDutyCycle(3)
time.sleep(2)