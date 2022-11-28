class Board:
    def __init__(self):
        self.board = [['O'] * 6 for _ in range(6)]

    def get_board(self):
        return self.board

    def place_ship(self, ship):
        while ship.size:
            self.board[ship.x][ship.y] = '■'
            if ship.direction == 'v':
                ship.x += 1
            elif ship.direction == 'h':
                ship.y += 1
            elif ship.direction == 'd':
                ship.x += 1
                ship.y += 1
            ship.size -= 1


class Ship:
    def __init__(self, direction='h', size=3, x=0, y=0):
        self.direction = direction
        self.size = size
        self.x = x
        self.y = y

    # def get_coordinates(self):
    #     self.x, self.y = input("Введите началь")


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

# def setup_ships():
#     user_ship_1


def instructions():
    print("-------------------------------------------------")
    print("                  МОРСКОЙ БОЙ                    ")
    print("-------------------------------------------------")
    print("   Введите координаты, чтобы расположить корабли:")
    print("   1 корабль на 3 клетки, 2 на две, 4 на одну.   ")
    print("   Достаточно указать первую клетку и направление")
    print("   Например: 1 1 d расположит корабль от левой   ")
    print("   верхней клетки по диагонали.                  ")
    print("   Направления: h - по горизонтали, v - по верти-")
    print("   кали, d - по диагонали                              ")
    print("-------------------------------------------------")


instructions()
user_board = Board()
ai_board = Board()
user_ship_1 = Ship('d', 3, 0, 0)
user_ship_2 = Ship('h', 2, 4, 4)
user_board.place_ship(user_ship_1)
user_board.place_ship(user_ship_2)
print_boards(user_board, ai_board)
