#Purpose: simulate "playful" behavior, by using random movements and collision detection

import random
import robot
import RPi.GPIO as GPIO

CHECK_INCREMENT = 1.0 #When the robot checks to make sure it isn't too close to a wall.
MAX_SPIN_TIME = 3 #The maximum number of time that the robot can spin.
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

FAR_LEFT = P25
MIDDLE_LEFT = P24
MIDDLE_RIGHT = P23
FAR_RIGHT = P5

seconds_per_degree = robot.SECONDS_FOR_QUARTER_TURN/90

def _turnLeftDegrees(degrees):
    '''
    Turns left by a number of degrees.
    '''
    global seconds_per_degree
    robot._runForGivenTime(robot.LEFT, degrees*seconds_per_degree)

def _turnRightDegrees(degrees):
    '''
    Turns right by a number of degrees.
    '''
    global seconds_per_degree
    robot._runForGivenTime(robot.RIGHT, degrees*seconds_per_degree)

def move():
    #Do checking for collision avoidance.
    INPUT_FAR_LEFT = GPIO.input(FAR_LEFT)
    INPUT_MIDDLE_LEFT = GPIO.input(FAR_LEFT)
    INPUT_FAR_LEFT = GPIO.input(FAR_LEFT)
    INPUT_FAR_LEFT = GPIO.input(FAR_LEFT)