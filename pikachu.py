from pico2d import load_image
import game_framework

class Idle:
    @staticmethod
    def enter(pikachu):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()
    
    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(5 + 80 * int(pikachu.frame), 885 - 330, 60, 60, pikachu.x, pikachu.y)

class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.current_state = Idle
        self.transitions = { }
    
    def start(self):
        self.current_state.enter(self.pikachu)
    
    def update(self):
        self.current_state.do(self.pikachu)

    def handle_event(self):
        pass

    def draw(self):
        self.current_state.draw(self.pikachu)

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
        self.state_machine.update()
    
    def draw(self):
        self.state_machine.draw()
    
    def func_frame_per_action(self):
        time_per_action = 0.5
        action_per_time = 1.0 / time_per_action
        frame_per_action = 7
        return (self.frame + action_per_time * frame_per_action * game_framework.frame_time) % 7