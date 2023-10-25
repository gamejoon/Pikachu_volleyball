from pico2d import load_image

class Background:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.x = self.width // 2
        self.y = self.height // 2
        self.image = load_image("background.png")
    
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)