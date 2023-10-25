from pico2d import *
import random
from background import Background
from volleyball_net import Volleyball_Net
from cloud import Cloud

screen_width = 432
screen_height = 304
        
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
    volleyball_net = Volleyball_Net(screen_width, screen_height)
    clouds = [Cloud(random.randint(0, screen_width), screen_width, screen_height) for _ in range(random.randint(10, 15))]

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