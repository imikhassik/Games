class Board:
    _board = [['O'] * 6 for i in range(6)]

    def get_board(self):
        print('  | 1 | 2 | 3 | 4 | 5 | 6 |\n')
        for index, row in enumerate(self._board):
            print(index + 1, end=' | ')
            for cell in row:
                print(cell, end=' | ')
            print()


user_board = Board()
user_board.get_board()
