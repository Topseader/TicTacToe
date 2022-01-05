import os
import string
from player import HumanPlayer

class Game:
    def __init__(self, player_x, player_o, sym='X', board_size=3):
        self.player_x = player_x
        self.player_o = player_o
        self.sym = sym
        self.board_size = board_size
        self.last_move = []

        if self.board_size < 5:
            self.win_len = self.board_size
        else:
            self.win_len = 5

        self.board = [[' ' for _ in range(board_size)]for _ in range(board_size)]

    #TODO: Printer class
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

    def check_move(self, player):
        while True:
            sym, row, col = player.make_move()
            self.last_move = sym, row, col
            
            try:
                self.board[row][col] != ' '
            except ValueError:
                print('Totally invalid input!')      
                continue
            except IndexError:
                print('Invalid input!')
                continue


            if self.board[row][col] != ' ':
                print('Cell is occupied!')
                continue
            else:
                break

        return True


    def get_move(self, player):
        if player.ai == False:
            if self.check_move(player):
                sym, row, col = self.last_move
        else:
            sym, row, col = self.last_move
        
        self.board[row][col] = sym


    def is_win(self):
        sym, row, col = self.last_move
        
        #rows
        if all(elem == sym for elem in self.board[row]):
            return True

        #columns
        entire_col = []
        for i in range(self.board_size):
            entire_col.append(self.board[i][col])

        if all(elem == sym for elem in entire_col):
            return True

        return False




    def play(self):
        self.help()
        for n_turns in range(self.board_size ** 2):
            self.get_move(self.player_x)
            self.print_board(self.board)
            if self.is_win():
                print('X player is win')
                break

            print('O player\'s turn')
            self.get_move(self.player_o)
            self.print_board(self.board)
            if self.is_win():
                print('O player is win')
                break
            print('X player\'s turn')


def main():
    pl_x = HumanPlayer('X')
    pl_o = HumanPlayer('O')
    game = Game(pl_x, pl_o, 'X', 6)
    game.play()




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