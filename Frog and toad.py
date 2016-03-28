##Frog and toad puzzle game
##Robert Roe: 150409241
##SEF034: Assignment 4

import os
import sys

def main():
    choice = menu()
    while(choice != 0): ##Loops until option 4 is chosen
        if (choice == 1):
            PlayGame()
        elif(choice == 2):
            RunDemonstration()
        elif(choice == 3):
            PrintRules()
        elif(choice == 4):
            print("Goodbye")
            sys.exit()
        else:
            print("Choice not valid")
            choice = menu()
        choice = menu()
        
def menu():
    choice = 0
    print("""\n\tWelcome to Frogs vs toads.\n
    Pick an option:
    \t1. Play game
    \t2. See a computer demonstration
    \t3. Rule list
    \t4. Quit""")
    while(choice == 0):
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Value error. Please enter a valid choice")
    return choice

def PlayGame():##Entire game is run from this function
    OriginalLog = ["T", "T", "T", "", "F", "F", "F"] ##Initialises "log" in game
    GameList = OriginalLog
    MovesValid = True
    while(MovesValid):
        print("Here is your log: " + str(GameList))
        MovesValid = AnyMovesValid(GameList)
        choice = PlayerOption()
        if(choice == 1):
            GameList = MoveFrog(GameList)
        if(choice == 2):
            GameList = ["T", "T", "T", "", "F", "F", "F"]
            print("Log reset")
        if(choice == 3):
            print("Goodbye")
            sys.exit()
        else:
            print("Choice not valid")
        MovesValid = AnyMovesValid(GameList)
    if(GameList == OriginalLog[::-1]):
        print(GameList)
        print("CONGRATULATIONS, YOU'VE WON")
    else:
        print("No moves left. Bad Luck")
        
def PlayerOption():
    choice = 0
    print("\n\tWhat will you do?\n1. Move Frogs/Toads\n2. Reset log\n3. Quit program")
    while(choice == 0):
        try:
            choice = int(input("\nEnter Choice: "))
        except ValueError:
            choice == 0
            print("Option Not Valid")
    return choice

def MoveFrog(GameList):#Gets movement info, checks if valid, then moves animal
    try:
        n1 = int(input("Select frog/toad to move: "))
        n1 -=1 ##Creates index position from user input
        n2 = int(input("Select position to move to: "))
        n2 -=1
        if(CheckValidMove(n1, n2, GameList)):
            GameList = MoveFrogPositions(n1, n2, GameList)
    except ValueError:
        print("Value not valid")
    return GameList

def CheckValidMove(n1, n2, GameList): ##Checks Reasons that move could not be completed
    IsMoveValid = True
    if(abs(n1-n2)>2):
        print("Jump is too big")
        IsMoveValid = False
        return IsMoveValid
    if(GameList[n1] == ""):
        print("No amphibian in initial space")
        IsMoveValid = False
        return IsMoveValid
    if(n1==n2):
        print("Cannot jump to same place")
        IsMoveValid = False
        return IsMoveValid
    if(GameList[n2] != ""):
        print("Target space is not free")
        IsMoveValid = False
        return IsMoveValid
    if(GameList[n1] == "T" and n2<n1):
        print("Toads cannot move backwards")
        IsMoveValid = False
        return IsMoveValid
    if((GameList[n1] == "F" and n1<n2)):
        print("Frogs cannot move backwards")
        IsMoveValid = False
        return IsMoveValid
    return IsMoveValid

def AnyMovesValid(GameList):##Checks to see if there are any valid moves on the board
    ValidMove = False
    for i in range((len(GameList))): ##For each item in list
        if(GameList[i] == "F"): ##If Item is a frog
            try: ##Tries for next two spaces
                if(GameList[i-1] == "" or GameList[i-2] == ""):
                    ValidMove = True
            except IndexError: ##Will throw if either index isn't valid
                try: ##Tries again with the higher index
                    if(GameList[i-1] == ""):
                        ValidMove = True
                except IndexError: ##If higher index isn't valid
                    pass
        if(GameList[i] == "T"): ##Does the same process as above but for toads
            try:
                if(GameList[i+1] == "" or GameList[i+2] == ""):
                    ValidMove = True
            except IndexError:
                try:
                    if(GameList[i+1] == ""):
                        ValidMove = True
                except IndexError:
                    pass
    return ValidMove ##returns true if any moves are valid
    
def MoveFrogPositions(OriginalPos, NewPos, GameList):#Moves frog/toad within list
    GameList[NewPos] = GameList[OriginalPos]
    GameList[OriginalPos] = ""
    return GameList

def RunDemonstration():
    print("\n\tHere is your log, with 3 toads and 3 frogs, and one free space")
    print("""["T", "T", "T", "", "F", "F", "F"] """)
    print("\n\tFrogs can only move to the left, and toads to the right, as shown below")
    print("""["T", "T", "T", "", "F", "F", "F"] """)
    print("""["T", "T", "T", "F", "", "F", "F"] """)
    print("\tor")
    print("""["T", "T", "T", "", "F", "F", "F"] """)
    print("""["T", "T", "", "T", "F", "F", "F"] """)
    print("\n\tBoth animals can jump over one another, but only by one space")
    print("""["T", "T", "", "T", "F", "F", "F"] """)
    print("""["T", "T", "F", "T", "", "F", "F"] """)
    print("\n\tOnce they have switched places, the game has been won, like so")
    print("""["F", "F", "F", "", "T", "T", "T"] """)
    print("\n\tGood Luck!")

def PrintRules():
    print("""\tRules
    - Frogs may only move right
    - Toads may only move left
    - Both frogs and toads can jump over one space to reach a free space
    - Once both species have switched ends, the game is over
    - The game can be reset at any time""")


main()
