import hashlib

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, coord2):
        return Coord(self.x + coord2.x, self.y + coord2.y)

    def subtract(self, coord2):
        return Coord(self.x - coord2.x, self.y - coord2.y)

    def scalar_multiply(self, multiplier):
        return Coord(self.x * multiplier, self.y * multiplier)

    def invert(self):
        return Coord(-self.x, -self.y)

    def __eq__(self, other):
        if not isinstance(other, Coord):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()
