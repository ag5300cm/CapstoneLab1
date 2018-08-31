
import random # getting random so I don't have to make one

guessMe = random.randint(1, 10)
print(guessMe) # for trouble shooting will remove later

print ("Lets play a game, guess a number 1 to 10 " ) #lets user know number range

userGuess = int(input("Guess a number? ")) # gets first guess

while guessMe != userGuess : # checks for match to continue loop or not
    if userGuess > guessMe : # if not correct will ask for user input again
        print("To high ") # letting use know there guess compared to number location
        userGuess = int(input("Guess a number? "))
    elif userGuess < guessMe :
        print("To low ")
        userGuess = int(input("Guess a number? "))
    else:
        break

print("Yay you win!!!") # will activate this after while loop it done