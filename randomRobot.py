#Purpose: simulate "playful" behavior, by using random movements and collision detection

import random
import robot
import RPi.GPIO as GPIO

CHECK_INCREMENT = 1.0 #When the robot checks to make sure it isn't too close to a wall.
P25= 25
P24= 24
P23= 23
P5 = 5

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(P25, GPIO.IN)
GPIO.setup(P24, GPIO.IN)
GPIO.setup(P23, GPIO.IN)
GPIO.setup(P5, GPIO.IN)

def forwardCheck():
    '''
    Checks the sensors to see if we are close to an object.
    @return True if we are too close, False if we are good.
    '''
    if GPIO.input(P25) or GPIO.input(P24) or GPIO.input(P23) or GPIO.input(P5): 
        return True
    return False

