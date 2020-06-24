# RASPBERRY PI PLANE
Raspberry Pi is used to control servos via Adafruit PCA9685. The Raspberry Pi uses Joans PIGPIO library to accurately set and control the brushless motors esc via Pulse Width Modulation(PWM).

# Motivation
To gain a deeper understading of implementing software and hardware through the Python Language.

# PROJECT PARTS LIST
  -Raspberry Pi(any version 3 & 4 will work)
  
  -AdaFruit PCA9685(Servo Controller)
  
  -Lipo Battery
  
  -Lipo Charger
  
  -Brushless Motor/ESC
  
  -2 Servos
  
  -Jumper Cables(M/F, M/M, F/F)
  
  -Portable 10000mah charger(Optional)


*PCA9685 WIRING to RASPBERYY PI
  1. Pi 3V3 to sensor VCC
  2. Pi GND to sensor GND
  3. Pi SCL to sensor SCL
  4. Pi SDA to sensor SDA


*PCA9685 INSTALLATION
  *install within project folder
  - sudo pip3 install adafruit-circuitpython-pca9685
  - sudo pip3 install adafruit-circuitpython-servokit

*Joans PIGPIO Library
  *install within project folder
  wget https://github.com/joan2937/pigpio/archive/master.zip
  unzip master.zip
  cd pigpio-master
  make
  sudo make install
  sudo pigpiod(activate)
  sudo killall pigpio(deactivate)


 


  
  
