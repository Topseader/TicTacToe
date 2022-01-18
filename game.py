import os
import string
from player import HumanPlayer

class Game:
    def __init__(self, player_x, player_o, sym=' X ', board_size=3):
        self.player_x = player_x
        self.player_o = player_o
        self.sym = sym
        self.board_size = board_size
        self.last_move = []

        if self.board_size < 5:
            self.win_len = self.board_size
        else:
            self.win_len = 5

        self.board = [['   ' for _ in range(board_size)]for _ in range(board_size)]

    #TODO: Printer class
    def print_board(self, lst):
        os.system('clear')
        big_board = [None] * (self.board_size * 2)
        big_board[0] = '┌' + '───┬' * (self.board_size-1) + '───┐'

        for indx in range(1,len(big_board)):
            if indx % 2 == 0:
                big_board[indx] = '├' + '───┼' * (self.board_size-1) + '───┤'
            else:
                big_board[indx] = '│'
                for i in range(self.board_size):
                    big_board[indx] += lst[indx//2][i] + '│'

        big_board.append('└' + '───┴' * (self.board_size-1) + '───┘')

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

    def check_move(self, player):
        while True:
            sym, row, col = player.make_move()
            self.last_move = sym, row, col
            
            try:
                self.board[row][col] != '   '
            except ValueError:
                print('Totally invalid input!')
                continue
            except IndexError:
                print('Invalid input!')
                continue


            if self.board[row][col] != '   ':
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
        for col_num in range(self.board_size - self.win_len):
            if all(self.board[row][col_num + i] == sym for i in range(self.win_len)):
                return True

        #columns
        for row_num in range(self.board_size - self.win_len):
            if all(self.board[row_num + i][col] == sym for i in range(self.win_len)):
                return True

        #diagonals
        offset = 0

        #top-left to bottom-right
        if row <= col:            
            while col - row + self.win_len + offset - 1 <= self.board_size:
                if all(self.board[i+offset][col-row+i+offset] == sym for i in range(self.win_len)):
                    return True
                offset += 1
        else:
            while row - col + self.win_len + offset - 1 <= self.board_size:
                if all(self.board[row-col+i+offset][i+offset] == sym for i in range(self.win_len)):
                    return True
                offset += 1

        #top-right to bottom-left
        offset = 0

        #above the middle lane 
        if row + col <= self.board_size - 1:            
            while row + col - offset >= self.win_len - 1:
                if all(self.board[i+offset][row+col-i-offset] == sym for i in range(self.win_len)):
                    return True
                offset += 1

        #below the middle lane
        # NOT DONE!
        else:            
            while row + col + offset <= self.board_size*2 - self.win_len:
                print(all(self.board[row+col-1-self.board_size+i+offset][self.board_size-1-i-offset] == sym for i in range(self.win_len)))
                if all(self.board[row+col-1-self.board_size+i+offset][self.board_size-1-i-offset] == sym for i in range(self.win_len)):
                    return True
                offset += 1
        
        
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
    pl_x = HumanPlayer(' X ')
    pl_o = HumanPlayer(' O ')
    game = Game(pl_x, pl_o, ' X ', 13)
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