import time

def run(mode):
    global running, current_mode
    
    running = True
    current_mode = mode
    current_mode.init()
    
    global frame_time
    frame_time = 0.0
    current_time = time.time()
    
    while running:
        current_mode.handle_events()
        current_mode.update_world()
        current_mode.render_world()
        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time

def quit():
    pass

def change_mode(mode):
    pass

def push_mode(mode):
    pass

def pop_mode():
    pass