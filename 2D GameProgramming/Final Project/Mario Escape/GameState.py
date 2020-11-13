from pico2d import *
from Mario import *
import GameFramework
import GameWorld
import GameSprite
import GameObject
import Background
import json

stage_level = 0 # 스테이트 전환시 level을 변경해가며 enter()를 다시 호출(나중에 사용함)

def enter():
	GameWorld.init(["background", "platform", "coin", "obstacle", "mario"])
	GameSprite.load()

	global mario
	mario = Mario()
	GameWorld.add(GameWorld.layer.mario, mario)
	
	background = Background.Background()
	GameWorld.add(GameWorld.layer.background, background)

	load_sound()
	load_stage(1)


def update():
	GameWorld.update()
	check_coin()
	check_obstacle()

def draw():
	GameWorld.draw()
	GameObject.draw_collision_box()

def handle_event(event):
	global mario

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

def load_stage(level):
	with open("JSON/Stage_%d.json" % level) as file:
		data = json.load(file)

	for info in data:
		if ("Tile" in info["name"]):
			object = GameSprite.Platform(info["name"], info["x"], info["y"], info["w"], info["h"])
		elif ("Ladder" in info["name"]):
			object = GameSprite.Platform(info["name"], info["x"], info["y"], info["w"], info["h"])
		elif ("Coin" in info["name"]):
			object = GameSprite.Coin(info["name"], info["x"], info["y"], info["w"], info["h"])
		elif ("Obstacle" in info["name"]):
			object = GameSprite.Obstacle(info["name"], info["x"], info["y"], info["w"], info["h"])
			
		GameWorld.add(info["layer_index"], object)

def load_sound():
	global bg_music, coin_wav

	coin_wav = load_wav("SOUND/coin.wav")

def check_coin():
	global coin_wav

	for coin in GameWorld.objects_at(GameWorld.layer.coin):
		if GameObject.collides_box(mario, coin):
			GameWorld.remove(coin)
			coin_wav.play()

def check_obstacle():
	for obstacle in GameWorld.objects_at(GameWorld.layer.obstacle):
		if GameObject.collides_box(mario, obstacle):
			GameWorld.remove(obstacle)

if (__name__ == "__main__"):
	GameFramework.run_main()