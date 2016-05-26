from sys import exit as e
from time import sleep
from random import choice

board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9]
wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
val = "X"
lastMove = "O"

def printBoard():
    global board
    print("- - - - - - - - - -")
    for i in range(0, 8, 3):
        print("| ",board[i]," | ",board[i+1]," | ",board[i+2]," |")
        print("- - - - - - - - - -")

def makeMove(val):
    global board, lastMove
    if lastMove == "O":
        val = "X"
    elif lastMove == "X":
        val = "O"
    printBoard()
    while True:
        print("At which number would you like to place a ",val,"?")
        choice = int(input("Choice: "))
        if choice not in board:
            print("This is an invalid integer")
        elif choice in board and board[choice-1] != "X" or "O":
            board[choice-1] = val
            break
    while True:
        if val == "X":
            val == "O"
            break
        else:
            val == "X"
            break
    lastMove = val
    checkBoard()
    if checkWin() == "X":
        print("X Wins")
        return "X"
    elif checkWin() == "O":
        print("O Wins")
        return "O"

def checkWin():
    global board, wins
    for c in wins:
        placeOne = c[0]
        placeTwo = c[1]
        placeThree = c[2]
        if board[placeOne-1] == "X":
            if board[placeTwo-1] == "X":
                if board[placeThree-1] == "X":
                    return "X"
        elif board[placeOne-1] == "O":
            if board[placeTwo-1] == "O":
                if board[placeThree-1] == "O":
                    return "O"

def checkBoard():
    global board
    nonInts = 0
    for i in board:
        if i not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            nonInts += 1
    if nonInts == 9:
        print("This round is a draw")
        printBoard()
        sleep(1)
        e()
            
def main():
    global val, lastMove
    while True:
        if makeMove(val) == "X":
            print("Well Done To X")
            printBoard()
            sleep(1)
            e()
        elif makeMove(val) == "O":
            print("Well Done To O")
            printBoard()
            sleep(1)
            e()

if __name__ == "__main__":
    main()
