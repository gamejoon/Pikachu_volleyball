object = []

def add(o):
    object.append(o)
    
def update():
    for o in object:
        o.update()

def render():
    for o in object:
        o.draw()