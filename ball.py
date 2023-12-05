from pico2d import load_image
import game_framework

class Ball:
    def __init__(self):
        self.x = 108
        self.y = 162
        self.width = 40
        self.height = 40
        self.frame = 0
        self.image = load_image('sprite_sheet.png')
        self.screen_width = 432
        self.screen_height = 304
        self.speed = 3

    def update(self):
        pass

    def draw(self):
        pass