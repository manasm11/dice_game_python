from my_template import *
from abc import ABCMeta, abstractmethod, abstractproperty
import random
board_length = 100
p_sym = "P"
c_sym = "C"


class IBoard(metaclass=ABCMeta):
    @abstractproperty
    def board(self):
        raise NotImplementedError

    @abstractmethod
    def set_position(self, symbol, increment):
        check_int(increment)
        check_str(symbol)

    @abstractmethod
    def get_position(self, symbol):
        check_str(symbol)


class Board(IBoard):
    _board = [
        "_"*board_length,
        "_"*board_length
    ]
    _symbols = {
        "computer": "C",
        "player": "P",
    }

    @property
    def board(self):
        # clear_screen()
        return self._board[0]+"\n"+self._board[1]+"\n\n"

    def set_position(self, symbol, increment):
        super().set_position(symbol, increment)
        check_in(symbol, self._symbols.values())
        board_index = self._symbols["computer"] == symbol
        final_index = self.get_index(board_index, symbol, increment)
        if final_index < board_length:
            self._board[board_index] = Board.get_board_string(
                symbol, final_index)

    def get_position(self, symbol):
        super().get_position(symbol)
        check_in(symbol, self._symbols.values())
        board_index = self._symbols["computer"] == symbol
        return self._board[board_index].find(symbol)+1

    def get_index(self, board_index, symbol, increment):
        check_int(board_index)
        check_int(increment)
        check_str(symbol)
        i = self._board[board_index].find(symbol)
        if i == -1:
            i = 0
        return i+increment

    @staticmethod
    def get_board_string(symbol, index):
        check_int(index)
        check_str(symbol)
        return "_"*(index) + symbol + "_"*(board_length-index-1)


if __name__ == "__main__":
    player_wins = False
    computer_wins = False
    b = Board()
    while(not player_wins and not computer_wins):
        print(b.board)
        input("Press enter to roll dice")
        p_dice = random.randint(1, 6)
        c_dice = random.randint(1, 6)
        print(f"Your dice gave:     {p_dice}")
        print(f"Computer dice gave: {c_dice}")
        b.set_position("P", p_dice)
        b.set_position("C", c_dice)

        player_wins = b.get_position("P") == board_length
        computer_wins = b.get_position("C") == board_length

    print(b.board)
    if player_wins:
        print("🎉🎉🎉PLAYER WINS !!!🎉🎉🎉")
    if computer_wins:
        print("🤖🤖🤖COMPUTER WINS !!!🤖🤖🤖")
    print("\n")
