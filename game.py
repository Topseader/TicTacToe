import os
import string
from player import HumanPlayer

class Game:
    def __init__(self, player_x, player_o, sym='X', board_size=3):
        self.player_x = player_x
        self.player_o = player_o
        self.sym = sym
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)]for _ in range(board_size)]


    def print_board(self, lst):
        os.system('clear')
        big_board = [None] * (self.board_size * 2)
        big_board[0] = '┌' + '───┬' * (self.board_size-1) + '───┐'

        for indx in range(1,len(big_board)):
            if indx % 2 == 0:
                big_board[indx] = '├' + '───┼' * (self.board_size-1) + '───┤'
            else:
                big_board[indx] = '│ '
                for i in range(self.board_size):
                    if len(lst[indx//2][i]) == 1:
                        big_board[indx] += lst[indx//2][i] + ' │ '
                    else:
                        big_board[indx] += lst[indx//2][i] + '│ '

        big_board.append('└' + '───┴' * (self.board_size-1) + '───┘')

        for i in big_board:
            print(i)


    def help(self):
        chars_list = list(string.ascii_uppercase[:self.board_size])
        help_board = [[' ' for _ in range(self.board_size)]for _ in range(self.board_size)]
        for row_num, row in enumerate(help_board):
            for col_num, el in enumerate(row):
                help_board[row_num][col_num] = f'{chars_list[row_num]}{col_num}'

        self.print_board(help_board)


    def get_move(self, player):
        sym, row, col = player.make_move()
        self.board[row][col] = sym

    
    def play(self):
        pass


def main():
    pl_x = HumanPlayer('X')
    pl_o = HumanPlayer('O')
    game = Game(pl_x, pl_o, 'X', 5)
    game.help()
    game.get_move(pl_x)
    game.print_board(game.board)



if __name__ == '__main__':
    main()

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