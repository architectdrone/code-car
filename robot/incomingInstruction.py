#Purpose: This is a prototype file for interfacing with the software written to actually control the robot.

'''
Command:
    (NOTE)
    Commands should be formatted as a dictionary.

    (MANDATORY)
    'command': String detailing which command will be executed. Use the following:
        -'forward': Go forward. The key 'rotations' specifies how many rotations to go forward.
        -'backward': Go backward. The key 'rotations' specifies how many rotations to go forward.
        -'left': Perform a -90 degree turn. When the instruction finishes, car's front will be -90 degrees from it's start.
        -'right': Perform a 90 degree turn. When the instruction finishes, car's front will be 90 degrees from it's start.
        -'stop': Stop for a certain number of seconds. The number of seconds is given by the key 'seconds'.
    
    (CONDITIONALLY MANDATORY)
    'rotations': Number of rotations. Mandatory only when 'command' is 'forward' or 'backward'. 
    'seconds': Number of seconds to stop. Mandatory only when 'command' is 'stop'.
'''

def getInstructionSet():
    '''
    Returns a list of commands. Each command should be formatted in the dictionary style documented above.
    @return A list of commands dictionaries, correctly formatted to the specifications of command dictionaries listed in incomingInstruction.py
    '''

    raise NotImplementedError("This has not yet been implemented.") #Put your code here.