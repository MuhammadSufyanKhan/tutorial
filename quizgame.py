print("Welcome to my computer Quiz!")
playing = input("Do you wanna play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score=0
answer=input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print(f'Wrong')

answer=input("What does GPU stand for ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print(f'Wrong')

answer=input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print(f'Wrong')

answer=input("what does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print(f'Wrong')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")

