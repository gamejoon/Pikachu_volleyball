objects = []

def add_object(o):
    objects.append(o)

def add_objects(o):
    for object in o:
        objects.append(object)

def update():
    for o in objects:
        o.update()

def render():
    for o in objects:
        o.draw()