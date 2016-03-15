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
        choice = menu()
        

def menu():
    choice = 0
    print("""\n\tWelcome to Frog's vs toads.\n
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

def MoveFrog(GameList):
    n1 = int(input("Select frog to move: "))
    n1 -=1 ##Creates index position from user input
    n2 = int(input("Select position to move to: "))
    n2 -=1
    if(CheckValid(n1, n2)):
        GameList = MoveFrogPositions(n1, n2)

def CheckValidMove(n1, n2):
    print("Valid move check")
    return True

def MoveFrogPositions(GameList):
    print("Move Frogs")
    return GameList
