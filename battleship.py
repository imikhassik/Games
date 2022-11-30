def instructions():
    print("-------------------------------------------------")
    print("                  МОРСКОЙ БОЙ                    ")
    print("-------------------------------------------------")
    print("   Введите координаты, чтобы расположить корабли:")
    print("   1 корабль на 3 клетки, 2 на две, 4 на одну.   ")
    print("   Достаточно указать первую клетку и направление")
    print("   Например: 1 1 v расположит корабль от левой   ")
    print("   верхней клетки по вертикали.                  ")
    print("   Направления:                                  ")
    print("   h - по горизонтали, v - по вертикали          ")
    print("-------------------------------------------------")


class Board:
    def __init__(self):
        self.board = [['O'] * 6 for _ in range(6)]

    def get_board(self):
        return self.board

    def place_ship(self, ship):
        try:
            while ship.size:
                if ship.radar():
                    self.board[ship.x][ship.y] = '*'
                    if ship.direction == 'v' and ship.size > 1:
                        ship.x += 1
                    elif ship.direction == 'h' and ship.size > 1:
                        ship.y += 1
                    ship.size -= 1
                else:
                    return False
            return True
        except IndexError:
            print("Координаты за пределами поля")
            return False

    def confirm_placement(self, flag):
        if flag:
            for row in range(6):
                for column in range(6):
                    if self.get_board()[row][column] == '*':
                        self.get_board()[row][column] = '■'
        else:
            for row in range(6):
                for column in range(6):
                    if self.get_board()[row][column] == '*':
                        self.get_board()[row][column] = 'O'

    def print_boards(self, other=None):
        if other:
            print('  | 1 | 2 | 3 | 4 | 5 | 6 |       | 1 | 2 | 3 | 4 | 5 | 6 |\n')
            for i in range(6):
                print(i + 1, end=' | ')
                for j in range(6):
                    print(f"{self.board[i][j]}", end=' | ')
                print(f'\t{i + 1}', end=' | ')
                for j in range(6):
                    print(f"{other.get_board()[i][j]}", end=' | ')
                print('\n')
        else:
            print('  | 1 | 2 | 3 | 4 | 5 | 6 |\n')
            for i in range(6):
                print(i + 1, end=' | ')
                for j in range(6):
                    print(f"{self.board[i][j]}", end=' | ')
                print('\n')


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
                if self.x in range(1, 7) and self.y in range(1, 7) and self.direction in ('h', 'v'):
                    self.x -= 1
                    self.y -= 1
                    break
                elif self.direction not in ('h', 'v'):
                    print("Направление: h - по горизонтали, v - по вертикали")
                else:
                    print("Координаты за пределами поля")
            except ValueError:
                if self.size > 1:
                    print("Некорректные координаты. Пример корректного ввода: 2 1 h")
                else:
                    print("Некорректные координаты. Пример корректного ввода для корабля на одну клетку: 2 1")
                continue

    def radar(self):
        search_area = user_board.get_board().copy()
        if 0 < self.x < 5 and 0 < self.y < 5:
            search_area = [row[self.y-1:self.y+2] for row in search_area[self.x-1:self.x+2]]
        elif self.x == 0 and self.y == 0:
            search_area = [row[self.y:self.y+2] for row in search_area[self.x:self.x+2]]
        elif self.x == 5 and self.y == 0:
            search_area = [row[self.y:self.y+2] for row in search_area[self.x-1:self.x+1]]
        elif self.x == 0 and self.y == 5:
            search_area = [row[self.y-1:self.y+1] for row in search_area[self.x:self.x+2]]
        elif self.x == 5 and self.y == 5:
            search_area = [row[self.y-1:self.y+1] for row in search_area[self.x-1:self.x+1]]
        elif self.x == 0:
            search_area = [row[self.y-1:self.y+2] for row in search_area[self.x:self.x+2]]
        elif self.x == 5:
            search_area = [row[self.y-1:self.y+2] for row in search_area[self.x-1:self.x+1]]
        elif self.y == 0:
            search_area = [row[self.y:self.y+2] for row in search_area[self.x-1:self.x+2]]
        elif self.y == 5:
            search_area = [row[self.y-1:self.y+1] for row in search_area[self.x-1:self.x+2]]

        for row in search_area:
            if '■' in row:
                print("Другой корабль слишком близко")
                return False
        else:
            return True

    @staticmethod
    def setup_ships():
        ships = {}
        sizes = [3, 2, 2, 1, 1, 1, 1]
        i = 0
        while i <= 6:
            ships[i] = Ship()
            ships[i].size = sizes[i]
            ships[i].get_coordinates()
            if user_board.place_ship(ships[i]):
                user_board.confirm_placement(1)
                user_board.print_boards()
                i += 1
            else:
                user_board.confirm_placement(0)
                continue


instructions()
user_board = Board()
ai_board = Board()
user_board.print_boards()
Ship.setup_ships()
