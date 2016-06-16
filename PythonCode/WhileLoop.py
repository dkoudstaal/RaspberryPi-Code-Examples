## Program: Play it again Sam
## File: WhileLoop.py
## Programmer: Dirk Koudstaal
## Date: 7 March 2014

# Import sleep for time module.
from time import sleep
import pygame

def playMusic(time,file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    sleep(time)
    pygame.mixer.music.stop()

# Ask for the number of times Sam should play his song.
playRequests=input("How many times do you want Sam to play his song?\nPlease enter a number  ")
print("\nYou have requested that Sam plays his songs",playRequests,"times\n")

# Convert the input to an integer.
playRequests=int(playRequests)

# Set the initial value of the counter (how many songs are played) to 0
numberPlayed = 0

# Start the loop and check how many times the loop has played the song.
# While that number is less than the number requested the loop keeps
# executing the commands.
# You have to link to your music file. mp3 might not work on the Pi
while numberPlayed < playRequests :
    print("Sam plays his song")
    playMusic(10,'MusicFile.ogg')

    # Count the number of times the song has been played
    numberPlayed=numberPlayed+1

    print("Sam has played his song",numberPlayed,"times\n")
    sleep(2)

# The while loop has finished because it has cycled through the number of requests.

print("Thank you Sam for playing your song",numberPlayed,"times\n")
print("Applause!!")
playMusic(10,'MusicFile.ogg')
