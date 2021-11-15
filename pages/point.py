class Point(object):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return str(vars(self))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented
