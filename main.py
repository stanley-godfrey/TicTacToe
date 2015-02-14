from sys import exit
from time import sleep

board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9]

def printBoard():
    global board
    print("- - - - - - - - - -")
    for i in range(0, 8, 3):
        print("| ",board[i]," | ",board[i+1]," | ",board[i+2]," |")
        print("- - - - - - - - - -")

def makeMove(val):
    global board
    printBoard()
    while True:
        print("At which number would you like to place a ",val,"?")
        choice = int(input("Choice: "))
        if choice not in board:
            print("This is an invalid integer")
        elif choice in board and board[choice-1] != "X" or "O":
            board[choice-1] = val
            break
    if checkWin() == "X":
        print("X Wins")
        return "X"
    elif checkWin() == "O":
        print("O Wins")
        return "O"

def checkWin():
    global board
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
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

def main():
    while True:
        if makeMove("X") == "X":
            print("Well Done To X")
            sleep(1)
            exit()
        elif makeMove("X") == "O":
            print("Well Done To O")
            sleep(1)
            exit()

if __name__ == "__main__":
    main()
