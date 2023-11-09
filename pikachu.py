from pico2d import load_image

class Pikachu:
    def __init__(self, player):
        self.x = 304
        self.y = 54
        self.frame = 0
        self.image = load_image("sprite_sheet.png")
    
    def update(self):
        pass
    
    def draw(self):
        self.image.clip_draw(5, 885 - 330, 60, 60, self.x, self.y)