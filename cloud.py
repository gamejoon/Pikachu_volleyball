from pico2d import load_image
from random import randint

class Cloud:
    image = None
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 48
        self.height = 24
        self.x = randint(self.screen_width - 500, self.screen_width - 1)
        self.y = randint(self.screen_height // 2, self.screen_height)
        self.speed = randint(1, 3)
        self.sizediff = randint(0, 10)
        if Cloud.image == None:
            Cloud.image = load_image("cloud.png")
    
    def update(self):
        self.x += self.speed
        self.sizediff = (self.sizediff + 1) % 11
        if self.x - (self.width + self.func_sizediff()) // 2 > self.screen_width:
            self.x = self.screen_width - 500
            self.y = randint(self.screen_height // 2, self.screen_height)
            self.speed = randint(1, 3)

    def draw(self):
        self.image.draw(self.x, self.y, self.width + self.func_sizediff(), self.height + self.func_sizediff())
        # self.size + 2 * (5 - (|5 - (0 ~ 10)|))
    
    def func_sizediff(self):
        return 2 * (5 - abs(self.sizediff - 5))    