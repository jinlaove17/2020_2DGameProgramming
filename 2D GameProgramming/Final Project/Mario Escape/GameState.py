from pico2d import *
from Mario import *
from Background import *
import GameFramework
import GameWorld
import GameSprite
import GameObject
import json

stage_level = None
prev_stage, next_stage = range(2)

def enter():
	GameWorld.game_init(["background", "platform", "coin", "obstacle", "mario"])
	GameSprite.load()

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
		GameWorld.current_objects = GameWorld.title_objects

	mario.handle_event(event)

def exit():
	pass

def pause():
	pass

def resume():
	pass

def load_stage():
	global stage_level, mario, background
	stage_level = 1
	mario = Mario()
	background = Background("IMAGE/background.png")

	for level in range(1, 3 + 1):
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

				GameWorld.add(info["layer_index"], object, level)
		
		print(GameWorld.stage3_objects)
		GameWorld.add(GameWorld.layer.mario, mario, level)
		GameWorld.add(GameWorld.layer.background, background, level)
			
	GameWorld.curr_objects = GameWorld.stage1_objects

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
			pass

def set_mario_pos(stage):
	global mario
	
	x, y = mario.pos

	if (stage == prev_stage):
		x = get_canvas_width() - Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2
	elif (stage == next_stage):
		x = Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2

	mario.pos = x, y


def change_stage():
	global stage_level, mario, background

	if (stage_level == 1):
		if (mario.pos[0] < Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2):
			set_mario_pos(next_stage)
		elif (mario.pos[0] >= get_canvas_width() - Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2):
			stage_level += 1
			set_mario_pos(next_stage)
			background.set_rect(150)
			GameWorld.curr_objects = GameWorld.stage2_objects
	elif (stage_level == 2):
		if (mario.pos[0] < Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2):
			stage_level -= 1
			set_mario_pos(prev_stage)
			background.set_rect(0)
			GameWorld.curr_objects = GameWorld.stage1_objects
		elif (mario.pos[0] >= get_canvas_width() - Mario.IMAGE_RECT[mario.state][mario.fidx][2] // 2):
			stage_level += 1
			set_mario_pos(next_stage)
			background.set_rect(250)
			GameWorld.curr_objects = GameWorld.stage3_objects

if (__name__ == "__main__"):
	GameFramework.run_main()