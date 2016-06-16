#from time import sleep
#import pygame

##def playMusic(time,file):
##    pygame.mixer.init()
##    pygame.mixer.music.load(file)
##    pygame.mixer.music.play()
##    sleep(time)
##    pygame.mixer.music.stop()

studentNames = ("Dirk","Julian","Dean","Gerry","Haydn","Lachlan","Tom","Andrew","Damian","Sam","Kyle","Jonathon")
index = 0

length = len(studentNames)
print("list lenght is "+str(length))

##studentNames.insert(6,"Peter")

for studentName in studentNames:
    print(str(index)+"\t"+studentName)
    index += 1

print(studentNames[4])










##print(studentNames[length-2])
##length = len(studentNames)
##
##studentNames.append("Eliza")
##length = len(studentNames)
##print(length)
##print(studentNames[length-1])
##
##studentNames.pop(0)
##length = len(studentNames)
##print(length)
##print(studentNames[0])

##while index <5:
##    print(str(index)+"\t"+studentNames[index])
##    index += 1
##
##
##
##
##
##playMusic(10,'Applause.ogg')

input("\nHit Enter key to exit program .......")  
