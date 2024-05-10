#Random Guess Number
import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quiet(Q): ")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Sucess: Correct Guess!!")
        break
    elif(userChoice < target):
        print("Guess number is too small. Take a bigger guess..")
    else:
        print("Guess number is too big. Take a smaller guess..")