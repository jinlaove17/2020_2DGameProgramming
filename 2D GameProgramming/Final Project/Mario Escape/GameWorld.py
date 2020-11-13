from pico2d import *
import GameFramework

objects = []
trashcan = []

def init(layer_names):
    global objects
    global layer

    objects = []
    layer = lambda: None
    layerIndex = 0

    for name in layer_names:
        objects.append([])
        layer.__dict__[name] = layerIndex
        layerIndex += 1

def add(layer_index, object):
    objects[layer_index].append(object)

def remove(object):
    trashcan.append(object)

def all_objects():
    for layer_objects in objects:
        for object in layer_objects:
            yield object

def object(layer_index, object_index):
    layer_objects = objects[layer_index]
    return layer_objects[object_index]

def objects_at(layer_index):
    for object in objects[layer_index]:
        yield object

def update():
	for object in all_objects():
		object.update()

	#counts = list(map(len, objects))
	#print("total object count =", counts)

	if (len(trashcan) > 0):
		empty_trashcan()

def draw():
	for object in all_objects():
		object.draw()

def empty_trashcan():
    global trashcan

    for object in trashcan:
        for layer_objects in objects:
            try:
                layer_objects.remove(object)
            except ValueError:
                pass

    trashcan = []