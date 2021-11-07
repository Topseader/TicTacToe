import os
import re
import random

# todo: class Board:


def print_board(board):
    os.system('clear')
    for row in board: 
        print(''.join(row))        

def correct_row(row):
    if row == 0: return 1
    if row == 1: return 3
    if row == 2: return 5


def correct_col(col):
    if col == 0: return 2
    if col == 1: return 6
    if col == 2: return 10


def small_board(_board):
    board = [[],[],[]]
    for i in range(3):
        for j in range(3):
            board[i].append(_board[correct_row(i)][correct_col(j)])

    return board


# todo: refactor
def win(board):
    board = small_board(board)

    #rows
    if   board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != ' ':
        return True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != ' ':
        return True
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != ' ':
        return True

    #columns
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != ' ':
        return True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != ' ':
        return True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != ' ':
        return True

    #dioganals
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ':
        return True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' ':
        return True

    else:
        return False


def ai_move(board):
    board = small_board(board)
    cell = None
    while cell != ' ':
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        cell = board[row] [col]
        move = (correct_row(row), correct_col(col))
    return move


def human_move(board):
    print(f'You\'re an X player. Make your move')
    while True:
        move = re.findall(r'[0-2]', input())
        if len(move) == 2:
            move = (correct_row(int(move[0])), correct_col(int(move[1])))
            row = move[0]
            col = move[1]

            if board[row][col] == ' ':
                board[row][col] = 'X'
                return row, col
            else:
                print('This cell is occupied!')
        else:
            print('Invalid input!')

def game():
    EMPTY_BOARD = [
    list('┌───┬───┬───┐'),
    list('│   │   │   │'),
    list('├───┼───┼───┤'),
    list('│   │   │   │'),
    list('├───┼───┼───┤'),
    list('│   │   │   │'),
    list('└───┴───┴───┘')
]
    board = EMPTY_BOARD
    current_sym = 'O'
    moves_count = 0
    print_board(board)
    print('Welcome!')    

    #Main game loop
    while ((not win(board)) and moves_count < 9):        
        if current_sym == 'X':
            current_sym = 'O'
        else:
            current_sym = 'X'        

        if (current_sym == 'O'):
            move = ai_move(board)
        else:
            move = human_move(board)

        row = move[0]
        col = move[1]

        board[row][col] = current_sym

        print_board(board)

        moves_count += 1

    if win(board):
        print(f'The {current_sym} player won the game!')
    else:
        print('It\'s a tie!')


game()