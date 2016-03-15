##Frog and toad puzzle game
##Robert Roe: 150409241
##SEF034: Assignment 4

import os
import sys

def main():
    choice = menu()
    while(choice != 0): ##Loops until option 2 is chosen
        if (choice == 1):
            PlayGame()
        elif(choice == 2):
            sys.exit()
        else:
            print("Choice not valid")
            choice = menu()
        

def menu():
    choice = 0
    print("""\tWelcome to Frog's vs toads.\n
Pick an option:
\t1. Play game
\t2. Quit""")
    while(choice ==0):
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Value error. Please enter a valid choice")
    return choice


def PlayGame():
    GameList = ["T", "T", "T", "", "F", "F", "F"]
    MovesValid = True
    while(MovesValid):
        print("Here is your log: " + str(GameList))
        MovesValid = False
        print("False statement declared")
