#from abc import ABC, abstractmethod

class HumanPlayer:
    def __init__(self, sym):
        self.sym = sym
        self.ai = False


    def make_move(self):
        raw_str = input()
        try:
            row = self.correct_row(raw_str[0])
            col = int(raw_str[1])
        except ValueError: # ???
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