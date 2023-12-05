from pico2d import *

import game_world
from background import Background
from volleyball_net import Volleyball_Net
from cloud import Cloud
# from waves import Wave
from pikachu import Pikachu

import game_framework

screen_width = 432
screen_height = 304
size_per_space = 16

def handle_events():
    
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.running = False
        else:
            pikachu1.handle_event(event)
            pikachu2.handle_event(event)
            

def init():
    global pikachu1, pikachu2

    background = Background(screen_width, screen_height)
    game_world.add_object(background, 0)
    
    volleyball_net = Volleyball_Net(screen_width, screen_height)
    game_world.add_object(volleyball_net, 1)
    
    clouds = [Cloud(screen_width, screen_height) for _ in range(15)]
    game_world.add_objects(clouds, 1)
    
    # waves = [Wave(x * size_per_space) for x in range(screen_width // size_per_space)]
    # game_world.objects += waves

    pikachu1 = Pikachu('p1')
    pikachu2 = Pikachu('p2')
    game_world.add_object(pikachu1, 2)
    game_world.add_object(pikachu2, 2)
    
    
def update_world():
    game_world.update_world()
    

def render_world():
    clear_canvas()
    game_world.render_world()
    update_canvas()