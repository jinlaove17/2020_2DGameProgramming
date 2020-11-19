from pico2d import *
import GameFramework

curr_objects = []
title_objects = []
stage1_objects = []
stage2_objects = []
stage3_objects = []
stage4_objects = []
trashcan = []

def title_init(layer_names):
    global title_objects
    global layer

    layer = lambda: None
    layerIndex = 0

    for name in layer_names:
        title_objects.append([])
        layer.__dict__[name] = layerIndex
        layerIndex += 1

def game_init(layer_names):
    global stage1_objects, stage2_objects, stage3_objects, stage4_objects
    global layer

    layer = lambda: None
    layerIndex = 0

    for name in layer_names:
        stage1_objects.append([])
        stage2_objects.append([])
        stage3_objects.append([])
        stage4_objects.append([])
        layer.__dict__[name] = layerIndex
        layerIndex += 1

def add(layer_index, object, stage_level=None):
    if (stage_level == 1):
        stage1_objects[layer_index].append(object)
    elif (stage_level == 2):
        stage2_objects[layer_index].append(object)
    elif (stage_level == 3):
        stage3_objects[layer_index].append(object)
    elif (stage_level == 4):
        stage4_objects[layer_index].append(object)
    else:
        title_objects[layer_index].append(object)

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

def clear():
    global curr_objects, title_objects, stage1_objects, stage2_objects, stage3_objects, stage4_objects

    curr_objects = stage1_objects
    for object in all_objects(): del object

    curr_objects = stage2_objects
    for object in all_objects(): del object

    curr_objects = stage3_objects
    for object in all_objects(): del object

    curr_objects = stage4_objects
    for object in all_objects(): del object

    curr_objects = title_objects
    for object in all_objects(): del object

    curr_objects = []
    title_objects = []
    stage1_objects = []
    stage2_objects = []
    stage3_objects = []
    stage4_objects = []