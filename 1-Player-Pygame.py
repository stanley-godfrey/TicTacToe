import pygame
import sys
import random
import time


# <editor-fold desc="Setup">
pygame.init()
pygame.mixer.quit()
pygame.mixer.init()

board_length = 3
board_width = 3

width = 50  # programming technique - variable assignment; data type - integer
height = 50  # programming technique - variable assignment; data type - integer
margin = 5  # programming technique - variable assignment; data type - integer

clock = pygame.time.Clock()
FPS = 60
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = (board_length * width) + ((board_length + 1) * margin),\
                                         (board_width * height) + ((board_width + 1) * margin)
screen = pygame.display.set_mode(SCREENSIZE)

off_white = (220, 220, 220)  # programming technique - variable assignment; data type - tuple
black = (0, 0, 0)
blue = (0, 0, 255)  # programming technique - variable assignment; data type - tuple
green = (0, 255, 0)  # programming technique - variable assignment; data type - tuple

gameState = "running"  # programming technique - variable assignment; data type - string
gamePlayer = 'X'  # programming technique - variable assignment; data type - string

board = []  # programming technique - variable assignment; data structure - list
square = " "  # programming technique - variable assignment; data type - string
wins = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

theme = pygame.mixer.music.load('Resources/bensound-buddy.mp3')
pygame.mixer.music.play(-1)
# </editor-fold>


def generate_board(square_cell, x, y):
    board_comp = [[square_cell for x in range(x)] for y in range(y)]
    return board_comp


def print_board(board):
    print('-------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell + '|', end='')
        print()
        print('-------')


def check_win(board):
    state = None
    for win in wins:
        state = board[win[0][0]][win[0][1]]
        if board[win[1][0]][win[1][1]] == state and board[win[2][0]][win[2][1]] == state and state != ' ':
            print('Win', state)
            print_board(board)
            return 'done'


def check_full(board):
    full = 0
    for row in board:
        for cell in row:
            if cell != ' ':
                full += 1
    if full == 9:
        print('Full')
        print_board(board)
        return 'full'


def generate_move(board):
    found = False
    while not found:
        move_x = random.choice(range(0, 3))
        move_y = random.choice(range(0, 3))
        if board[move_x][move_y] == ' ':
            found = True
    return move_x, move_y


board = generate_board(square, board_length, board_width)

start_time = time.time()

screen.fill(black)

# <editor-fold desc="Main Loop">
while gameState != "exit":

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = "exit"
        elif event.type == pygame.MOUSEBUTTONDOWN:  # programming technique - conditional elif
            mouse_pos = pygame.mouse.get_pos()
            mouse_col = mouse_pos[0] // (width + margin)  # programming technique - integer division
            mouse_row = mouse_pos[1] // (height + margin)  # programming technique - integer division
            if board[mouse_row][mouse_col] == ' ':
                board[mouse_row][mouse_col] = gamePlayer  # programming technique - two-dimensional arrays
                if check_full(board) != 'full':
                    x, y = generate_move(board)
                    board[x][y] = 'O'

    for row in range(0, board_length):  # programming technique - for loop
        for column in range(0, board_width):  # programming technique - for loop
            if board[row][column] == 'X':
                color = green
            elif board[row][column] == 'O':
                color = blue
            else:
                color = off_white  # programming technique - variable assignment
            pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin,
                                             width, height])  # programming technique - pygame rectangle

    if check_full(board) == 'full':
        board = generate_board(square, board_length, board_width)
        start_time = time.time()

    pygame.display.flip()

    win = check_win(board)
    if win == 'done':
        finish_time = time.time()
        time_taken = finish_time - start_time
        print('Time Taken: %s' % ('{0:.2f}'.format(time_taken)), end=' ')
        print('seconds')
        board = generate_board(square, board_length, board_width)
        start_time = time.time()

    clock.tick(FPS)
# </editor-fold>

pygame.mixer.music.stop()
pygame.quit()
sys.exit()
