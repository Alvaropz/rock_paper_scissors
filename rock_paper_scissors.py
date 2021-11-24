import random
import math

def rock_paper_scissors(tries, tries_machine, total):
    min_win = int(total/2)+1
    print("'p' stands for 'paper'. 'r' stands for 'rock'. 's' stands for 'scissors'.")
    while tries > 0 and tries_machine > 0:
        choice = input("Your choice?: ").lower()
        if choice in ['p', 'r', 's']:
            choice_machine = random.choice(['p', 'r', 's'])
            if (choice == 'p' and choice_machine == 'r') or (choice == 'r' and choice_machine == 's') or (choice == 's' and choice_machine == 'p'):
                tries_machine -= 1
                print("Yes! You won! You chose '{}' and the machine chose '{}'.".format(choice.upper(), choice_machine.upper()))
            if (choice == 'p' and choice_machine == 's') or (choice == 'r' and choice_machine == 'p') or (choice == 's' and choice_machine == 'r'):
                tries -= 1
                print("Oh no! You lost! You chose '{}' and the machine chose '{}'.".format(choice.upper(), choice_machine.upper()))
            if (choice == choice_machine):
                print("You chose '{}' and the machine chose '{}'. It's a tie!".format(choice.upper(), choice_machine.upper()))
            if abs(tries - tries_machine) == min_win:
                break
        else:
            print("You didn't chose the right character. 'p' stands for 'paper'. 'r' stands for 'rock'. 's' stands for 'scissors'")

    if tries > tries_machine:
        return print("You won!")
    else:
        return print("You lost. :(")

print("You are playing rock, paper, scissors which is based on the popular game where you have to beat your oponent. The rules are:\nRock --> Scissors.\nScissors --> Paper.\nPaper --> Rock")
tries = input("How many tries do you want to do? ")
while True:
    if tries.isdigit():
        tries = int(tries)
        rock_paper_scissors(tries, tries, tries)
        break
    else:
        tries = input("How many tries do you want to do? ")