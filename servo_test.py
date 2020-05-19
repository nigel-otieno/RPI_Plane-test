import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo2 = GPIO.PWM(13, 50)


servo1.start(0)
servo2.start(0)
print ("waiting 2 seconds")
time.sleep(2)

print ("rotating servo 90 degrees")
duty = 2

while True:
    while duty <= 12:
        key = input()
        
        #Left Servo Control
        if key == "a":
            servo1.ChangeDutyCycle(duty)
            time.sleep(0.5)
        elif key == "aa":
            servo1.ChangeDutyCycle(7)
            time.sleep(0.5)
            
        #Right Servo Control
        elif key == "q":
            servo2.ChangeDutyCycle(duty)
            time.sleep(0.5)
        elif key == "qq":
            servo2.ChangeDutyCycle(7)
            time.sleep(0.5)
            
    
time.sleep(2)

servo1.stop()
servo2.stop()

GPIO.cleanup()
print ("good job")
