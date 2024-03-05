import random

class Board:
    def __init__(self):
        self.board = [[0]*10 for _ in range(10)]

    def shot(self, dot):
        x, y = dot
        if self.board[x][y] == 1:
            self.board[x][y] = "X"
            print("Попадание!")
        else:
            self.board[x][y] = "-"
            print("Мимо!")

class BoardException(Exception):
    pass

class DotException(BoardException):
    def __init__(self, dot):
        self.dot = dot

    def __str__(self):
        return f"Ошибка! Некорректные координаты точки {self.dot}."

class OutsideBoardException(BoardException):
    def __init__(self, dot):
        self.dot = dot

    def __str__(self):
        return f"Ошибка! Точка {self.dot} выходит за пределы доски."

class OccupiedDotException(BoardException):
    def __init__(self, dot):
        self.dot = dot

    def __str__(self):
        return f"Ошибка! Точка {self.dot} уже занята."

class Ship:
    def __init__(self, length, start_dot, end_dot):
        self.length = length
        self.start_dot = start_dot
        self.end_dot = end_dot
        self.coordinates = []

        if start_dot[0] != end_dot[0] and start_dot[1] != end_dot[1]:
            raise DotException(start_dot)

        if start_dot[0] > end_dot[0] or start_dot[1] > end_dot[1]:
            raise DotException(start_dot)

        if self.length == 1:
            self.coordinates.append(start_dot)
        elif start_dot[0] == end_dot[0]:
            for y in range(start_dot[1], end_dot[1] + 1):
                self.coordinates.append((start_dot[0], y))
        elif start_dot[1] == end_dot[1]:
            for x in range(start_dot[0], end_dot[0] + 1):
                self.coordinates.append((x, start_dot[1]))

class Player:
    def __init__(self):
        self.board = Board()
        self.enemy_board = Board()

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                x, y = map(int, input("Введите координаты выстрела (через пробел): ").split())
                dot = (x, y)
                self.enemy_board.shot(dot)
                break
            except Exception as e:
                print(e)

    def place_ships(self):
        for length in range(1, 5):
            for _ in range(5 - length):
                while True:
                    try:
                        print(f"Разместите корабль длиной {length}:")
                        x1, y1 = map(int, input("Введите координаты начальной точки (через пробел): ").split())
                        x2, y2 = map(int, input("Введите координаты конечной точки (через пробел): ").split())
                        start_dot = (x1, y1)
                        end_dot = (x2, y2)
                        ship = Ship(length, start_dot, end_dot)
                        for dot in ship.coordinates:
                            if self.board.board[dot[0]][dot[1]] == 1:
                                raise OccupiedDotException(dot)
                            self.board.board[dot[0]][dot[1]] = 1
                        break
                    except Exception as e:
                        print(e)

    def play(self):
        print("Расстановка кораблей:")
        self.place_ships()
        print("Игра началась!")
        while True:
            self.move()


player = Player()
player.play()