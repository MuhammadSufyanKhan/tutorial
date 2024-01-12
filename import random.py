import random 

topofrange= input("Type a Number: ")

if topofrange.isdigit():
    topofrange = int(topofrange)

    if topofrange <=0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print ("Please type a number next time.")
    quit()

randumnumber=random.randint(0, topofrange)
guesses = 0

while True:
    guesses +=1
    userguess = input("Make a Guess: ")
    
    if userguess.isdigit():
        userguess = int(userguess)
    else:
        print ("Please type a number next time.")
        continue

    if userguess==randumnumber:
        print("you guessed it right")
        break
    elif userguess > randumnumber:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses")