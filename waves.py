from pico2d import load_image
import random

class Wave:
    image = None
    def __init__(self, x):
        self.width = 16
        self.height = 32
        self.x = x + self.width // 2
        self.y = 0 - self.height // 2
        self.speed = 2
        if Wave.image == None:
            Wave.image = load_image("wave.png")
    
    def update(self):
        self.y += self.speed
        if self.y > 32 - self.height // 2:
            self.y = 32 - self.height // 2
            self.speed = -1
        elif self.y + self.height // 2 < 0 and self.speed < 0:
            self.speed = 2
            self.y = -random.randrange(0, 40) - self.height // 2
        self.y -= random.randrange(0, 3)
        
    def draw(self):
        self.image.draw(self.x, self.y)