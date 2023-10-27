from pico2d import *
import random
from background import Background
from volleyball_net import Volleyball_Net
from cloud import Cloud
import game_world

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
    global running
    global background
    global volleyball_net
    global clouds
    global game_world

    running = True
    
    background = Background(screen_width, screen_height)
    game_world.add(background)
    
    volleyball_net = Volleyball_Net(screen_width, screen_height)
    game_world.add(volleyball_net)
    
    clouds = [Cloud(random.randint(-screen_width // 2, screen_width), screen_width, screen_height) for _ in range(20)]
    game_world.objects += clouds
    
def update_world():
    game_world.update()
    delay(0.05)

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas(screen_width, screen_height)
create_world()

while running:
    handle_events()
    update_world()
    render_world()
    # print(game_world.objects)

close_canvas()