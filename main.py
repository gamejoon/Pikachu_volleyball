from pico2d import *

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(432, 304)

running = True

while running:
    handle_events()
    update_canvas()

close_canvas()