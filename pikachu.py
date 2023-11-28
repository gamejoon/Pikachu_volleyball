from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN, SDLK_RETURN
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

def enter_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RETURN

def enter_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RETURN

class Idle:
    @staticmethod
    def enter(pikachu):
        pikachu.dir = 0

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()
    
    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        if pikachu.player == 'p1':
            pikachu.image.clip_draw(pikachu.image_pivot['Idle'][int(pikachu.frame)][0], pikachu.image_pivot['Idle'][int(pikachu.frame)][1], pikachu.image_pivot['Idle'][int(pikachu.frame)][2], pikachu.image_pivot['Idle'][int(pikachu.frame)][3], pikachu.x, pikachu.y)
        elif pikachu.player == 'p2':
            pikachu.image.clip_composite_draw(pikachu.image_pivot['Idle'][int(pikachu.frame)][0], pikachu.image_pivot['Idle'][int(pikachu.frame)][1], pikachu.image_pivot['Idle'][int(pikachu.frame)][2], pikachu.image_pivot['Idle'][int(pikachu.frame)][3], 0, 'h', pikachu.x, pikachu.y, pikachu.image_pivot['Idle'][int(pikachu.frame)][2], pikachu.image_pivot['Idle'][int(pikachu.frame)][3])


class Run_Right:
    @staticmethod
    def enter(pikachu):
        pikachu.dir = 1

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()

    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        if pikachu.player == 'p1':
            pikachu.image.clip_draw(pikachu.image_pivot['Run_Right'][int(pikachu.frame)][0], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][1], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][2], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][3], pikachu.x, pikachu.y)
        elif pikachu.player == 'p2':
            pikachu.image.clip_composite_draw(pikachu.image_pivot['Run_Right'][int(pikachu.frame)][0], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][1], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][2], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][3], 0, 'h', pikachu.x, pikachu.y, pikachu.image_pivot['Run_Right'][int(pikachu.frame)][2], pikachu.image_pivot['Run_Right'][int(pikachu.frame)][3])


class Run_Left:
    @staticmethod
    def enter(pikachu):
        pikachu.dir = -1

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()

    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        if pikachu.player == 'p1':
            pikachu.image.clip_draw(pikachu.image_pivot['Run_Left'][int(pikachu.frame)][0], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][1], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][2], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][3], pikachu.x, pikachu.y)
        elif pikachu.player == 'p2':
            pikachu.image.clip_composite_draw(pikachu.image_pivot['Run_Left'][int(pikachu.frame)][0], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][1], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][2], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][3], 0, 'h', pikachu.x, pikachu.y, pikachu.image_pivot['Run_Left'][int(pikachu.frame)][2], pikachu.image_pivot['Run_Left'][int(pikachu.frame)][3])

class Jump:
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
        self.transitions = {
            Idle : {right_down : Run_Right, left_down : Run_Left},
            Run_Right : {right_up : Idle, left_down : Run_Left},
            Run_Left : {left_up : Idle, right_down : Run_Right}
        }
    
    def start(self):
        self.current_state.enter(self.pikachu)

    def update(self):
        self.current_state.do(self.pikachu)
        self.pikachu.x += self.pikachu.dir * self.pikachu.func_speed_pps() * game_framework.frame_time
        if self.pikachu.player == 'p2':
            if self.pikachu.x - self.pikachu.width // 2 <= 216:
                self.pikachu.x = 216 + self.pikachu.width // 2
            elif self.pikachu.x + self.pikachu.width // 2 > 432:
                self.pikachu.x = 432 - self.pikachu.width // 2

    def handle_event(self, e):
        for check_event, next_event in self.transitions[self.current_state].items():
            if check_event(e):
                self.current_state.exit(self.pikachu)
                self.current_state = next_event
                self.current_state.enter(self.pikachu)

    def draw(self):
        self.current_state.draw(self.pikachu)

class Pikachu:
    def __init__(self, player):
        if player == 'p2':
            self.x = 304
            self.y = 54
        self.width = 60
        self.height = 60
        self.frame = 0
        self.speed = 5
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
                                      ),
                            'Run_Right' : ((8, 885 - 327, 61 - 8, 327 - 272),
                                           (73, 885 - 328, 127 - 73, 328 - 273),
                                           (139, 885 - 329, 192 - 139, 329 - 274),
                                           (205, 885 - 328, 259 - 205, 328 - 273),
                                           (272, 885 - 327, 325 - 272, 327 - 272),
                                           (272, 885 - 327, 325 - 272, 327 - 272),
                                           (205, 885 - 328, 259 - 205, 328 - 273),
                                           (139, 885 - 329, 192 - 139, 329 - 274),
                                           (73, 885 - 328, 127 - 73, 328 - 273),
                                           (8, 885 - 327, 61 - 8, 327 - 272)
                                           ),
                            'Run_Left': ((8, 885 - 327, 61 - 8, 327 - 272),
                                         (73, 885 - 328, 127 - 73, 328 - 273),
                                         (139, 885 - 329, 192 - 139, 329 - 274),
                                         (205, 885 - 328, 259 - 205, 328 - 273),
                                         (272, 885 - 327, 325 - 272, 327 - 272),
                                         (272, 885 - 327, 325 - 272, 327 - 272),
                                         (205, 885 - 328, 259 - 205, 328 - 273),
                                         (139, 885 - 329, 192 - 139, 329 - 274),
                                         (73, 885 - 328, 127 - 73, 328 - 273),
                                         (8, 885 - 327, 61 - 8, 327 - 272)
                                         )
                            }
        self.dir = 0
        self.player = player
    
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
    
    def draw(self):
        self.state_machine.draw()
    
    def func_frame_per_action(self):
        time_per_action = 1.2
        action_per_time = 1.0 / time_per_action
        frame_per_action = 10
        return (self.frame + action_per_time * frame_per_action * game_framework.frame_time) % 10

    def func_speed_pps(self):
        pixel_per_meter = (10.0 / 0.5) # 10pixel 50cm
        speed_mps = self.speed
        speed_pps = (speed_mps * pixel_per_meter)
        return speed_pps