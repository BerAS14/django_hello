class StateGameSnake(object):
    def __init__(self):
        self.field = []
        self.snake = []
        self.direction = ''
        self.game_started = False
        self.step_over = False
        self.game_over = False

    def __repr__(self):
        return str(vars(self))
