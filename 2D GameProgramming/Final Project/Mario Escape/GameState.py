from pico2d import *
from Mario import *
import GameFramework
import GameWorld
import GameSprite
import GameObject
import json

stage_level = None # 스테이트 전환시 level을 변경해가며 enter()를 다시 호출(나중에 사용함)
interact_object = []

def enter():
	global mario, tile1, tile2, ladder

	mario = Mario()
	GameWorld.add(3, mario)
	
	with open("JSON/Stage_1.json") as file:
		data = json.load(file)

	for info in data:
		object = GameSprite.Sprite(info["name"], info["x"], info["y"], info["w"], info["h"])
		GameWorld.add(info["layer_index"], object)

		if "ladder" in info["name"]:
			interact_object.append(object)

	print(interact_object)

def update():
	GameWorld.update()

	for layer_objects in GameWorld.objects:
		for object in layer_objects:
			if(object != mario):
				if GameObject.collides_box(mario, object):
					#print("Player Collision", object.name)
					pass

def draw():
	GameWorld.draw()
	GameObject.draw_collision_box()

def handle_event(event):
	global running

	if (event.type == SDL_QUIT):
		GameFramework.quit()
	elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		GameFramework.pop()

	mario.handle_event(event)

def exit():
	pass

def pause():
	pass

def resume():
	pass

if (__name__ == "__main__"):
	GameFramework.run_main()