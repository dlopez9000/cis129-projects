# Lab 7 The Dice Game
# Darlene Lopez
# 3/10/2024
# This program is a simple dice game between two players 

import random

# the main function
def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':

        # populate variables
        winnersName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnersName = rollDice(p1number, p2number, playerOne, playerTwo, winnersName)

        # call to displayInfo
        displayInfo(winnersName)

        endProgram = input('Do you want to end program? (yes/no): ')

# this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter Player One's Name: ")
    playerTwo = input("Enter Player Two's Name: ")
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number > p2number:
        winnersName = playerOne
    elif p1number < p2number:
        winnersName = playerTwo
    else:
        winnersName = "TIE"

    return winnersName

# this function displays the winner
def displayInfo(winnersName):
    print("The winner is:", winnersName)

# calls main
main()

