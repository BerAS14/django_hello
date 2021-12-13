from pages.point import Point


class StateGameSnake(object):
    def __init__(self):
        self.field = []
        self.snake = []
        self.direction = ''
        self.game_started = False
        self.step_over = False
        self.game_over = False
        self.apple = Point(-1, -1)
        self.speed = 0

    def __repr__(self):
        return str(vars(self))
