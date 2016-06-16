## Code demonstrating the use of a push-button
## to toggle the Pi Cam on or off.
## This program is not complete and you have to
## create the code to get out of the permanent while loop.
## Coded by Dirk Koudstaal
## Not interested in claiming copyright!
## Modify it, use it, give it to others or delete it!

import RPi.GPIO as IO
import picamera
from time import sleep

IO.setmode(IO.BOARD)
IO.setup(12,IO.IN)

camera=picamera.PiCamera()

cameraOn = False

print('The push-button acts as a toggle to turn on and off the camera\
\nA while loop set to True is used to create the toggle behaviour\
\nYou have to code for the event the user does not want to use the\
\ncamera any more.\
\nTo get out of the program use the keys Ctrl C when the camera is\
\nin the off mode.')

input('Hit enter to activate the push-down button........')


while True: # This is a infinite loop. You hae to program for its exit.
        
    if IO.input(12):
        if cameraOn == True:
            cameraOn = False
            camera.stop_preview()
            while IO.input(12):
                sleep(0.01)

        else:
            cameraOn = True
            camera.start_preview()
            while IO.input(12):
                sleep(0.01)

IO.cleanup()
