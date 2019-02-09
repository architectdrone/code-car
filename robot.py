#This module is used by scripts generated by the user's GUI.
import time
import RPi.GPIO as GPIO

#GLOBALS: You set this.
#GPIO
IN1 = 12
IN2 = 13
ENA = 6
IN3 = 20
IN4 = 21
ENB = 26

#Port Lists
#A list of ports corresponding to an action.
FORWARD = [IN1, IN4]
BACKWARD = [IN2, IN3]
LEFT = [IN4]
RIGHT = [IN1]

#Calibration
SECONDS_PER_1_ROTATION = 3.2 #We need to do some calibration of this.
SECONDS_FOR_QUARTER_TURN = 3.4 #Also needs calibration

#SETUP GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

#PUBLIC
def forward(rotations):
    '''
    Causes the robot to go forward by the number of rotations specified.
    @param rotations Number of rotations to go forward.
    '''
    global FORWARD
    _runForGivenTime(FORWARD, _convertRotationsToSeconds(rotations))

def backward(rotations):
    '''
    Causes the robot to go backward by the number of rotations specified.
    @param rotations Number of rotations to go backward.
    '''
    global BACKWARD
    _runForGivenTime(BACKWARD, _convertRotationsToSeconds(rotations))

def left():
    '''
    Turn left.
    '''
    global LEFT
    global SECONDS_FOR_QUARTER_TURN
    _runForGivenTime(LEFT, SECONDS_FOR_QUARTER_TURN)

def right():
    '''
    Turn right.
    '''
    global RIGHT
    global SECONDS_FOR_QUARTER_TURN
    _runForGivenTime(RIGHT, SECONDS_FOR_QUARTER_TURN)

def stop(seconds):
    '''
    Stop for a certain number of seconds.
    @param seconds Number of seconds to stop.
    '''
    time.sleep(seconds)

#PRIVATE

def _run(port):
    '''
    PRIVATE: Starts driving power to the given pin.
    @param port The port to drive to.
    '''
    GPIO.output(port, GPIO.HIGH)

def _halt(port):
    '''
    PRIVATE: Stops driving power to the given pin.
    @param port The port to stop driving to.
    '''
    GPIO.output(port, GPIO.LOW)

def _runForGivenTime(portList, _time):
    '''
    PRIVATE: runs a list of ports, for a given amount of time, before stopping them.
    @param portList A list of ints specifing ports to run.
    @param _time Amount of time to run the ports.
    '''
    for i in portList:
        _run(i)
    time.sleep(_time)
    for i in portList:
        _halt(i)


def _convertRotationsToSeconds(rotations):
    '''
    Converts a number of rotations into seconds, which can be used by the hardware.
    @param rotations Rotations to convert.
    @return Float number of seconds. 
    '''
    global SECONDS_PER_1_ROTATION
    return rotations*SECONDS_PER_1_ROTATION

