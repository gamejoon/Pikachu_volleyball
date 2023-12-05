from pico2d import load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN, SDLK_RETURN, SDLK_g, SDLK_d, SDLK_r, SDLK_f, SDLK_z
import game_framework
import math

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

def g_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_g

def g_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_g

def d_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def d_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def r_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_r

def r_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_r

def f_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_f

def f_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_f

def z_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_z

def z_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_z

class Idle:
    @staticmethod
    def enter(pikachu, e):
        pikachu.xdir = 0

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()
    
    @staticmethod
    def exit(pikachu, e):
        if r_down(e) and pikachu.player == 'p1': pikachu.jumping()
        if upkey_down(e) and pikachu.player == 'p2': pikachu.jumping()


class Run_Right:
    @staticmethod
    def enter(pikachu, e):
        pikachu.xdir = 1

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()

    @staticmethod
    def exit(pikachu, e):
        if r_down(e) and pikachu.player == 'p1': pikachu.jumping()
        if upkey_down(e) and pikachu.player == 'p2': pikachu.jumping()


class Run_Left:
    @staticmethod
    def enter(pikachu, e):
        pikachu.xdir = -1

    @staticmethod
    def do(pikachu):
        pikachu.frame = pikachu.func_frame_per_action()

    @staticmethod
    def exit(pikachu, e):
        if r_down(e) and pikachu.player == 'p1': pikachu.jumping()
        if upkey_down(e) and pikachu.player == 'p2': pikachu.jumping()

class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.current_state = Idle
        self.transitions = {'p1' : {
                Idle: {g_down: Run_Right, d_down: Run_Left, r_down: Idle},
                Run_Right: {g_up: Idle, d_down: Run_Left, r_down: Run_Right},
                Run_Left: {d_up: Idle, g_down: Run_Right, r_down: Run_Left}
            },
            'p2' : {
            Idle : {right_down : Run_Right, left_down : Run_Left, upkey_down : Idle},
            Run_Right : {right_up : Idle, left_down : Run_Left, upkey_down : Run_Right},
            Run_Left : {left_up : Idle, right_down : Run_Right, upkey_down : Run_Left}
            }
        }
    
    def start(self):
        self.current_state.enter(self.pikachu, ('None', 0))

    def update(self):
        self.current_state.do(self.pikachu)
        self.pikachu.x += self.pikachu.xdir * self.pikachu.func_speed_pps() * game_framework.frame_time
        if self.pikachu.player == 'p1':
            if self.pikachu.x - self.pikachu.width // 2 < 0:
                self.pikachu.x = self.pikachu.width // 2
            elif self.pikachu.x + self.pikachu.width // 2 > 432 // 2:
                self.pikachu.x = 432 // 2 - self.pikachu.width // 2
        elif self.pikachu.player == 'p2':
            if self.pikachu.x - self.pikachu.width // 2 < 216:
                self.pikachu.x = 216 + self.pikachu.width // 2
            elif self.pikachu.x + self.pikachu.width // 2 > 432:
                self.pikachu.x = 432 - self.pikachu.width // 2
        if self.pikachu.ydir > 0:
            self.pikachu.y += 5 * -math.cos(self.pikachu.ydir) * self.pikachu.func_speed_pps() * game_framework.frame_time
            self.pikachu.ydir -= math.pi * game_framework.frame_time
            if self.pikachu.ydir < 0: self.pikachu.ydir = 0

    def handle_event(self, e):
        for check_event, next_event in self.transitions[self.pikachu.player][self.current_state].items():
            if check_event(e):
                self.current_state.exit(self.pikachu, e)
                self.current_state = next_event
                self.current_state.enter(self.pikachu, e)

    def draw(self):
        if self.pikachu.player == 'p1':
            self.pikachu.image.clip_draw(self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][0],
                                    self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][1],
                                    self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][2],
                                    self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][3], self.pikachu.x, self.pikachu.y)
        elif self.pikachu.player == 'p2':
            self.pikachu.image.clip_composite_draw(self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][0],
                                              self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][1],
                                              self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][2],
                                              self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][3], 0, 'h', self.pikachu.x,
                                              self.pikachu.y, self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][2],
                                              self.pikachu.image_pivot[self.current_state][int(self.pikachu.frame)][3])

class Pikachu:
    def __init__(self, player):
        if player == 'p1': self.x = 108
        elif player == 'p2': self.x = 324
        self.y = 54
        self.width = 64
        self.height = 64
        self.frame = 0
        self.speed = 5
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.image = load_image("sprite_sheet.png")
        self.image_pivot = {Idle : ((8, 885 - 327, 61 - 8, 327 - 272),
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
                            Run_Right : ((8, 885 - 327, 61 - 8, 327 - 272),
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
                            Run_Left: ((8, 885 - 327, 61 - 8, 327 - 272),
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
        self.xdir = 0
        self.ydir = 0
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
        return (self.frame + action_per_time * frame_per_action * game_framework.frame_time) % len(self.image_pivot[self.state_machine.current_state])

    def func_speed_pps(self):
        pixel_per_meter = (10.0 / 0.5) # 10pixel 50cm
        speed_mps = self.speed
        speed_pps = (speed_mps * pixel_per_meter)
        return speed_pps

    def jumping(self):

        if self.ydir == 0:
            self.ydir = math.pi
