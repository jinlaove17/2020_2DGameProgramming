from pico2d import *
from Mario import *
from Background import *
import GameFramework
import GameWorld
import GameObject
import GameSprite
import Image
import Font
import json

STATE_IN_GAME, STATE_GAME_OVER = range(2)
STAGE_LEVEL = 0
TOTAL_COIN_COUNT = 0
PREV, NEXT = range(2)
FONT_COLOR = (255, 255, 255)

def enter():
	GameWorld.clear()
	GameSprite.load()

	global STAGE_LEVEL, TOTAL_COIN_COUNT

	STAGE_LEVEL = 1
	TOTAL_COIN_COUNT = 0

	global state, game_over_image

	state = STATE_IN_GAME
	game_over_image = load_image("IMAGE/GameOver.png")

	global mario, background, ui, font

	mario = Mario()
	background = Background("IMAGE/Background.png", mario)
	ui = GameSprite.UI(10, get_canvas_height() - 72)
	font = Font.load("FONT/koverwatch.ttf", 25)

	GameWorld.game_init(["background", "platform", "coin", "box", "plant", "cannon", "obstacle", "Door", "mario", "ui"])

	for level in range(1, 5 + 1):
		with open("JSON/Stage_%d.json" % level) as file:
			data = json.load(file)

			for info in data:
				obj = GameSprite.createObject(info, mario)
				if obj is None:
					print("Not created:", info["name"])
					continue
				if isinstance(obj, GameSprite.Coin):
					TOTAL_COIN_COUNT += 1
				# obj = clazz(info["name"], info["x"], info["y"], info["w"], info["h"])
				# if ("Tile" in info["name"] or "Ladder" in info["name"]):
				# 	object = GameSprite.Platform(info["name"], info["x"], info["y"], info["w"], info["h"])
				# elif ("Coin" in info["name"]):
				# 	object = GameSprite.Coin(info["name"], info["x"], info["y"], info["w"], info["h"])
				# 	TOTAL_COIN_COUNT += 1
				# elif ("Obstacle" in info["name"]):
				# 	object = GameSprite.Obstacle(info["name"], info["x"], info["y"], info["w"], info["h"])
				# elif ("Plant" in info["name"]):
				# 	object = GameSprite.Plant(info["name"], info["x"], info["y"], info["w"], info["h"], mario)
				# elif ("Box" in info["name"]):
				# 	object = GameSprite.Box(info["name"], info["x"], info["y"], info["w"], info["h"], mario)
				# elif ("Cannon" in info["name"]):
				# 	object = GameSprite.Cannon(info["name"], info["x"], info["y"])
				# elif ("Door" in info["name"]):
				# 	object = GameSprite.Door(info["name"], info["x"], info["y"])

				GameWorld.add(info["layer_index"], obj, level)
		
		GameWorld.add(GameWorld.layer.mario, mario, level)
		GameWorld.add(GameWorld.layer.background, background, level)
		GameWorld.add(GameWorld.layer.ui, ui, level)

	GameWorld.curr_objects = GameWorld.stage1_objects
	load_sound()

def update():
	global TOTAL_COIN_COUNT
	global state

	if (state == STATE_GAME_OVER): return
	if (TOTAL_COIN_COUNT == 0): GameSprite.Door.open_door()

	GameWorld.update()
	check_collision()
	change_stage()

	if (ui.dead()): end_game()

def draw():
	GameWorld.draw()
	GameObject.draw_collision_box()

	font.draw(95, get_canvas_height() - 60, "X %d" % TOTAL_COIN_COUNT, FONT_COLOR)

	if (state == STATE_GAME_OVER):
		game_over_image.draw(400, 300, get_canvas_width(), get_canvas_height())

def handle_event(event):
	if (event.type == SDL_QUIT):
		GameFramework.quit()
	elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		GameFramework.pop()

	mario.handle_event(event)

def exit():
	global bgm, start_wav, coin_wav, plant_dead_wav

	Image.unload("IMAGE/Mario.png")
	Image.unload("IMAGE/Sprite.png")
	Image.unload("IMAGE/Background.png")
	Font.unload("FONT/koverwatch.ttf", 25)
	GameWorld.clear()

	bgm.stop()
	del bgm
	del start_wav
	del coin_wav
	del plant_dead_wav

def pause():
	pass

def resume():
	pass

def end_game():
	global state, mario
	
	state = STATE_GAME_OVER
	mario.LIFE_LOST_WAV.set_volume(0)
	game_over_wav.set_volume(100)
	game_over_wav.play()

def load_sound():
	global bgm, start_wav, coin_wav, plant_dead_wav, game_over_wav

	bgm = load_music("SOUND/cave dungeon.mp3")
	start_wav = load_wav("SOUND/game start.wav")
	coin_wav = load_wav("SOUND/coin.wav")
	plant_dead_wav= load_wav("SOUND/plant dead.wav")
	game_over_wav = load_wav("SOUND/game over.wav")

	bgm.set_volume(100)
	bgm.repeat_play()
	start_wav.play()

	global mario

	mario.LIFE_LOST_WAV.set_volume(80)

def check_collision():
	global TOTAL_COIN_COUNT
	global mario

	for coin in GameWorld.objects_at(GameWorld.layer.coin):
		if GameObject.collides_box(mario, coin):
			GameWorld.remove(coin)
			TOTAL_COIN_COUNT -= 1
			coin_wav.play()

	for obstacle in GameWorld.objects_at(GameWorld.layer.obstacle):
		if GameObject.collides_box(mario, obstacle):
			mario.is_collide = True
			break

	for plant in GameWorld.objects_at(GameWorld.layer.plant):
		if GameObject.collides_box(mario, plant):
			mario.is_collide = True
			break

	#for box in GameWorld.objects_at(GameWorld.layer.box):
	#	if GameObject.collides_box(mario, box):
	#		box.is_collide = True
	#	else:
	#		box.is_collide = False

	for obstacle in GameWorld.objects_at(GameWorld.layer.obstacle):
		if ("Stone" in obstacle.name):
			for plant in GameWorld.objects_at(GameWorld.layer.plant):
				if GameObject.collides_box(obstacle, plant):
					GameWorld.remove(obstacle)
					plant.state = GameSprite.Plant.DIE
					plant_dead_wav.play()
					return
			for box in GameWorld.objects_at(GameWorld.layer.box):
				if GameObject.collides_box(obstacle, box):
					GameWorld.remove(obstacle)
					GameWorld.remove(box)
					ladder = GameSprite.Platform("Ladder_1", 740, 430, 39, 170)
					GameWorld.add(GameWorld.layer.platform, ladder, 3)
					return

def set_stage(stage):
	global STAGE_LEVEL

	if (stage == PREV):
		STAGE_LEVEL -= 1
	elif (stage == NEXT):
		STAGE_LEVEL += 1

	background.set_stage_level(STAGE_LEVEL)

def change_stage():
	global STAGE_LEVEL
	global mario

	if (mario.die()):
		mario.pos = (100, 300)
		# mario.delta = (0, 0)
		mario.state = Mario.RIGHT_RUN
		mario.falling_speed = 0
		mario.is_collide = False
		STAGE_LEVEL = 1
		ui.decrease_life()
		background.set_stage_level(1)
		GameWorld.curr_objects = GameWorld.stage1_objects
		return

	(x, y) = mario.pos
	hw = Mario.IMAGE_RECT[mario.state][mario.fidx % len(Mario.IMAGE_RECT[mario.state])][2] // 2
	hh = Mario.IMAGE_RECT[mario.state][mario.fidx % len(Mario.IMAGE_RECT[mario.state])][3] // 2

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
			x = hw
			set_stage(NEXT)
			GameWorld.curr_objects = GameWorld.stage4_objects
		elif ((730 < x and x < get_canvas_width()) and (y > get_canvas_height())):
			y = hh
			# mario.delta = (0, 0)
			STAGE_LEVEL = 5
			GameWorld.curr_objects = GameWorld.stage5_objects
	elif (STAGE_LEVEL == 4):
		if (x < hw):
			x = get_canvas_width() - hw
			set_stage(PREV)
			GameWorld.curr_objects = GameWorld.stage3_objects
		elif (x > get_canvas_width() - hw):
			x = get_canvas_width() - hw
	elif (STAGE_LEVEL == 5):
		if (x < hw):
			x = hw
		elif (x > get_canvas_width() - hw):
			x = get_canvas_width() - hw
		elif (y < hh):
			y = get_canvas_width() - hh
			mario.delta = (0, 0)
			STAGE_LEVEL = 3
			GameWorld.curr_objects = GameWorld.stage3_objects
			
	mario.pos = (x, y)

if (__name__ == "__main__"):
	GameFramework.run_main()