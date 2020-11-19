from pico2d import *
from Mario import *
from Background import *
import GameFramework
import GameWorld
import GameSprite
import GameObject
import TitleState
import json

STAGE_LEVEL = None
PREV, NEXT = range(2)

def enter():
	GameWorld.game_init(["background", "platform", "coin", "obstacle", "mario"])
	GameSprite.load()

	init_stage()
	load_sound()

def update():
	GameWorld.update()
	check_coin()
	check_obstacle()
	change_stage()

def draw():
	GameWorld.draw()
	GameObject.draw_collision_box()

def handle_event(event):
	if (event.type == SDL_QUIT):
		GameFramework.quit()
	elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		bgm.stop()
		GameWorld.clear()
		GameFramework.change(TitleState)

	mario.handle_event(event)

def exit():
	pass

def pause():
	pass

def resume():
	pass

def init_stage():
	global STAGE_LEVEL
	global mario, background

	STAGE_LEVEL = 1
	mario = Mario()
	background = Background("IMAGE/Background.png", mario)

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
		
		GameWorld.add(GameWorld.layer.mario, mario, level)
		GameWorld.add(GameWorld.layer.background, background, level)
			
	GameWorld.curr_objects = GameWorld.stage1_objects

def load_sound():
	global bgm, jump_wav, coin_wav, life_lost_wav

	bgm = load_music("SOUND/cave dungeon.mp3")
	jump_wav = load_wav("SOUND/jump.wav")
	coin_wav = load_wav("SOUND/coin.wav")
	life_lost_wav = load_wav("SOUND/life lost.wav")

	bgm.set_volume(100)
	bgm.repeat_play()
	life_lost_wav.set_volume(60)

def check_coin():
	for coin in GameWorld.objects_at(GameWorld.layer.coin):
		if GameObject.collides_box(mario, coin):
			GameWorld.remove(coin)
			coin_wav.play()

def check_obstacle():
	global mario

	for obstacle in GameWorld.objects_at(GameWorld.layer.obstacle):
		if GameObject.collides_box(mario, obstacle):
			if ("FireBar" in obstacle.name):
				mario.is_collide = True

def set_stage(stage):
	global STAGE_LEVEL

	if (stage == PREV):
		STAGE_LEVEL -= 1
		Background.STAGE_LEVEL -= 1
	elif (stage == NEXT):
		STAGE_LEVEL += 1
		Background.STAGE_LEVEL += 1

def change_stage():
	global STAGE_LEVEL, mario

	(x, y) = mario.pos
	hw = Mario.IMAGE_RECT[mario.state][mario.fidx % len(Mario.IMAGE_RECT[mario.state])][2] // 2

	if (STAGE_LEVEL == 1):
		if (x < hw):
			x = hw
		elif (x > get_canvas_width() - hw):
			x = hw
			set_stage(NEXT)
			GameWorld.curr_objects = GameWorld.stage2_objects
	elif (STAGE_LEVEL == 2):
		if (x < hw):
			x = get_canvas_width() - hw
			set_stage(PREV)
			GameWorld.curr_objects = GameWorld.stage1_objects
		elif (x > get_canvas_width() - hw):
			x = hw
			set_stage(NEXT)
			GameWorld.curr_objects = GameWorld.stage3_objects
	elif (STAGE_LEVEL == 3):
		if (x < hw):
			x = get_canvas_width() - hw
			set_stage(PREV)
			GameWorld.curr_objects = GameWorld.stage2_objects
		elif (x > get_canvas_width() - hw):
			pass
			
	mario.pos = (x, y)

if (__name__ == "__main__"):
	GameFramework.run_main()