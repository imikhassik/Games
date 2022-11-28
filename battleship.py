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
    print("   кали, d - по диагонали                        ")
    print("-------------------------------------------------")


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
    def __init__(self, x=0, y=0, direction='h', size=3):
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size

    def get_coordinates(self):
        self.x, self.y, self.direction = input("Введите координаты корабля: ").split()
        self.x, self.y = map(int, (self.x, self.y))
        self.x -= 1
        self.y -= 1


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


def setup_ships():
    ships = {}
    sizes = [3, 2, 2, 1, 1, 1, 1]
    for i, size in enumerate(sizes):
        ships[i] = Ship()
        ships[i].size = size
        ships[i].get_coordinates()
        user_board.place_ship(ships[i])
        print_boards(user_board, ai_board)


instructions()
user_board = Board()
ai_board = Board()
print_boards(user_board, ai_board)
setup_ships()
