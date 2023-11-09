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
    game_framework.running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.running = False
            

def init():
    global background
    global volleyball_net
    global clouds
    # global waves
    global game_world

    
    background = Background(screen_width, screen_height)
    game_world.add_object(background)
    
    volleyball_net = Volleyball_Net(screen_width, screen_height)
    game_world.add_object(volleyball_net)
    
    clouds = [Cloud(screen_width, screen_height) for _ in range(15)]
    game_world.add_objects(clouds)
    
    # waves = [Wave(x * size_per_space) for x in range(screen_width // size_per_space)]
    # game_world.objects += waves
    
    pikachu = Pikachu('p1')
    game_world.add_object(pikachu)
    
    
def update_world():
    game_world.update()
    

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()