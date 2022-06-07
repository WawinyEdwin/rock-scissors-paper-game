# Rock-Paper-Scissors Game.
#access to random choice for the machine
import random

#possible options
# S = "scissors"
# R = "rock"
# P = "paper"

# choices for the machine player
choices = ["S", "R", "P"]


while True:
    #choices
    choiceCPU = random.choice(choices)
    choiceMe = None

    #
    while choiceMe not in choices:
        #user choice
        print("--Welcome To The Rock-Scissors-Paper Game--- \n")
    
        choiceMe = input("Choose between S, R and P: \n")

# if choices are equal we determine a tie
    if choiceMe == choiceCPU:
        print("Player-",(choiceMe) , ":", "CPU Player-", (choiceCPU))
        print('A Tie')
    elif choiceMe == "R":
        if choiceCPU == "P":
            print("Player-",(choiceMe) , ":", "CPU Player-", (choiceCPU))
            print('You Loose') 
        if choiceCPU == "S":
            print("Player-",(choiceMe) , ":", "CPU Player-", (choiceCPU))
            print('You Win')
    elif choiceMe == "S":
        if choiceCPU == "R":
            print("Player-",(choiceMe) , ":", "CPU Player-", (choiceCPU))
            print('You Loose') 
        if choiceCPU == "P":
            print("Player-",(choiceMe) , ":", "CPU Player", (choiceCPU))
            print('You Win')
    elif choiceMe == "P":
        if choiceCPU == "S":
            print("Player",(choiceMe) , ":", "CPU Player", (choiceCPU))
            print('You Loose') 
        if choiceCPU == "R":
            print("Player",(choiceMe) , ":", "CPU Player", (choiceCPU))
            print('You Win')
    else:
        print("Invalid Choice, Retry!")
        retry = input("Do you want to Retry! (yes/no)").lower()

        if retry != yes:
            break
    print("....")

    re_play = input("Do you want to play again? (yes/no) : ").lower()

    if re_play != "yes":
        break

print("Bye!")





