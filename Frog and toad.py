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


def PlayGame():##Entire game is run from this function
    GameList = ["T", "T", "T", "", "F", "F", "F"] ##Initialises "log" in game
    MovesValid = True
    while(MovesValid):
        print("Here is your log: " + str(GameList))
        GameList = MoveFrog(GameList)
        
        

def MoveFrog(GameList):
    n1 = int(input("Select frog to move: "))
    n1 -=1 ##Creates index position from user input
    n2 = int(input("Select position to move to: "))
    n2 -=1
    if(CheckValidMove(n1, n2, GameList)):
        GameList = MoveFrogPositions(n1, n2, GameList)

    return GameList

def CheckValidMove(n1, n2, GameList): ##Checks Reasons that move could not be completed
    IsMoveValid = True
    if(abs(n1-n2)>2):
        print("Jump is too big")
        IsMoveValid = False
        return IsMoveValid
    if(n1==n2):
        print("Cannot jump to same place")
        IsMoveValid = False
        return IsMoveValid
    if(GameList[n1] == ""):
        print("No amphibian in initial space")
        IsMoveValid = False
        return IsMoveValid
    if(GameList[n2] != ""):
        print("Target space is not free")
        IsMoveValid = False
        return IsMoveValid
    return IsMoveValid
    
def MoveFrogPositions(OriginalPos, NewPos, GameList):
    print("Move Frogs")
    return GameList
