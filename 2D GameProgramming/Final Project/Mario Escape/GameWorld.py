from pico2d import *
import GameFramework

curr_objects = []
stage1_objects = []
stage2_objects = []
trashcan = []

def init(layer_names):
    global curr_objects, stage1_objects, stage2_objects
    global layer

    curr_objects = []
    layer = lambda: None
    layerIndex = 0

    for name in layer_names:
        curr_objects.append([])
        layer.__dict__[name] = layerIndex
        layerIndex += 1

    stage1_objects = curr_objects
    stage2_objects = curr_objects

def add(stage_level, layer_index, object):
    if (stage_level == 1):
        stage1_objects[layer_index].append(object)
    elif (stage_level == 2):
        stage2_objects[layer_index].append(object)

def remove(object):
    trashcan.append(object)

def all_objects():
    for layer_objects in curr_objects:
        for object in layer_objects:
            yield object

def object(layer_index, object_index):
    layer_objects = curr_objects[layer_index]
    return layer_objects[object_index]

def objects_at(layer_index):
    for object in curr_objects[layer_index]:
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
        for layer_objects in curr_objects:
            try:
                layer_objects.remove(object)
            except ValueError:
                pass

    trashcan = []