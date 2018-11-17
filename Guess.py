
#Import modules
import random
#Read comment for: except ValueError
try:
    #Decide the number
    playerGuess = int(input())
    computerNum = random.randint(1, 10)
    print("Number here")

    #Print instructions and computer's number
    print("Made By Cody")
    print("Type a number between 1 and 10 to guess!")
    print("")
    
    print("----------------------------------------------------\n") #Seperator
    
    #Logic
    #In case user's guess is over 10
    if playerGuess > 10:
        print("ERROR: Guess was over 10. Please try again.")
    
    else:
        print("You guessed: " + str(playerGuess))
        print("The computer's number was: " + str(computerNum))
    
        if playerGuess == computerNum:
            print("\nYour guess was correct! Nice job!")
        
        else:
            print("\nNice try, but incorrect. Try again!")

#In case user doesn't type anything
except ValueError:
    print("ERROR: Invalid input:\n")
    print("A simple guessing game created by Cody Summers")
    print("Type a number between 1 and 10 to guess!")
    
