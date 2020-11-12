from pico2d import *
import GameFramework
import GameObject
import GameState
import GameWorld
import Image

class Mario:
	GRAVITY = 3000
	JUMP = 900

	# State
	LEFT_IDLE = 0
	RIGHT_IDLE = 1
	LEFT_RUN = 2
	RIGHT_RUN = 3
	LEFT_JUMP = 4
	RIGHT_JUMP = 5
	LEFT_FALLING = 6
	RIGHT_FALLING = 7
	CLIMB = 8
	DIE = 9

	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
		(SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
		(SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
		(SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
		(SDL_KEYUP, SDLK_UP):      ( 0, -1),
		(SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
		(SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
		(SDL_KEYUP, SDLK_RIGHT):   (-1,  0)
	}

	KEY_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

	IMAGE_RECT = [
		# Left Idle
		[ (8, 247, 33, 79), (80, 245, 33, 78), (153, 247, 32, 77) ],
		# Right Idle
		[ (8, 168, 32, 77), (80, 167, 33, 78), (151, 168, 34, 77) ],

		# Left Run
		[ (205, 256, 43, 68), (280, 250, 33, 77), (339, 251, 50, 75) ],
		# Right Run
		[ (202, 173, 51, 75), (278, 172, 34, 78), (344, 178, 43, 68) ],

		# Left Jump
		[ (0, 80, 52, 71), (72, 76, 52, 72), (145, 78, 52, 72) ],
		# Right Jump
		[ (14, 2, 53, 72), (84, 1, 53, 71), (156, 3, 52, 72) ],

		# Left Falling
		[ (392, 93, 49, 64), (392, 93, 49, 64), (392, 93, 49, 64) ],
		# Right Falling
		[ (391, 9, 49, 64), (391, 9, 49, 64), (391, 9, 49, 64) ],

		# Climb
		[ (253, 91, 48, 76), (323, 92, 46, 74), (253, 91, 48, 76) ],
		# Die
		[ (245, 4, 57, 78), (324, 6, 57, 80), (245, 4, 57, 78) ]
	]

	def __init__(self):
		self.pos = (100, 500)
		self.delta = (0, 0)
		self.fidx = 0
		self.time = 0
		self.prev_state = None
		self.state = Mario.RIGHT_IDLE
		self.FPS = 7
		self.image = Image.load("image/Mario.png")

	def draw(self):
		self.fidx = int(self.time * self.FPS) % len(Mario.IMAGE_RECT[self.state])
		self.image.clip_draw(*Mario.IMAGE_RECT[self.state][self.fidx], *self.pos)

	def update(self):
		x, y = self.pos
		dx, dy = self.delta
		self.pos = x + dx, y + dy
		self.time += GameFramework.delta_time

		if (self.state in [Mario.LEFT_JUMP, Mario.RIGHT_JUMP, Mario.LEFT_FALLING, Mario.RIGHT_FALLING]):
			x, y = self.pos
			y = y + self.falling_speed * GameFramework.delta_time
			self.pos = x, y
			self.falling_speed -= Mario.GRAVITY * GameFramework.delta_time

		_, foot, _, _ = self.get_bb()
		platform = self.get_platform(foot)

		if (platform != None):
			left, bottom, right, top = platform.get_bb()

			if (self.state == Mario.LEFT_IDLE or self.state == Mario.LEFT_RUN):
				if (foot > top):
					self.state = Mario.LEFT_FALLING
					self.falling_speed = 0
			elif (self.state == Mario.RIGHT_IDLE or self.state == Mario.RIGHT_RUN):
				if (foot > top):
					self.state = Mario.RIGHT_FALLING
					self.falling_speed = 0
			elif (self.state == Mario.CLIMB or self.state == Mario.DIE):
				pass
			elif (self.state == Mario.LEFT_FALLING or self.state == Mario.LEFT_JUMP):
				if (self.falling_speed < 0 and int(foot) <= top):
					x, y = self.pos
					y = y + top - foot
					self.pos = x, y
					self.state = Mario.LEFT_RUN
					self.falling_speed = 0
			elif (self.state == Mario.RIGHT_FALLING or self.state == Mario.RIGHT_JUMP):
				if (self.falling_speed < 0 and int(foot) <= top):
					x, y = self.pos
					y = y + top - foot
					self.pos = x, y
					self.state = Mario.RIGHT_RUN
					self.falling_speed = 0

	def update_delta(self, ddx, ddy):
		dx, dy = self.delta
	
		if (ddx != 0):
			dx += 3 * ddx
			self.state = \
				Mario.LEFT_RUN if dx < 0 else \
				Mario.RIGHT_RUN if dx > 0 else \
				Mario.LEFT_IDLE if ddx > 0 else Mario.RIGHT_IDLE

		if (self.prev_state == None):
			self.prev_state = self.state

		if (ddy != 0):
			for object in GameWorld.objects[0]:
				if "Ladder" in object.name:
					if GameObject.collides_box(self, object):
						(_, bottom, _, top) = object.get_bb()
						(_, foot, _, _) = self.get_bb()
						
						if (ddy > 0 and foot >= top) or (ddy < 0 and foot <= bottom): continue
						
						dy += 3 * ddy
						self.state = Mario.CLIMB
						print(self.prev_state)
						print("Climb ladder")
						
						if(foot >= top):
							self.state = self.prev_state
							self.prev_state = None
							ddy = 0
							break

		self.delta = dx, dy

	def jump(self):
		if (self.state in [Mario.LEFT_IDLE, Mario.LEFT_RUN]):
			self.state = Mario.LEFT_JUMP
			self.falling_speed = Mario.JUMP
		elif (self.state in [Mario.RIGHT_IDLE, Mario.RIGHT_RUN]):
			self.state = Mario.RIGHT_JUMP
			self.falling_speed = Mario.JUMP

	def get_bb(self):
		x, y = self.pos
		w, h = (Mario.IMAGE_RECT[self.state][self.fidx][2] // 2, Mario.IMAGE_RECT[self.state][self.fidx][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	def get_platform(self, foot):
		selected = None
		select_top = 0
		x, y = self.pos

		for platform in GameWorld.objects[0]:
			left, bottom, right, top = platform.get_bb()
			if (x < left or x > right): continue
			mid = (bottom + top) // 2
			if (foot < mid): continue
			if (selected == None):
				selected = platform
				select_top = top
			else:
				if top > select_top:
					selected = platform
					select_top = top

		return selected

	def handle_event(self, event):
		pair = (event.type, event.key)

		if pair in Mario.KEY_MAP:
			self.update_delta(*Mario.KEY_MAP[pair])
		elif (pair == Mario.KEY_SPACE):
			self.jump()
