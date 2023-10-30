from pico2d import load_image

class Wave:
    image = None
    def __init__(self):
        self.width = 16
        self.height = 32
        if Wave.image == None:
            Wave.image = load_image("wave.png")
    
    def update(self):
        pass
    
    def draw(self):
        pass