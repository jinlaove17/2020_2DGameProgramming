from pico2d import *
import GameFramework
import GameWorld
import Image
import json
import math
import random

sprite_image = None
sprite_rects = {}

def load():
	global sprite_image

	if (sprite_image is None):
		sprite_image = Image.load("IMAGE/Sprite.png")

		with open("JSON/ObjectRect.json") as file:
			data = json.load(file)

			for name in data:
				#print(name)
				sprite_rects[name] = tuple(data[name])

def createObject(info, mario):
	# obj = clazz(info["name"], info["x"], info["y"], info["w"], info["h"])
	obj = None
	if ("Tile" in info["name"] or "Ladder" in info["name"]):
		obj = Platform(info["name"], info["x"], info["y"], info["w"], info["h"])
	elif ("Coin" in info["name"]):
		obj = Coin(info["name"], info["x"], info["y"])
	elif ("Obstacle_FireBar" in info["name"]):
		obj = FireBarObstacle(info["name"], info["x"], info["y"], info["w"], info["h"])
	elif ("Obstacle_Spike" in info["name"]):
		obj = SpikeObstacle(info["name"], info["x"], info["y"], info["w"], info["h"])
		obj.height = 0
	elif ("Obstacle" in info["name"]):
		obj = Obstacle(info["name"], info["x"], info["y"], info["w"], info["h"])
	elif ("Plant" in info["name"]):
		obj = Plant(info["name"], info["x"], info["y"], mario)
	elif ("Box" in info["name"]):
		obj = Box(info["name"], info["x"], info["y"], info["w"], info["h"])
	elif ("Cannon" in info["name"]):
		obj = Cannon(info["name"], info["x"], info["y"])
	elif ("Door" in info["name"]):
		obj = Door(info["name"], info["x"], info["y"])

	return obj

class Platform:
	def __init__(self, name, x, y, w, h):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.size = (w, h)

	def draw(self):
		sprite_image.clip_draw_to_origin(*self.rect, *self.pos, *self.size)

	def update(self):
		pass

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = self.size

		left = x
		bottom = y
		right =  x + w
		top =  y + h

		return (left, bottom, right, top)

class Coin:
	FPS = 10
	IMAGE_RECT = [
		(582, 445, 31, 32),
		(615, 445, 30, 32),
		(652, 445, 21, 32),
		(690, 445, 10, 32),
		(718, 445, 21, 32),
		(747, 445, 30, 32),
	]

	def __init__(self, name, x, y):
		self.name = name
		self.pos = (x, y)
		self.fidx = 0
		self.time = 0

	def draw(self):
		self.time += GameFramework.delta_time
		self.fidx = round(self.time * Coin.FPS) % 6
		sprite_image.clip_draw(*Coin.IMAGE_RECT[self.fidx], *self.pos)

	def update(self):
		pass

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (Coin.IMAGE_RECT[self.fidx][2] // 2, Coin.IMAGE_RECT[self.fidx][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

class Obstacle:
	FALLING_PPS = 300
	ROTATIONS = {
		"Obstacle_FireBar_1": (280, math.pi),
		"Obstacle_FireBar_2": (140, math.pi),
		"Obstacle_FireBar_3": (0, 0),
		"Obstacle_FireBar_4": (140, 0),
		"Obstacle_FireBar_5": (280, 0),
	}
	SPIKE_WAV = None
	FIREBAR_WAV = None

	def __init__(self, name, x, y, w, h, dx=0, dy=0):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		(self.dx, self.dy) = (dx, dy)
		self.size = (w, h)
		self.fidx = 0
		self.time = 0
		self.rad = 0
		self.radius = 0
		self.radian = 0
		self.wav_count = 0

		if (self.name in Obstacle.ROTATIONS):
			(self.radius, self.radian) = Obstacle.ROTATIONS[self.name]

		if (Obstacle.SPIKE_WAV == None):
			Obstacle.SPIKE_WAV = load_wav("SOUND/spike.wav")
			Obstacle.SPIKE_WAV.set_volume(30)

		if (Obstacle.FIREBAR_WAV == None):
			Obstacle.FIREBAR_WAV = load_wav("SOUND/fire whoosh.wav")
			Obstacle.FIREBAR_WAV.set_volume(10)

	def draw(self):
		self.time += GameFramework.delta_time
		self.drawImage()

	def drawImage(self):
		sprite_image.clip_draw(*self.rect, *self.pos)

	def update(self):
		pass

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = self.size

		left = x - w // 2
		bottom = y - h // 2
		right = x + w // 2
		top = y + h // 2

		return (left, bottom, right, top)

class SpikeObstacle(Obstacle):
	IMAGE_RECT = (761, 316, 68, 72)

	def update(self):
		t = self.time % 2.0

		if (t > 1.0):
			t = 2.0 - t

		h = SpikeObstacle.IMAGE_RECT[3]
		self.height = round(h * t)

		self.wav_count += GameFramework.delta_time

		if (self.wav_count >= 1):
			self.wav_count = -1
			Obstacle.SPIKE_WAV.play()

	def drawImage(self):
		(x, y, w, h) = SpikeObstacle.IMAGE_RECT
		y += h - self.height
		h = self.height
		sprite_image.clip_draw_to_origin(x, y, w, h, *self.pos)

	def get_bb(self):
		(x, y) = self.pos
		(_, _, w, h) = SpikeObstacle.IMAGE_RECT
		return (x, y, x + w, y + self.height)

class FireBarObstacle(Obstacle):
	def update(self):
		self.wav_count += GameFramework.delta_time
		
		if (self.wav_count >= 2):
			self.wav_count = 0
			Obstacle.FIREBAR_WAV.play()

	def drawImage(self):
		self.rad += GameFramework.delta_time
		self.radian += GameFramework.delta_time
		self.pos = (400 + self.radius * math.cos(self.radian), 250 + self.radius * math.sin(self.radian))
		sprite_image.clip_composite_draw(*self.rect, self.rad, ' ', *self.pos, *self.size)

class StoneObstacle(Obstacle):
	def update(self):
		(x, y) = self.pos
		(w, h) = self.size
		
		x += self.dx * Obstacle.FALLING_PPS * GameFramework.delta_time
		y += self.dy * Obstacle.FALLING_PPS * GameFramework.delta_time
		
		self.pos = (x, y)
		
		if (y < -h):
			GameWorld.remove(self)

class BulletObstacle(Obstacle):
	def update(self):
		(x, y) = self.pos
		(w, h) = self.size
		
		x += self.dx * Obstacle.FALLING_PPS * GameFramework.delta_time
		y += self.dy * Obstacle.FALLING_PPS * GameFramework.delta_time
		
		self.pos = (x, y)
		
		if (x < -w):
			GameWorld.remove(self)

class Box:
	def __init__(self, name, x, y, w, h):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.size = (w, h)

	def draw(self):
		sprite_image.clip_draw_to_origin(*self.rect, *self.pos, *self.size)

	def update(self):
		pass

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = self.size

		left = x
		bottom = y
		right =  x + w
		top =  y + h

		return (left, bottom, right, top)

class Plant:
	FPS = 4
	FALLING_PPS = 300
	ATTACK_COUNT = 0
	IDLE, ATTACK, DIE = range(3)
	ATTACK_WAV = None

	IMAGE_RECT = [
		# IDLE
		[(660, 496, 58, 68), (728, 496, 56, 68), (794, 496, 51, 68)],
		# ATTACK
		[(855, 496, 47, 68), (912, 496, 69, 68), (996, 496, 77, 68)],
		# DIE
		[(1081, 496, 48, 68)]
	]

	def __init__(self, name, x, y, mario):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.fidx = 0
		self.time = 0
		self.state = Plant.IDLE
		self.mario = mario

		if (Plant.ATTACK_WAV == None):
			Plant.ATTACK_WAV = load_wav("SOUND/plant attack.wav")

	def draw(self):
		self.time += GameFramework.delta_time
		self.fidx = round(self.time * Plant.FPS) % len(Plant.IMAGE_RECT[self.state])
		sprite_image.clip_draw(*Plant.IMAGE_RECT[self.state][self.fidx], *self.pos)

	def update(self):
		(mario_x, _) = self.mario.pos

		if (mario_x > 100 and self.state == Plant.IDLE):
			Plant.ATTACK_COUNT += Plant.FPS * GameFramework.delta_time

			if (Plant.ATTACK_COUNT >= 5):
				if (self.fidx == 0):
					Plant.ATTACK_COUNT = 0
					self.state = Plant.ATTACK
				
		if (self.state == Plant.ATTACK and self.fidx == len(Plant.IMAGE_RECT[self.state]) - 1):
			self.attack(mario_x)
			self.state = Plant.IDLE
		elif (self.state == Plant.DIE):
			(x, y) = self.pos
			dy = -1

			y += dy * Plant.FALLING_PPS * GameFramework.delta_time
			h = Plant.IMAGE_RECT[self.state][self.fidx][3] // 2

			self.pos = (x, y)

			if (y < -h):
				GameWorld.remove(self)

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (Plant.IMAGE_RECT[self.state][self.fidx][2] // 2, Plant.IMAGE_RECT[self.state][self.fidx][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	def attack(self, mario_x):
		# Obstacle_Stone의 너비와 높이
		(w, h) = (78, 58)
		(x, y) = (mario_x, get_canvas_height() + h)
		(dx, dy) = (0, -1)

		Plant.ATTACK_WAV.play()

		stone = StoneObstacle("Obstacle_Stone", x, y, w, h, dx, dy)
		GameWorld.add(GameWorld.layer.obstacle, stone, 4)

class Cannon:
	FPS = 8
	ATTACK_COUNT = 0
	IDLE, ATTACK = range(2)
	LEFT, RIGHT = range(2)
	ATTACK_WAV = None

	IMAGE_RECT = [
		# IDLE
		[(768, 260, 37, 32)],
		# ATTACK
		[(850, 260, 38, 32), (928, 260, 41, 32), (1007, 260, 43, 32), (769, 216, 53, 32), (850, 216, 58, 32), (928, 216, 61, 32)]
	]

	def __init__(self, name, x, y):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.state = Cannon.IDLE
		self.time = 0
		self.fidx = 0

		if (Cannon.ATTACK_WAV == None):
			Cannon.ATTACK_WAV = load_wav("SOUND/cannon attack.wav")

	def draw(self):
		self.time += GameFramework.delta_time
		self.fidx = round(self.time * Cannon.FPS) % len(Cannon.IMAGE_RECT[self.state])
		sprite_image.clip_draw(*Cannon.IMAGE_RECT[self.state][self.fidx], *self.pos)

	def update(self):
		if (self.state == Cannon.IDLE):
			Cannon.ATTACK_COUNT += Cannon.FPS * GameFramework.delta_time

			if (Cannon.ATTACK_COUNT >= 3):
				if (self.fidx == 0):
					Cannon.ATTACK_COUNT = 0
					attacks = random.choice([True, False])

				if (attacks):
					self.state = Cannon.ATTACK

		if (self.state == Cannon.ATTACK and self.fidx == len(Cannon.IMAGE_RECT[self.state]) - 1):
			self.attack()
			self.state = Cannon.IDLE

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (Cannon.IMAGE_RECT[self.state][self.fidx][2] // 2, Cannon.IMAGE_RECT[self.state][self.fidx][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	def attack(self):
		# Obstacle_Bullet의 너비와 높이
		(w, h) = (27, 19)
		(x, y) = self.pos
		(dx, dy) = (-1, 0)
		x -= 30
		
		Cannon.ATTACK_WAV.play()

		bullet = BulletObstacle("Obstacle_Bullet", x, y, w, h, dx, dy)
		GameWorld.add(GameWorld.layer.obstacle, bullet, 5)

class Door:
	OPENS = False

	def __init__(self, name, x, y):
		self.name = name
		self.pos = (x, y)
		self.size = (64, 63)
		self.close_rect = (580, 216, 64, 63)
		self.open_rect = (670, 216, 64, 63)

	def __del__(self):
		Door.OPENS = False

	def draw(self):
		if (not Door.OPENS):
			sprite_image.clip_draw_to_origin(*self.close_rect, *self.pos)
		else:
			sprite_image.clip_draw_to_origin(*self.open_rect, *self.pos)

	def update(self):
		pass

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = self.size

		left = x
		bottom = y
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	@staticmethod
	def open_door():
		Door.OPENS = True

class UI:
	def __init__(self, x, y):
		self.mario_pos = (x, y)
		self.life_pos = (x + 55, y + 30)
		self.coin_pos = (x + 55, y)
		self.life = 3

	def draw(self):
		mario_rect = (856, 323, 47, 62)
		sprite_image.clip_draw_to_origin(*mario_rect, *self.mario_pos)
		life_rect = (660, 596, 40 * self.life, 24)
		sprite_image.clip_draw_to_origin(*life_rect, *self.life_pos)
		coin_rect = (582, 445, 31, 32)
		sprite_image.clip_draw_to_origin(*coin_rect, *self.coin_pos, 25, 25)

	def update(self):
		pass

	def decrease_life(self):
		self.life -= 1

	def dead(self):
		return (self.life <= 0)