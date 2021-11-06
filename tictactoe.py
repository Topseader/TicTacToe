import os

EMPTY_BOARD = [
list('┌───┬───┬───┐'),
list('│   │   │   │'),
list('├───┼───┼───┤'),
list('│   │   │   │'),
list('├───┼───┼───┤'),
list('│   │   │   │'),
list('└───┴───┴───┘')
]

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


def insert_on_board(board, row, col, sym): #pass corrected adresses
    board[row][col] = sym
    return board

def cell_empty(row, col):
    return board[row][col] == ' '

# todo: refactor
def win(_board):
    board = [[],[],[]]
    for i in range(3):
        for j in range(3):
            board[i].append(_board[correct_row(i)][correct_col(j)])

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

def game():    
    board = EMPTY_BOARD
    current_sym = '0'
    print_board(board)
    print('Welcome!')
    

    #Main game loop
    while(not win(board)):
        if current_sym == 'X':
            current_sym = 'O'
        else:
            current_sym = 'X'
        print(f'You\'re an {current_sym} player. Make your move')
        # todo: improve with re
        move = input()
        move = (correct_row(int(move[0])), correct_col(int(move[1])))
        row = move[0]
        col = move[1]
        
        if board[move[0]] [move[1]] == ' ':
            board = insert_on_board(board, row, col, current_sym)        

        print_board(board)

    print(f'The {current_sym} player won the game!')


game()

'''
print_board(insert_on_board(EMPTY_BOARD,
                            correct_row(0), 
                            correct_col(0), 
                            'X'))
'''
