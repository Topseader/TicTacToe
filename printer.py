import os
import string
import platform

class ConsolePrinter:
    def __init__(self, board_size):
        self.board_size = board_size
        if platform.system() == 'Windows':
            self.clear = 'cls'
        else:
            self.clear = 'clear'

    def print_board(self, lst):
        os.system(self.clear)

        big_board = [None] * ((self.board_size * 2) + 1)

        big_board[0] = ['    ']
        for i in range(self.board_size):
            if i < 10:
                big_board[0].append(str(i) + '   ')
            else:
                big_board[0].append(str(i) + '  ')

        big_board[0] = ''.join(big_board[0])
        big_board[1] = '  ┌' + '───┬' * (self.board_size-1) + '───┐'

        chars_list = list(string.ascii_uppercase[:self.board_size])

        for indx in range(2,len(big_board)):
            if indx % 2 != 0:
                big_board[indx] = '  ├' + '───┼' * (self.board_size-1) + '───┤'
            else:
                big_board[indx] = str(chars_list[indx//2-1]) + ' │'
                for i in range(self.board_size):
                    big_board[indx] += lst[indx//2-1][i] + '│'

        big_board.append('  └' + '───┴' * (self.board_size-1) + '───┘')

        for i in big_board:
            print(i)

    def help(self):
        chars_list = list(string.ascii_uppercase[:self.board_size])
        help_board = [[' ' for _ in range(self.board_size)]for _ in range(self.board_size)]
        for row_num, row in enumerate(help_board):
            for col_num, el in enumerate(row):
                if col_num < 10:
                    help_board[row_num][col_num] = f'{chars_list[row_num]}{col_num} '
                else:
                    help_board[row_num][col_num] = f'{chars_list[row_num]}{col_num}'

        self.print_board(help_board)
