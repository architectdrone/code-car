#Purpose: Execute code.py files, and perform nessesary file managament automatically.
import os
import time
DELAY = 0

executingAFile = False
while True:
    time.sleep(DELAY)
    os.system('clear')
    if executingAFile:
        print("Executing...")
    else:
        print("Nothing to execute (yet).")
    
    #Is a new code.py file ready?
    if not executingAFile: #Only run this is we are not executing a file already, or else we might execute the same script twice!
        #Forgive me father, I have sinned: I have used a try/except block for something other than error handling. 
        #The gist is that I am trying to see if code.py exists. If it does exist, we execute it. If not, we start over.
        try:
            open('code.py')
        except:
            continue
    else: #Now handle the deletion of the script.
        try:
            open('done.txt') #Test to see if the special done flag has appeared.
        except:
            continue #If not, we continue to wait for it to finish.
        else:
            #If the done flag is present, we delete it, code.py, and, finally, set executingAFile to False.
            os.system('rm done.txt')
            os.system('rm code.py')
            executingAFile = False
            continue
        
    
    executingAFile = True #Indicate that we are indeed executing a file.
    os.system('python3 code.py')
