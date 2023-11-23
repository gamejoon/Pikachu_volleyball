from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN
import game_framework

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN

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
        pikachu.image.clip_draw(pikachu.image_pivot['Idle'][int(pikachu.frame)][0], pikachu.image_pivot['Idle'][int(pikachu.frame)][1], pikachu.image_pivot['Idle'][int(pikachu.frame)][2], pikachu.image_pivot['Idle'][int(pikachu.frame)][3], pikachu.x, pikachu.y)

class Run:
    @staticmethod
    def enter(pikachu):
        pass

    @staticmethod
    def do(pikachu):
        pass

    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        pass

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
        self.image_pivot = {'Idle' : ((8, 885 - 327, 61 - 8, 327 - 272),
                                      (73, 885 - 328, 127 - 73, 328 - 273),
                                      (139, 885 - 329, 192 - 139, 329 - 274),
                                      (205, 885 - 328, 259 - 205, 328 - 273),
                                      (272, 885 - 327, 325 - 272, 327 - 272),
                                      (272, 885 - 327, 325 - 272, 327 - 272),
                                      (205, 885 - 328, 259 - 205, 328 - 273),
                                      (139, 885 - 329, 192 - 139, 329 - 274),
                                      (73, 885 - 328, 127 - 73, 328 - 273),
                                      (8, 885 - 327, 61 - 8, 327 - 272)
                                      )}
        self.dir = 0
    
    def update(self):
        self.state_machine.update()
    
    def draw(self):
        self.state_machine.draw()
    
    def func_frame_per_action(self):
        time_per_action = 1.2
        action_per_time = 1.0 / time_per_action
        frame_per_action = 10
        return (self.frame + action_per_time * frame_per_action * game_framework.frame_time) % 10