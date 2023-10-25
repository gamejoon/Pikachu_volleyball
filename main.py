from pico2d import *
import random
from math import cos, radians
from background import Background

screen_width = 432
screen_height = 304

class Volleyball_Net:
    def __init__(self):
        self.width = 8
        self.height = 112
        self.x = screen_width // 2
        self.y = 32 + self.height // 2
        self.image = load_image("volleyball_net.png")
    
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
        self.image = load_image("cloud.png")
        self.speed = 1
        self.theta = random.randint(1, 360)
    
    def update(self):
        self.x += self.speed
        self.theta = (self.theta + 10) % 360 

    def draw(self):
        self.image.draw(self.x, self.y, (int)(self.width * (1 + 0.2 * math.cos(math.radians(self.theta)))), (int)(self.height * (1 + 0.2 * math.cos(math.radians(self.theta)))))
        # cloud.size * (1 + 0.2 * cos(theta))
        
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

    background = Background(screen_width, screen_height)
    volleyball_net = Volleyball_Net()
    clouds = [Cloud(random.randint(0, screen_width)) for _ in range(random.randint(10, 15))]

def update_world():
    global background
    global volleyball_net
    global clouds

    background.update()
    volleyball_net.update()
    for o in range(len(clouds)):
        clouds[o].update()
    delay(0.05)

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