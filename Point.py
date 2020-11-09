class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        super().__init__(name, x, y)

    def get_color(self):
        return self.color

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x,
                            (255 - self.color[0], 255 - self.color[1], 255 - self.color[2]))
