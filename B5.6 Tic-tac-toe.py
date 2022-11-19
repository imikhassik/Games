board = [
    [' ', '0', '1', '2'],
    ['0', '-', '-', '-'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-']
]


def print_board(t, x=0, y=0):
    # Принимает символ на замену '-' и координаты
    # Распечатывает поле
    if t == 'x':
        board[x][y] = 'x'
    elif t == 'o':
        board[x][y] = 'o'

    for i in board:
        for j in i:
            print('%3s' % j, end='')
        print()


def get_coordinates():
    # Запрашивает ввод у пользователя и превращает ввод в координаты
    # Если ввод вне диапазона 0-2, запрашивает ввод бесконечно
    # Если ввод не из 2-х чисел, запрашивает два числа
    x, y = ' ', ' '
    while x not in "012" or y not in "012":
        try:
            x, y = input("Введите ряд и колонку через пробел в диапазоне от 0 до 2: ").split()
        except ValueError:
            print("Введите два числа")
            continue
    return int(x)+1, int(y)+1


def not_available(x, y):
    # Проверяет, можно ли ввести значение или уже занято
    if board[x][y] == '-':
        return False
    else:
        print("Занято")
        return True


def winner():
    # Сравнивает символы в рядах, колонках и по диагоналям, отсеивает '-'
    for row in board[1:]:
        if (row[1] == row[2] == row[3]) and '-' not in row:
            return True
    for col in range(1, 4):
        if board[1][col] == board[2][col] == board[3][col] and board[1][col] != '-':
            return True
    if board[1][1] == board[2][2] == board[3][3] and board[2][2] != '-':
        return True
    if board[1][3] == board[2][2] == board[3][1] and board[2][2] != '-':
        return True


def draw():
    # Возвращает True, когда все ячейки заполнены символами кроме '-'
    for row in board[1:]:
        for column in row[1:]:
            if column == '-':
                return False
    return True


turn = 'o'
print_board('', 0, 0)

while True:
    turn = 'x' if turn == 'o' else 'o'
    print(f"Очередь {turn}")
    row, column = get_coordinates()
    if not_available(row, column):
        turn = 'x' if turn == 'o' else 'o'
        continue
    print_board(turn, row, column)
    if draw():
        print('Ничья')
        break
    elif winner():
        print(f'{turn} выиграл!')
        break
