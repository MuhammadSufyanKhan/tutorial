import random

userwins=0
computerwins=0
tie=0


options=["rock", "paper", "scissors"]

while True:
    userinput= input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if userinput == "q":
        break
    if userinput not in options:
        continue

    randomnumber=random.randint(0,2)
    computerpick = options[randomnumber]
    print (f"Computer picked {computerpick}")

    if userinput==computerpick:
        print("Tie")
        tie+=1
    elif userinput== "rock" and computerpick == "scissors" or userinput=="paper"and computerpick=="rock" or userinput=="scissors"and computerpick=="paper":
        print("You Won!")
        userwins+=1
    else:
        print("You lose!")
        computerwins+=1


print(f"Games Tie {tie} times")
print(f"You won {userwins} times")
print(f"The Computer won {computerwins} times")  
print("Good Bye")