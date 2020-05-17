import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)

servo1.start(0)
print ("waiting 2 seconds")
time.sleep(2)

print ("rotating servo 180 degrees")
duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    servo1.ChangeDutyCycle(7)
    time.sleep(1)
    # duty = duty + 1
    
time.sleep(2)

servo1.stop()
GPIO.cleanup()
print ("good job")