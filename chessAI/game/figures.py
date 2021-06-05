class Figure:

    def __init__(self, color, x, y, name):
        self.color = color
        self.x = x
        self.y = y
        self.name = name

    def get_color(self):
        return self.color

    def get_position(self):
        position_tuple = (self.x, self.y)
        return position_tuple

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.name


class Pawn(Figure):

    def __init__(self, color, x, y, name):
        super().__init__(color, x, y, name)

    def __eq__(self, other):
        if isinstance(other, Pawn):
            return self.x == other.x & self.y == other.y
        return False


class Rook(Figure):

    def __init__(self, color, x, y, name):
        super().__init__(color, x, y, name)

    def __eq__(self, other):
        if isinstance(other, Rook):
            return self.x == other.x & self.y == other.y
        return False


class Knight(Figure):

    def __init__(self, color, x, y, name):
        super().__init__(color, x, y, name)

    def __eq__(self, other):
        if isinstance(other, Knight):
            return self.x == other.x & self.y == other.y
        return False


class Bishop(Figure):

    def __init__(self, color, x, y, name):
        super().__init__(color, x, y, name)

    def __eq__(self, other):
        if isinstance(other, Bishop):
            return self.x == other.x & self.y == other.y
        return False


class Queen(Figure):

    def __init__(self, color, x, y, name):
        super().__init__(color, x, y, name)

    def __eq__(self, other):
        if isinstance(other, Queen):
            return self.x == other.x & self.y == other.y
        return False


class King(Figure):

    def __init__(self, color, x, y, name):
        super().__init__(color, x, y, name)

    def __eq__(self, other):
        if isinstance(other, King):
            return self.x == other.x & self.y == other.y
        return False
