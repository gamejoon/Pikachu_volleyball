objects = []

def add(o):
    objects.append(o)
    
def update():
    for o in objects:
        o.update()

def render():
    for o in objects:
        o.draw()

def remove_object(o):
    if o in objects:
        objects.remove(o)