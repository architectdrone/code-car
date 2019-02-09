import incomingInstruction as incoming

def control():
    '''
    Main controlling function for the robot. Either executes a block of instructions, or performs some predefined idle functionality.
    '''

    newInstructionSet = incoming.getInstructionSet() #Get the newest instruction set from our interface.
    if newInstructionSet == []:
        idle()
    else:
        execute(newInstructionSet)

def idle():
    '''
    THings to do as the robot is idling.
    '''
    pass #I haven't decided on anything yet ;)

def execute(toExecute):
    '''
    Executes a list of commands formatted in the way described by incomingInstruction.py.
    @param toExecute A list of properly formatted command dictionaries. 
    '''

    for i in toExecute:
        if i['command'] == 'forward':
            forward(i['rotations'])
        elif i['command'] == 'backward':
            backward(i['rotations'])
        elif i['command'] == 'left':
            left()
        elif i['command'] == 'right':
            right()
        elif i['command'] == 'stop':
            stop(i['seconds'])
        else:
            raise KeyError(f"Unrecognized command {i['command']}.")
    

