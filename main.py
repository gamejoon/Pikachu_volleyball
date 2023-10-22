from pico2d import *
import random

screen_width = 432
screen_height = 304

class Background:
    def __init__(self):
        self.width = screen_width
        self.height = screen_height
        self.x = self.width // 2
        self.y = self.height // 2
        self.image = load_image("D:\\github\\pikachu_volleyball\\Picture\\background.png")
    
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class Volleyball_Net:
    def __init__(self):
        self.width = 8
        self.height = 112
        self.x = screen_width // 2
        self.y = 32 + self.height // 2
        self.image = load_image("D:\\github\\pikachu_volleyball\\Picture\\volleyball_net.png")
    
    def update(self):
        pass
    
    def draw(self):
        self.image.draw(self.x, self.y)

class Cloud:
    def __init__(self, x):
        self.width = 48
        self.height = 24
        self.x = x
        self.y = random.randint(screen_height // 2, screen_height)
        self.image = load_image("D:\\github\\pikachu_volleyball\\Picture\\cloud.png")
        self.speed = 1
    
    def update(self):
        self.x += self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def create_world():
    global background
    global volleyball_net
    global clouds

    background = Background()
    volleyball_net = Volleyball_Net()
    clouds = [Cloud(0) for _ in range(30)]

def update_world():
    global background
    global volleyball_net
    global clouds

    background.update()
    volleyball_net.update()
    for o in range(len(clouds)):
        clouds[o].update()

def render_world():
    clear_canvas()

    background.draw()
    volleyball_net.draw()
    for o in range(len(clouds)):
        clouds[o].draw()
    
    update_canvas()

open_canvas(432, 304)
create_world()

running = True

while running:
    handle_events()
    update_world()
    render_world()

close_canvas()