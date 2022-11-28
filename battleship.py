class Board:

    def __init__(self):
        self.board = [['O'] * 6 for i in range(6)]

    def get_board(self):
        return self.board


def print_boards(board_1, board_2):
    print('  | 1 | 2 | 3 | 4 | 5 | 6 |       | 1 | 2 | 3 | 4 | 5 | 6 |\n')
    for i in range(6):
        print(i + 1, end=' | ')
        for j in range(6):
            print(f"{board_1.get_board()[i][j]}", end=' | ')
        print(f'\t{i + 1}', end=' | ')
        for j in range(6):
            print(f"{board_2.get_board()[i][j]}", end=' | ')
        print('\n')


user_board = Board()
ai_board = Board()
print_boards(user_board, ai_board)