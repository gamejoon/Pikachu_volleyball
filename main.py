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

    background = load_image("D:\\github\\pikachu_volleyball\\Picture\\background.png")

def render_world():
    background.draw(432 // 2, 304 // 2)

open_canvas(432, 304)
create_world()

running = True

while running:
    handle_events()
    render_world()
    update_canvas()

close_canvas()