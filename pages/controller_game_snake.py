from random import randint

from .state_game_snake import StateGameSnake
from .point import Point


class ControllerGameSnake(object):
    def __init__(self):
        self.state = StateGameSnake()
        self.state.field = [24, 18, 'white']
        self.length_snake = 5
        self.acceleration = 10

    def __repr__(self):
        return str(vars(self))

    def get_center(self):
        x_center = round(self.state.field[0] / 2)
        y_center = round(self.state.field[1] / 2)
        return x_center, y_center

    def start_pause_new_game(self):
        if self.state.game_over:
            self.game_init()
            self.state.game_started = True
        if not self.state.game_started:
            self.state.game_started = True
        else:
            self.state.game_started = False

    def do_step(self):
        if not self.state.game_started or self.state.game_over:
            return
        if self.state.direction == 'Up':
            head_point = Point(self.head_x, self.head_y + 1)
            self.check_state_game(head_point)
        if self.state.direction == 'Down':
            head_point = Point(self.head_x, self.head_y - 1)
            self.check_state_game(head_point)
        if self.state.direction == 'Left':
            head_point = Point(self.head_x - 1, self.head_y)
            self.check_state_game(head_point)
        if self.state.direction == 'Right':
            head_point = Point(self.head_x + 1, self.head_y)
            self.check_state_game(head_point)
        self.state.step_over = True

    def game_init(self):
        self.state.speed = 600
        self.state.apple = Point(randint(0, self.state.field[0]-1), randint(1, self.state.field[1]))
        snake_head_x, snake_head_y = self.get_center()
        self.state.snake = []
        for i in range(self.length_snake):
            self.state.snake.append(Point(snake_head_x - i, snake_head_y))
        self.state.direction = 'Right'
        self.state.step_over = False
        self.state.game_over = False

    def go_up(self):
        if self.state.direction == 'Down' or not self.state.step_over:
            return
        self.state.direction = 'Up'
        self.state.step_over = False

    def go_down(self):
        if self.state.direction == 'Up' or not self.state.step_over:
            return
        self.state.direction = 'Down'
        self.state.step_over = False

    def go_left(self):
        if self.state.direction == 'Right' or not self.state.step_over:
            return
        self.state.direction = 'Left'
        self.state.step_over = False

    def go_right(self):
        if self.state.direction == 'Left' or not self.state.step_over:
            return
        self.state.direction = 'Right'
        self.state.step_over = False

    @property
    def head_x(self):
        return self.state.snake[0].x

    @property
    def head_y(self):
        return self.state.snake[0].y

    @property
    def state_width(self):
        return self.state.field[0]

    @property
    def state_height(self):
        return self.state.field[1]

    def check_game_over(self, head_point):
        if not 0 <= head_point.x < self.state_width:
            self.state.game_over = True
            return True
        if not 0 < head_point.y <= self.state_height:
            self.state.game_over = True
            return True
        if 1 <= self.state.snake[:-1].count(head_point):
            self.state.game_over = True
            return True
        return False

    def check_apple_eaten(self, head_point):
        if head_point == self.state.apple:
            while True:
                self.state.apple.x = randint(0, self.state.field[0]-1)
                self.state.apple.y = randint(1, self.state.field[1])
                if self.state.snake.count(self.state.apple) == 0:
                    break
            return True
        return False

    def check_state_game(self, head_point):
        if not self.check_game_over(head_point):
            if not self.check_apple_eaten(head_point):
                self.state.snake.pop()
            else:
                self.state.speed -= self.acceleration
            self.state.snake.insert(0, head_point)





