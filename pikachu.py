from pico2d import load_image
import game_framework

class Idle:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def do():
        pass
    
    @staticmethod
    def exit():
        pass

    @staticmethod
    def draw():
        pass

class StateMachine:
    def __init__(self, pikachu):
        pass
    
    def start(self):
        pass
    
    def update(self):
        pass

    def handle_event(self):
        pass

class Pikachu:
    def __init__(self, player):
        self.x = 304
        self.y = 54
        self.width = 60
        self.height = 60
        self.frame = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.image = load_image("sprite_sheet.png")
    
    def update(self):
        pass
    
    def draw(self):
        self.image.clip_draw(5, 885 - 330, 60, 60, self.x, self.y)