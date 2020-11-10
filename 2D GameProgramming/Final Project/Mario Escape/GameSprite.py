from pico2d import *
import GameFramework
import Image
import json

sprite_image = None
sprite_rects = {}
coin_rects = []

def load():
	global sprite_image

	if (sprite_image is None):
		sprite_image = Image.load("Image/Sprite.png")

		with open("JSON/ObjectRect.json") as file:
			data = json.load(file)

			for name in data:
				print(name)
				sprite_rects[name] = tuple(data[name])

	for num in range(1, 6 + 1):
		coin_rects.append(sprite_rects["Coin_%d" % num])

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
		x, y = self.pos
		w, h = self.size

		left = x
		bottom = y
		right =  x + w
		top =  y + h

		return (left, bottom, right, top)

class Coin:
	FPS = 10

	def __init__(self, name, x, y, w, h):
		self.name = name
		self.rect = sprite_rects[name]
		self.pos = (x, y)
		self.size = (w, h)
		self.time = get_time()

	def draw(self):
		frame = round((get_time() - self.time) * Coin.FPS) % 6
		sprite_image.clip_draw(*coin_rects[frame], *self.pos)

	def update(self):
		pass

	def get_bb(self):
		x, y = self.pos
		left = x - self.rect[2] // 2
		bottom = y - self.rect[3] // 2
		right = x + self.rect[2] // 2
		top = y + self.rect[3] // 2

		return (left, bottom, right, top)


class Obstacle:
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
		x, y = self.pos
		w, h = self.size

		left = x
		bottom = y
		right =  x + w
		top =  y + h

		return (left, bottom, right, top)