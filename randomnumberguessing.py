# to import random module
import random
# to create a range of random numbers between 1-10
n = random.randrange(1,100)
# to take a user input to enter a number
guess = int(input("Enter any number: "))

while n!= guess: # means if n is not equal to the input guess
    
    if guess < n:
        print("Too low")
    
        guess = int(input("Enter any number: "))
    
    elif guess > n:
        print("Too high!")
    
        guess = int(input("Enter any number: "))
    
    else:
        break
print("you guessed it right!!")