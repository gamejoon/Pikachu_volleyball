from pico2d import load_image
from math import cos, radians
from random import randint
import game_world

class Cloud:
    image = None
    def __init__(self, x, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 48
        self.height = 24
        self.x = x
        self.y = randint(self.screen_height // 2, self.screen_height)
        self.speed = 1
        self.theta = randint(1, 360)
        if Cloud.image == None:
            Cloud.image = load_image("cloud.png")
    
    def update(self):
        self.x += self.speed
        self.theta = (self.theta + 10) % 360
        if self.x - self.width // 2 > self.screen_width:
            game_world.remove_object(self)
            print("remove")

    def draw(self):
        self.image.draw(self.x, self.y, (int)(self.width * (1 + 0.2 * cos(radians(self.theta)))), (int)(self.height * (1 + 0.2 * cos(radians(self.theta)))))
        # cloud.size * (1 + 0.2 * cos(theta))