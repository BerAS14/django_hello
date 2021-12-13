import unittest

from pages.controller_game_snake import ControllerGameSnake
from pages.point import Point


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):

    def setUp(self):
        self.game = ControllerGameSnake()
        self.game.state.field = [13, 9, 'white']
        self.game.game_init()

    def test_example(self):
        self.assertEqual(4, fun(3))

    def test_snake(self):
        self.assertEqual(6, self.game.state.snake[0].x)
        self.assertEqual(4, self.game.state.snake[0].y)

    def test_go_up_from_start(self):
        self.game.state.game_started = True
        self.game.do_step()
        self.game.go_up()
        self.game.do_step()
        self.assertEqual('Up', self.game.state.direction)

    def test_go_up_when_going_down(self):
        game = ControllerGameSnake()
        game.game_init()
        game.state.game_started = True
        game.do_step()
        game.go_down()
        game.do_step()
        game.go_up()
        self.assertEqual('Down', game.state.direction)

    def test_go_up_when_going_left(self):
        game = ControllerGameSnake()
        game.game_init()
        game.state.game_started = True
        game.do_step()
        game.go_left()
        game.do_step()
        game.go_up()
        self.assertEqual('Up', game.state.direction)

    def test_get_center(self):
        x = self.game.get_center()
        self.assertEqual((6, 4), x)

    def test_game_do_step_up(self):
        self.game.state.game_started = True
        self.game.do_step()
        self.game.go_up()
        self.game.do_step()
        self.assertEqual("[{'x': 7, 'y': 5}, {'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}]",
                         str(self.game.state.snake))

    def test_game_do_step_down(self):
        self.game.state.game_started = True
        self.game.do_step()
        self.game.go_down()
        self.game.do_step()
        self.assertEqual(
            "[{'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}]",
            str(self.game.state.snake))

    def test_game_do_step_right_not_change_direction(self):
        self.game.state.game_started = True
        self.game.go_right()
        self.game.do_step()
        self.assertEqual(
            "[{'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}]",
            str(self.game.state.snake))

    def test_game_do_step_right(self):
        self.game.state.game_started = True
        self.game.go_down()
        self.game.go_right()
        self.game.do_step()
        self.assertEqual(
            "[{'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}]",
            str(self.game.state.snake))

    def test_game_over_step_right(self):
        self.game.state.game_started = True
        print(self.game.state.snake[0])
        for i in range(8):
            self.game.do_step()
            print(self.game.state.snake[0])
        self.assertEqual(True, self.game.state.game_over)

    def test_game_over_step_left(self):
        self.game.state.game_started = True
        self.game.go_down()
        self.game.go_left()
        print(self.game.state.snake[0])
        for i in range(7):
            self.game.do_step()
            print(self.game.state.snake[0])
        self.assertEqual(True, self.game.state.game_over)

    def test_game_over_step_up(self):
        self.game.state.game_started = True
        self.game.do_step()
        self.game.go_up()
        print(self.game.state.snake[0])
        for i in range(6):
            self.game.do_step()
            print(self.game.state.snake[0])
        self.assertEqual(True, self.game.state.game_over)

    def test_game_over_step_down(self):
        self.game.state.game_started = True
        self.game.do_step()
        self.game.go_down()
        print(self.game.state.snake[0])
        for i in range(3):
            self.game.do_step()
            print(self.game.state.snake[0])
        self.assertEqual(False, self.game.state.game_over)
        self.game.do_step()
        print(self.game.state.snake[0])
        self.assertEqual(True, self.game.state.game_over)
        self.game.do_step()
        print(self.game.state.snake[0])
        self.assertEqual(True, self.game.state.game_over)

    def test_compare_equal_points(self):
        point = Point(3, 5)
        self.assertEqual(Point(3, 5), point)

    def test_game_over_self_crossing(self):
        self.game.state.game_started = True
        self.game.do_step()
        self.game.go_down()
        self.game.do_step()
        self.game.go_left()
        self.game.do_step()
        self.game.do_step()
        self.assertEqual(False, self.game.state.game_over)
        self.game.go_up()
        self.game.do_step()
        self.game.go_right()
        self.game.do_step()
        self.game.go_down()
        self.game.do_step()
        self.assertEqual(True, self.game.state.game_over)

    def test_game_enlargement_snake_step_right(self):
        self.game.state.game_started = True
        self.game.state.apple.x = 8
        self.game.state.apple.y = 4
        self.game.do_step()
        self.game.do_step()
        self.assertEqual(6, len(self.game.state.snake))

    def test_game_enlargement_snake_step_up(self):
        self.game.state.game_started = True
        self.game.state.apple.x = 7
        self.game.state.apple.y = 5
        self.game.do_step()
        self.game.go_up()
        self.game.do_step()
        self.assertEqual(6, len(self.game.state.snake))

    def test_game_enlargement_snake_step_down(self):
        self.game.state.game_started = True
        self.game.state.apple.x = 7
        self.game.state.apple.y = 3
        self.game.do_step()
        self.game.go_down()
        self.game.do_step()
        self.assertEqual(6, len(self.game.state.snake))

    def test_game_enlargement_snake_step_left(self):
        self.game.state.game_started = True
        self.game.state.apple.x = 6
        self.game.state.apple.y = 3
        self.game.do_step()
        self.game.go_down()
        self.game.do_step()
        self.game.go_left()
        self.game.do_step()
        self.assertEqual(6, len(self.game.state.snake))