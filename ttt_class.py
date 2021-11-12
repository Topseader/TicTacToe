import os
#import re
#import random

class Board:

    def __init__(self, size=3, win_size=3):
        self.size = size
        self.small_board = [[' ' for i in range(size)] for i in range(size)]
        self.win_size = win_size


    def print_board(self):
        os.system('clear')
        # can be replaced with self.size << 1
        big_board = ['None'] * (self.size*2)
        big_board[0] = '┌' + '───┬' * (self.size-1) + '───┐'

        for index in range(1,len(big_board)):
            if index % 2 == 0:
                big_board[index] = '├' + '───┼' * (self.size-1) + '───┤'
            else:                
                big_board[index] = '│ '
                for i in range(self.size):
                    big_board[index] += self.small_board[index//2][i] + ' │ '

        big_board.append('└' + '───┴' * (self.size-1) + '───┘')

        for i in big_board:
            print(i)


    def get_move(self, sym: str, row: int, col: int):
        try:
            self.small_board[row][col]
        except IndexError:
            print('Invalid input!')
            return False
        
        if self.small_board[row][col] == ' ':
            self.small_board[row][col] = sym
            return True
        else:
            print('Cell is occupied!')
            return False


class Player:
    def __init__(self, sym, is_human=True)
        self.sym = sym
        self.is_human = is_human



test = Board(4)
test.get_move('x',2,1)
test.print_board()

'''
    EMPTY_BOARD = [list('┌───┬───┬───┐'),
                   list('│   │   │   │'),
                   list('├───┼───┼───┤'),
                   list('│   │   │   │'),
                   list('├───┼───┼───┤'),
                   list('│   │   │   │'),
                   list('└───┴───┴───┘')
                  
                  ]
'''                  