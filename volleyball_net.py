from pico2d import load_image

class Volleyball_Net:
    def __init__(self, screen_width, screen_height):
        self.width = 8
        self.height = 112
        self.x = screen_width // 2
        self.y = 32 + self.height // 2
        self.image = load_image("volleyball_net.png")
    
    def update(self):
        pass
    
    def draw(self):
        self.image.draw(self.x, self.y)