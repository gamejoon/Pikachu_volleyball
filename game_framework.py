running = None
current_mode = None

def run(mode):
    global running, current_mode
    
    running = True
    current_mode = mode
    current_mode.init()
    
    while running:
        current_mode.handle_events()
        current_mode.update_world()
        current_mode.render_world()

def quit():
    pass

def change_mode(mode):
    pass

def push_mode(mode):
    pass

def pop_mode():
    pass