from pico2d import open_canvas, close_canvas
import game_framework
import single_mode as current_mode

screen_width = 432
screen_height = 304

open_canvas(screen_width, screen_height)
game_framework.run(current_mode)
close_canvas()