from pico2d import *

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

    background = load_image("D:\\github\\pikachu_volleyball\\Picture\\background.png") # width = 432, height = 304
    volleyball_net = load_image("D:\\github\\pikachu_volleyball\\Picture\\volleyball_net.png") # width = 8, height = 112

def render_world():
    background.draw(432 // 2, 304 // 2)
    volleyball_net.draw(432 // 2, 32 + 112 // 2)

open_canvas(432, 304)
create_world()

running = True

while running:
    handle_events()
    render_world()
    update_canvas()

close_canvas()