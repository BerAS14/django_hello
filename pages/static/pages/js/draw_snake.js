var canvas = document.getElementById("c");
var context = canvas.getContext("2d");
var screen_field_width = canvas.width;
var screen_field_height = canvas.height;
var color_head_snake = 'blue';
var color_snake = 'green';

function initEvent() {
    addEventListener("keydown", function(event) {
        if (event.code == 'Space') {
          fetch('/snake_start/?format=json');
          return;
        }
        if (event.code == 'ArrowUp') {
          fetch('/go_up/?format=json');
          return;
        }
        if (event.code == 'ArrowLeft') {
          fetch('/go_left/?format=json');
          return;
        }
        if (event.code == 'ArrowRight') {
          fetch('/go_right/?format=json');
          return;
        }
        if (event.code == 'ArrowDown') {
          fetch('/go_down/?format=json');
          return;
        }
    });
}

function transformCoordinate(x, y, state_field_width, state_field_height) {

    return [Math.round(screen_field_width / state_field_width * x),
        Math.round(screen_field_height - y * screen_field_height / state_field_height)];
}

function getSizeRectangle(state_field_width, state_field_height) {
    return [Math.round(screen_field_width / state_field_width * 1), Math.round(1 * screen_field_height / state_field_height)];
}

function drawSnake(stateSnake) {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height);
    context.beginPath();
    var screen_size_rectangle = getSizeRectangle(stateSnake['field'][0], stateSnake['field'][1]);
    var screen_coordinates;
    var snake = stateSnake['snake'];
    var field = stateSnake['field'];
    for (var prop in snake) {
      screen_coordinates = transformCoordinate(snake[prop].x, snake[prop].y, field[0], field[1]);
      let color = (prop > 0) ? color_snake : color_head_snake;
      context.fillStyle = color;
      context.fillRect(screen_coordinates[0], screen_coordinates[1], screen_size_rectangle[0], screen_size_rectangle[1]);
      context.strokeRect(screen_coordinates[0], screen_coordinates[1], screen_size_rectangle[0], screen_size_rectangle[1]);
    }
}

function fetchNow() {
    fetch('/do_step/?format=json').then(response => response.json()).then(stateSnake => {
      drawSnake(stateSnake);
      setTimeout(fetchNow, 600);
    });
}

function drawGameSnake(){
    initEvent();
    fetchNow();
}

drawGameSnake();





