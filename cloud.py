from pico2d import load_image
from math import cos, radians
from random import randint

class Cloud:
    def __init__(self, x, screen_width, screen_height):
        self.width = 48
        self.height = 24
        self.x = x
        self.y = randint(screen_height // 2, screen_height)
        self.image = load_image("cloud.png")
        self.speed = 1
        self.theta = randint(1, 360)
    
    def update(self):
        self.x += self.speed
        self.theta = (self.theta + 10) % 360 

    def draw(self):
        self.image.draw(self.x, self.y, (int)(self.width * (1 + 0.2 * cos(radians(self.theta)))), (int)(self.height * (1 + 0.2 * cos(radians(self.theta)))))
        # cloud.size * (1 + 0.2 * cos(theta))