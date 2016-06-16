## This code demonstrates how to program for push-down buttons
## The site below gives an excellent site for the explanation
## of a pull-down circuit and how to build it
## https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
## Coded by Dirk Koudstaal
## Not interested in claiming copyright!
## Modify it, use it, give it to others or delete it!

import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BOARD)
IO.setup(12,IO.IN)

print('The stat of an input pin is 0 (Boolen False).\
\nWhen the push-down button is pressed the state of the input pin\
\nwill change to 1 (True) and on release of the push-button\
\nthe input pin will change is status back to 0 (False).\
\nHowever, there is a slight delay in the status change\
\nfrom True back to False.\
\nThis is a program to capture this delay.')

print('\n\nThe status of the input pin is',IO.input(12))
input('\nHit the enter key to start the demo.........')
      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
 
loopCycles = 0
while True: # This while loop will capture the reset time for the input pin
    print("Push-button not pressed. Status of input pin = ",IO.input(12),"(False)")
    if IO.input(12):
        while IO.input(12):
            loopCycles += 1
            print(IO.input(12))
            sleep(0.01)
        break
print('You pressed the push-button\
\nStatus of input pint is reset to',IO.input(12),'(False)')
print('\nIt took',loopCycles,'cylces of the while loop to reset\
\nthe push-button input pin to a value of 0 (False)\
\nWhich is a total of',loopCycles,'x 0.01 =',0.01*loopCycles,'seconds') 
IO.cleanup()
