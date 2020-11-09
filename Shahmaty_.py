WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Создаём шахматную доску
    board = Board()
    board.field[0][0] = Rook(WHITE)
    board.field[0][1] = Knight(WHITE)
    board.field[0][2] = Bishop(WHITE)
    board.field[0][3] = Queen(WHITE)
    board.field[0][4] = King(WHITE)
    board.field[0][5] = Bishop(WHITE)
    board.field[0][6] = Knight(WHITE)
    board.field[0][7] = Rook(WHITE)
    board.field[1][0] = Pawn(WHITE)
    board.field[1][1] = Pawn(WHITE)
    board.field[1][2] = Pawn(WHITE)
    board.field[1][3] = Pawn(WHITE)
    board.field[1][4] = Pawn(WHITE)
    board.field[1][5] = Pawn(WHITE)
    board.field[1][6] = Pawn(WHITE)
    board.field[1][7] = Pawn(WHITE)
    board.field[7][0] = Rook(BLACK)
    board.field[7][1] = Knight(BLACK)
    board.field[7][2] = Bishop(BLACK)
    board.field[7][3] = Queen(BLACK)
    board.field[7][4] = King(BLACK)
    board.field[7][5] = Bishop(BLACK)
    board.field[7][6] = Knight(BLACK)
    board.field[7][7] = Rook(BLACK)
    board.field[6][0] = Pawn(BLACK)
    board.field[6][1] = Pawn(BLACK)
    board.field[6][2] = Pawn(BLACK)
    board.field[6][3] = Pawn(BLACK)
    board.field[6][4] = Pawn(BLACK)
    board.field[6][5] = Pawn(BLACK)
    board.field[6][6] = Pawn(BLACK)
    board.field[6][7] = Pawn(BLACK)
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        piece = ['Pawn', 'Queen', 'Rook', 'King', 'Knight', 'Bishop']
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    Pawn, Queen, Rook, King, Knight, Bishop <row> <col> <row1> <col1>')
        print('    -- ход из клетки (row, col)                  в клетку (row1, col1)')
        print('    ')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
            print('Введите название фигуры или команду "Рокировка"')
        else:
            print('Ход черных:')
            print('Введите название фигуры или команду "Рокировка"')
        command = input()
        if command == 'exit':
            break
        if command in piece:
            print('Введите координаты фигуры и новые координаты')
            command = input()
            row, col, row1, col1 = command.split()
            row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
            if not (board.field[row][col] is None):
                if board.field[row][col].can_move(board, row, col, row1, col1) \
                        or board.field[row][col].can_attack(board,
                                                            row, col,
                                                            row1,
                                                            col1):
                    board.move_piece(row, col, row1, col1)
                    print('Ход успешен')
                else:
                    print('Координаты некорректы! Попробуйте другой ход!')
            else:
                print('Координаты некорректы! Попробуйте другой ход!')
        elif command == 'Рокировка':
            print('Введите номер столбца ладьи для рокировки')
            col = int(input())
            if col == 0:
                if Board.castling0(board):
                    print('Ход успешен')
                else:
                    print('Координаты некорректы! Попробуйте другой ход!')
            elif col == 7:
                if Board.castling7(board):
                    print('Ход успешен')
                else:
                    print('Координаты некорректы! Попробуйте другой ход!')
            else:
                print('Координаты некорректы! Попробуйте другой ход!')
        else:
            print('Команда некорректна! Попробуйте другой ход!')


class Pawn:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if not (correct_coords(row, col)) or not (correct_coords(row1, col1)):
            return False
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if board.get_piece(row1, col1) is None:
            if row + direction == row1:
                return True
        else:
            return False

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        if not (board.get_piece(row1, col1) is None):
            if board.get_piece(row1, col1).get_color() != self.color:
                return (row + direction == row1
                        and (col + 1 == col1 or col - 1 == col1))
            else:
                return False
        else:
            return False


class Rook:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку,
        # которая не лежит в том же ряду или столбце клеток.
        if not (correct_coords(row, col)) or not (correct_coords(row1, col1)):
            return False
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1 + step, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1 + step, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Knight:
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if not (correct_coords(row, col) or correct_coords(row1, col1)):
            return False
        elif (row + 2 == row1 or row - 2 == row1) and \
                (col + 1 == col1 or col - 1 == col1):
            if board.field[row1][col1] is not None:
                return False
            else:
                return True
        elif (row + 1 == row1 or row - 1 == row1) and \
                (col + 2 == col1 or col - 2 == col1):
            if board.field[row1][col1] is not None:
                return False
            else:
                return True
        elif row == row1 and col == col1:
            return False
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Bishop:
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if not (correct_coords(row, col)) or not (correct_coords(row1, col1)):
            return False
        elif -(row1 - row) == col1 - col:
            d = 0
            step = 1 if (row1 >= row) else -1
            for i in range(row + step, row1, step):
                d += 1
                if step == 1:
                    if not (board.get_piece(i, col - d) is None):
                        return False
                else:
                    if not (board.get_piece(i, col + d) is None):
                        return False
            return True
        elif row1 - row == col1 - col:
            return True
        elif -(row1 - row) == col1 - col:
            return True
        elif row == row1 and col == col1:
            return False
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Queen:
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        piece = board.get_piece(row1, col1)
        if not (piece is None) and piece.get_color() == self.color:
            return False
        if row1 - row == col1 - col:
            step = 1 if (row1 >= row) else -1
            d = 0
            for i in range(row + step, row1, step):
                d += 1
                if step == 1:
                    if not (board.get_piece(i, col + d) is None):
                        return False
                else:
                    if not (board.get_piece(i, col - d) is None):
                        return False
            return True
        elif -(row1 - row) == col1 - col:
            d = 0
            step = 1 if (row1 >= row) else -1
            for i in range(row + step, row1, step):
                d += 1
                if step == 1:
                    if not (board.get_piece(i, col - d) is None):
                        return False
                else:
                    if not (board.get_piece(i, col + d) is None):
                        return False
            return True
        elif row != row1 and col == col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                # Если на пути по вертикали есть фигура
                if not (board.get_piece(r, col) is None):
                    return False
            return True
        elif row == row1 and col != col1:
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                # Если на пути по горизонтали есть фигура
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        elif row == row1 and col == col1:
            return False
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King:
    def __init__(self, color):
        self.color = color

    def char(self):
        return 'K'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row < row1 and (0 <= row < 8 and 0 <= col < 8) and (
                0 <= row1 < 8 and 0 <= col1 < 8) and col < col1:
            for i in range(row, row1):
                for j in range(col, col1):
                    if board.field[i][j] is not None:
                        return False
        elif row > row1 and col < col1 and (0 <= row < 8 and 0 <= col < 8) and (
                0 <= row1 < 8 and 0 <= col1 < 8):
            for i in range(row, row1, -1):
                for j in range(col, col1):
                    if board.field[i][j] is not None:
                        return False
        elif row < row1 and col > col1 and (0 <= row < 8 and 0 <= col < 8) and (
                0 <= row1 < 8 and 0 <= col1 < 8):
            for i in range(row, row1):
                for j in range(col, col1, -1):
                    if board.field[i][j] is not None:
                        return False
        elif row > row1 and col > col1 and (0 <= row < 8 and 0 <= col < 8) and (
                0 <= row1 < 8 and 0 <= col1 < 8):
            for i in range(row, row1, -1):
                for j in range(col, col1, -1):
                    if board.field[i][j] is not None:
                        return False
        if (row != row1 and col != col1) and \
                (row + 1 != row1 and col + 1 != col1):
            return False
        elif row == row1 and (col + 1 == col1 or col - 1 == col1):
            return True
        elif col == col1 and (row + 1 == row1 or row - 1 == row1):
            return True
        elif (row + 1 == row1 or row - 1 == row1) and \
                (col + 1 == col1 or col - 1 == col1):
            return True
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.j = 0
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    # ... методы current_player_color и cell без изменений ...
    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def current_player_color(self):
        return self.color

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        if row == 0 and col == 0 and piece.char() == 'R':
            self.a += 1
        if row == 7 and col == 0 and piece.char() == 'R':
            self.b += 1
        if row == 0 and col == 7 and piece.char() == 'R':
            self.c += 1
        if row == 7 and col == 7 and piece.char() == 'R':
            self.d += 1
        if row == 0 and col == 4 and piece.char() == 'K':
            self.e += 1
        if row == 7 and col == 4 and piece.char() == 'K':
            self.j += 1
        self.field[row1][col1] = piece
        self.field[row][col] = None
        self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        piece = self.field[row][col]
        if piece is not None:
            if piece.char() == "P":
                if piece.can_move(self, row, col, row1, col1) or \
                        piece.can_attack(self, row, col, row1, col1):
                    if row1 == 7 or row1 == 0:
                        color = self.field[row][col].get_color()
                        if char == 'Q':
                            self.field[row1][col1] = Queen(color)
                            if self.field[row][col].char() == "P":
                                self.field[row][col] = None
                        elif char == 'R':
                            self.field[row1][col1] = Rook(color)
                            if self.field[row][col].char() == "P":
                                self.field[row][col] = None
                        elif char == 'B':
                            self.field[row1][col1] = Bishop(color)
                            if self.field[row][col].char() == "P":
                                self.field[row][col] = None
                        elif char == 'N':
                            self.field[row1][col1] = Knight(color)
                            if self.field[row][col].char() == "P":
                                self.field[row][col] = None
                        return True
                    return False
                return False
            return False
        return False

    def castling0(self):
        if not (self.field[0][0] is None):
            if self.a == 0 and self.e == 0:
                if self.field[0][0].char() == 'R':
                    if self.field[0][0].get_color() == self.color:
                        if self.field[0][0].can_move(self, 0, 0, 0, 3) \
                                and not (self.field[0][4] is None):
                            if self.field[0][4].char() == 'K':
                                self.field[0][3] = Rook(self.color)
                                self.field[0][0] = None
                                self.field[0][2] = King(self.color)
                                self.field[0][4] = None
                                return True
        if not (self.field[7][0] is None):
            if self.b == 0 and self.j == 0:
                if self.field[7][0].char() == 'R':
                    if self.field[7][0].get_color() == opponent(self.color):
                        if self.field[7][0].can_move(self, 7, 0, 7, 3) \
                                and not (self.field[7][4] is None):
                            if self.field[7][4].char() == 'K':
                                self.field[7][3] = Rook(opponent(self.color))
                                self.field[7][0] = None
                                self.field[7][2] = King(opponent(self.color))
                                self.field[7][4] = None
                                return True
                            return False
                        return False
                    return False
            return False
        else:
            return False

    def castling7(self):
        if not (self.field[0][7] is None):
            if self.c == 0 and self.e == 0:
                if self.field[0][7].char() == 'R' and \
                        self.field[0][7].get_color() == self.color:
                    if self.field[0][7].can_move(self, 0, 7, 0, 5) \
                            and not (self.field[0][4] is None):
                        if self.field[0][4].char() == 'K':
                            self.field[0][5] = Rook(opponent(self.color))
                            self.field[0][7] = None
                            self.field[0][6] = King(opponent(self.color))
                            self.field[0][4] = None
                            return True
        if not (self.field[7][7] is None):
            if self.d == 0 and self.j == 0:
                if self.field[7][7].char() == 'R' \
                        and self.field[7][7].get_color() == opponent(self.color):
                    if self.field[7][7].can_move(self, 7, 7, 7, 5) \
                            and not (self.field[7][4] is None):
                        if self.field[7][4].char() == 'K':
                            self.field[7][5] = Rook(opponent(self.color))
                            self.field[7][7] = None
                            self.field[7][6] = King(opponent(self.color))
                            self.field[7][4] = None
                            return True
                        return False
                    return False
            return False
        else:
            return False


from Shahmaty_ import (Board, Pawn, Rook, King, Knight, Bishop, Queen, WHITE, BLACK)

board = Board()
main()
print_board(board)
