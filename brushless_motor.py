import time
import pigpio
import pygame
from adafruit_servokit import ServoKit

#set pi to
pi = pigpio.pi()
 
pygame.init()
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize the joysticks
j = pygame.joystick.Joystick(0)
j.init()

# Set kit to access pca9685 servo channels
kit = ServoKit(channels=8)

# Create variable for gpio pin
motor = 4


while not done:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Set event type to access JOYBUTTONDOWN for servos and motor
        if event.type == pygame.JOYBUTTONDOWN:
         
            # If joybuttondown key value is pressed, motor will output a response 
            if j.get_button(8):
                pi.set_servo_pulsewidth(4, 1000)    # off
                time.sleep(3)                
                print(event.button)
            if j.get_button(9):
                pi.set_servo_pulsewidth(4, 1500)    # 50% power
                time.sleep(3)                
                print(event.button)
            if j.get_button(0):
                pi.set_servo_pulsewidth(4, 1800)    # 80% power
                time.sleep(3)                
                print(event.button)
                
            # If joybuttondown key value is pressed, servos will output a response 
            if j.get_button(10):
                kit.servo[1].angle = 110
                print(event.button)
            if j.get_button(11):
                kit.servo[0].angle = 110              
                print(event.button) 
        
        # Set event type to access JOYBUTTONUP 
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        
        # Set event type to access JOYAXISMOTION for servo reset
        if event.type == pygame.JOYAXISMOTION:
            
            # If JOYAXISMOTION key value is moved up, servos will resest original position  
            if j.get_axis(2):
                kit.servo[0].angle = 0    
                print(event.axis)
            if j.get_axis(1):
                kit.servo[1].angle = 0    
                print(event.axis)
        
pi.stop()
