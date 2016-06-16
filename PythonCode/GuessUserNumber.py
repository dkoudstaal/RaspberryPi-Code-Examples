# Guess User's Numbers

print(
"""
This Program will attempt to guess a number that you have chosen.

Think of a number between 1 and 1000. Don't tell the computer :-)

When you are asked if the number is correct answer any one of the following:

    correct
    higher
    lower

If you want to leave the game answer with:

    exit
""")
userResponses=("lower","higher","correct","exit")

while True:
    maxGuess = 1000
    minGuess = 1
    computerGuess = maxGuess//2
    userResponse = ""
    triedGuess = 1
    wrongGuess = False

    while True:
        
        print("\n"+str(computerGuess))
        userResponse= input("Is this number correct?\nIf you want to \
leave the game answer with exit \nOtherwise answer with correct, higher \
or lower   ")
        userResponse = userResponse.lower()
        
##        for response in userResponses: # check for wrong user entry
##            if response == userResponse:
##                wrongGuess = False
##                break
##            else:
##                wrongGuess = True
##
##        if wrongGuess :
##            print("\n----Wrong Entry!----\n----Try Again!----")
##            
        if userResponse == userResponses[3]: # exit
            break        
        elif userResponse == userResponses[2]: # correct
            print("\nBingo!! \nThe computer guessed your number")
            print ("And it took "+str(triedGuess)+" times to guess your number")
            break
        elif userResponse ==userResponses[1]: # higher
            minGuess = computerGuess
            computerGuess = minGuess + ((maxGuess-minGuess)//2)
            triedGuess += 1
        elif userResponse == userResponses[0]: # lower
            maxGuess = computerGuess
            computerGuess = minGuess + ((maxGuess-minGuess)//2)
            triedGuess += 1
        else:
            print("\n----Wrong Entry!----\n----Try Again!----")

    playGame = input("\nDo you want to play an other game?\nAnswer yes or no  ")
    if playGame == "yes":
        print("You have started a new game.\n")
    else:
        break
        
print("\nPress the Enter key to exit")        
input("\n")        

