class Board:
    _board_1 = [['O'] * 6 for i in range(6)]
    _board_2 = [['O'] * 6 for j in range(6)]

    def __init__(self, name):
        self.name = name

    def get_board(self):
        return self._board_1 if self.name == 'user' else self._board_2


def print_board(board_1, board_2):
    print('  | 1 | 2 | 3 | 4 | 5 | 6 |       | 1 | 2 | 3 | 4 | 5 | 6 |\n')
    for i in range(6):
        print(i + 1, end=' | ')
        for j in range(6):
            print(f"{board_1.get_board()[i][j]}", end=' | ')
        print(f'\t{i + 1}', end=' | ')
        for j in range(6):
            print(f"{board_2.get_board()[i][j]}", end=' | ')
        print('\n')


user_board = Board('user')
ai_board = Board('ai')
user_board._board_1[0][0] = 'x'
ai_board._board_2[1][1] = 'y'

print_board(user_board, ai_board)
