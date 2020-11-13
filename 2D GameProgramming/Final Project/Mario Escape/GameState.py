from pico2d import *
from Mario import *
import GameFramework
import GameWorld
import GameSprite
import GameObject
import Background
import json

stage_level = None

def enter():
	GameWorld.init(["background", "platform", "coin", "obstacle", "mario"])
	GameSprite.load()

	global mario
	mario = Mario()
	GameWorld.add(1, GameWorld.layer.mario, mario)

	background = Background.Background()
	GameWorld.add(1, GameWorld.layer.background, background)

	load_sound()
	load_stage()


def update():
	GameWorld.update()
	check_coin()
	check_obstacle()
	change_stage()

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

def load_stage():
	for level in range(1, 3):
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
				
				GameWorld.add(level, info["layer_index"], object)

	print(GameWorld.stage1_objects)
	print(GameWorld.stage2_objects)
	GameWorld.curr_objects = GameWorld.stage1_objects

	global stage_level
	stage_level = 1

def load_sound():
	global bgm, jump_wav, coin_wav

	bgm = load_music("SOUND/cave dungeon.mp3")
	jump_wav = load_wav("SOUND/jump.wav")
	coin_wav = load_wav("SOUND/coin.wav")

	bgm.set_volume(80)
	bgm.repeat_play()

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

def change_stage():
	global stage_level, mario

	if (stage_level == 1):
		if (mario.pos[0] >= get_canvas_width() - Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2):
			stage_level += 1
			GameWorld.stage1_objects = GameWorld.curr_objects
			GameWorld.curr_objects = GameWorld.stage2_objects
			mario.pos = Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2, 140

if (__name__ == "__main__"):
	GameFramework.run_main()