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
		[ (53, 426, 32, 76), (197, 426, 32, 76), (341, 426, 30, 76) ],
		# Right Idle
		[ (480, 426, 31, 76), (617, 426, 33, 76), (763, 426, 31, 76) ],

		# Left Run
		[ (52, 284, 41, 76), (197, 284, 32, 76), (330, 284, 49, 76) ],
		# Right Run
		[ (471, 284, 49, 76), (622, 284, 32, 76), (758, 284, 41, 76) ],

		# Left Jump
		[ (45, 141, 50, 76), (185, 141, 50, 76), (329, 141, 50, 76) ],
		# Right Jump
		[ (473, 141, 50, 76), (617, 141, 50, 76), (758, 141, 50, 76) ],

		# Left Falling
		[ (609, 0, 50, 76), (609, 0, 50 ,76), (609, 0, 50, 76) ],
		# Right Falling
		[ (757, 0, 50, 76), (757, 0, 50 ,76), (757, 0, 50, 76) ],

		# Climb
		[ (49, 0, 46, 76), (193, 0, 42, 76), (49, 0, 46, 76) ],
		# Die
		[ (327, 0, 56 ,76), (467, 0, 56, 76), (327, 0, 56, 76) ]
	]

	def __init__(self):
		self.pos = (100, 300)
		self.delta = (0, 0)
		self.fidx = 0
		self.time = 0
		self.prev_state = None
		self.state = Mario.RIGHT_IDLE
		self.FPS = 7
		self.image = Image.load("IMAGE/Mario.png")

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
			for object in GameWorld.objects_at(GameWorld.layer.platform):
				if "Ladder" in object.name:
					if GameObject.collides_box(self, object):
						(_, bottom, _, top) = object.get_bb()
						(_, foot, _, _) = self.get_bb()
						
						if (ddy > 0 and foot >= top) or (ddy < 0 and foot <= bottom): continue
						
						dy += 3 * ddy
						self.state = Mario.CLIMB
						#print("Climb ladder")
						print(foot, top)
						
						if (foot >= top):
							self.state = self.prev_state
							self.prev_state = None
							ddy = 0

		self.delta = dx, dy

	def jump(self):
		if (self.state in [Mario.LEFT_IDLE, Mario.LEFT_RUN]):
			self.state = Mario.LEFT_JUMP
			self.falling_speed = Mario.JUMP
			GameState.jump_wav.play()
		elif (self.state in [Mario.RIGHT_IDLE, Mario.RIGHT_RUN]):
			self.state = Mario.RIGHT_JUMP
			self.falling_speed = Mario.JUMP
			GameState.jump_wav.play()

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

		for platform in GameWorld.objects_at(GameWorld.layer.platform):
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