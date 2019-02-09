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
    