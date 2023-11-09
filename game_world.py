objects = [[], [], []]

def add_object(o, layer):
    objects[layer].append(o)

def add_objects(o, layer):
    for object in o:
        objects[layer].append(object)

def update_world():
    for layer in objects:
        for o in layer:
            o.update()

def render_world():
    for layer in objects:
        for o in layer:
            o.draw()