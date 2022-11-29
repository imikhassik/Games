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
        try:
            while ship.size:
                self.board[ship.x][ship.y] = '■'
                if ship.direction == 'v' and ship.size > 1:
                    ship.x += 1
                elif ship.direction == 'h' and ship.size > 1:
                    ship.y += 1
                elif ship.direction == 'd' and ship.size > 1:
                    ship.x += 1
                    ship.y += 1
                ship.size -= 1
            return True
        except IndexError:
            print("Координаты за пределами поля")
            return False


class Ship:
    def __init__(self, x=0, y=0, direction='h', size=3):
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size

    def get_coordinates(self):
        while True:
            try:
                if self.size > 1:
                    self.x, self.y, self.direction = input("Введите координаты и направление корабля: ").split()
                else:
                    self.x, self.y = input("Введите координаты корабля: ").split()
                self.x, self.y = map(int, (self.x, self.y))
                if self.x and self.y in range(1, 7) and self.direction in ('h', 'v', 'd'):
                    self.x -= 1
                    self.y -= 1
                    break
                elif self.direction not in ('h', 'v', 'd'):
                    print("Направление: h - по горизонтали, v - по вертикали, d - по диагонали")
                else:
                    print("Координаты за пределами поля")
            except ValueError:
                if self.size > 1:
                    print("Некорректные координаты. Пример корректного ввода: 2 1 h")
                else:
                    print("Некорректные координаты. Пример корректного ввода для корабля на одну клетку: 2 1")
                continue


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
    i = 0
    while i <= 6:
        ships[i] = Ship()
        ships[i].size = sizes[i]
        ships[i].get_coordinates()
        if user_board.place_ship(ships[i]):
            print_boards(user_board, ai_board)
            i += 1


instructions()
user_board = Board()
ai_board = Board()
print_boards(user_board, ai_board)
setup_ships()
