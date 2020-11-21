from pico2d import *
import GameFramework
import GameState
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

	def __init__(self, name, x, y, w, h):
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
	IMAGE_RECT_SPIKE = [
		(585, 316, 61, 25),
		(673, 316, 64, 49),
		(761, 316, 68, 79)
	]

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

		if ("FireBar" in self.name):
			if ("FireBar_1" in self.name):
				self.radius = 280
				self.radian = math.pi
			elif ("FireBar_2" in self.name):
				self.radius = 140
				self.radian = math.pi
			elif ("FireBar_4" in self.name):
				self.radius = 140
				self.radian = 0
			elif ("FireBar_5" in self.name):
				self.radius = 280
				self.radian = 0

	def draw(self):
		self.time += GameFramework.delta_time
		self.rad += GameFramework.delta_time
		self.radian += GameFramework.delta_time

		if ("FireBar" in self.name):
			self.pos = (400 + self.radius * math.cos(self.radian), 250 + self.radius * math.sin(self.radian))
			sprite_image.clip_composite_draw(*self.rect, self.rad, ' ', *self.pos, *self.size)
		elif ("Spike" in self.name):
			FPS = 1
			self.fidx = round(self.time * FPS) % 3
			sprite_image.clip_draw_to_origin(*Obstacle.IMAGE_RECT_SPIKE[self.fidx], *self.pos)
		elif ("Stone" in self.name):
			sprite_image.clip_draw(*self.rect, *self.pos)

	def update(self):
		if ("Stone" in self.name):
			(x, y) = self.pos
			(w, h) = self.size

			x += self.dx * Obstacle.FALLING_PPS * GameFramework.delta_time
			y += self.dy * Obstacle.FALLING_PPS * GameFramework.delta_time

			self.pos = (x, y)

			if (y < -h):
				GameWorld.remove(self)

	def get_bb(self):
		(x, y) = self.pos

		if ("FireBar" in self.name or "Stone" in self.name):
			(w, h) = self.size
			left = x - w // 2
			bottom = y - h // 2
			right = x + w // 2
			top = y + h // 2
		else:
			(w, h) = (Obstacle.IMAGE_RECT_SPIKE[self.fidx][2], Obstacle.IMAGE_RECT_SPIKE[self.fidx][3])
			left = x
			bottom = y
			right = x + w
			top = y + h

		return (left, bottom, right, top)

class Plant:
	FPS = 3
	ATTACK_COUNT = 0
	STATE_CHANGE_COUNT = 0
	FALLING_PPS = 300
	IDLE, ATTACK, DIE = range(3)
	IMAGE_RECT = [
		# IDLE
		[(660, 496, 58, 68), (728, 496, 56, 68), (794, 496, 51, 68)],
		# ATTACK
		[(855, 496, 47, 68), (912, 496, 69, 68), (996, 496, 77, 68)],
		# DIE
		[(1081, 496, 48, 68)]
	]

	def __init__(self, name, x, y, w, h, mario):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.mario = mario
		self.size = (w, h)
		self.fidx = 0
		self.time = 0
		self.state = Plant.IDLE

	def draw(self):
		self.time += GameFramework.delta_time
		self.fidx = round(self.time * Plant.FPS) % len(Plant.IMAGE_RECT[self.state])
		sprite_image.clip_draw(*Plant.IMAGE_RECT[self.state][self.fidx], *self.pos)

	def update(self):
		Plant.ATTACK_COUNT += Plant.FPS * GameFramework.delta_time

		if (Plant.ATTACK_COUNT >= 5):
			Plant.ATTACK_COUNT = 0
			attacks = random.choice([True, False])
			if (attacks): self.attack()

		if (self.state == Plant.ATTACK):
			Plant.STATE_CHANGE_COUNT += Plant.FPS * GameFramework.delta_time

			if (Plant.STATE_CHANGE_COUNT >= 3):
				Plant.STATE_CHANGE_COUNT = 0
				self.state = Plant.IDLE
		elif (self.state == Plant.DIE):
			(x, y) = self.pos
			(dx, dy) = (0, -1)
			h = Plant.IMAGE_RECT[self.state][self.fidx][3] // 2

			x += dx * Plant.FALLING_PPS * GameFramework.delta_time
			y += dy * Plant.FALLING_PPS * GameFramework.delta_time

			self.pos = (x, y)

			if (y < -h):
				GameWorld.remove(self)
				print("plant removed!")

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (Plant.IMAGE_RECT[self.state][self.fidx][2] // 2, Plant.IMAGE_RECT[self.state][self.fidx][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	def get_coords(self):
		(x, y) = self.mario.pos
		(dx, dy) = (0, -1)

		# 58은 Obstacle_Stone의 높이(h)
		return (x, get_canvas_height() + 58, dx, dy)

	def attack(self):
		(x, y, dx, dy) = self.get_coords()
		if (x <= 100): return
		self.state = Plant.ATTACK
		GameState.plant_attack_wav.play()

		# 78은 Obstacle_Stone의 너비(w)
		stone = Obstacle("Obstacle_Stone", x, y, 78, 58, dx, dy)
		GameWorld.add(GameWorld.layer.obstacle, stone, 4)

class Box:
	def __init__(self, name, x, y, w, h, mario):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.size = (w, h)
		self.mario = mario
		self.is_collide = False

	def draw(self):
		sprite_image.clip_draw_to_origin(*self.rect, *self.pos, *self.size)

	def update(self):
		#if (self.is_collide):
		#	(mario_dx, mario_dy) = self.mario.delta
		#	self.mario.delta = (mario_dx / 2, mario_dy)
		#	(x, y) = self.pos
		#	x += (mario_dx / 2) * 250 * GameFramework.delta_time
		#	self.pos = (x, y)
		pass

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = self.size

		left = x
		bottom = y
		right =  x + w
		top =  y + h

		return (left, bottom, right, top)

class UI:
	LIFE_COUNT = 3

	def __init__(self, x, y):
		self.mario_pos = (x, y)
		self.life_pos = (x + 55, y + 30)
		self.coin_pos = (x + 55, y)
		UI.LIFE_COUNT = 3

	def draw(self):
		mario_rect = (856, 323, 47, 62)
		sprite_image.clip_draw_to_origin(*mario_rect, *self.mario_pos)
		life_rect = (660, 596, 40 * UI.LIFE_COUNT, 24)
		sprite_image.clip_draw_to_origin(*life_rect, *self.life_pos)
		coin_rect = (582, 445, 31, 32)
		sprite_image.clip_draw_to_origin(*coin_rect, *self.coin_pos, 25, 25)

	def update(self):
		pass