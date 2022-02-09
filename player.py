#from abc import ABC, abstractmethod

class HumanPlayer:
    def __init__(self, sym):
        self.sym = sym
        self.ai = False


    def make_move(self):
        raw_str = input()
        if raw_str[0] in list('0123456789'):
            print('Invalid input! Use letters to determine targeted row.')
            self.make_move()
        try:
            row = self.correct_row(raw_str[0])
            col = int(raw_str[1:3])
        except ValueError:
            print('Invalid input!')
            self.make_move()

        return (self.sym, row, col)


    @staticmethod
    def correct_row(char):      # "B3" => row=2; col=3
        row = ord(char.upper())
        row -= 65               # 'a' => 0
        return row








class AIPlayer:
    def __init__(self, sym):
        self.sym = sym
        self.ai = True

    def make_move(self):
        """MAKE SOMETHING"""

        return (self.sym, row, col)