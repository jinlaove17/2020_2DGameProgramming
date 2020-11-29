from pico2d import *
import GameFramework
import GameSprite
import GameObject
import GameWorld
import Image

class Mario:
	LEFT_IDLE, RIGHT_IDLE, LEFT_RUN, RIGHT_RUN, LEFT_JUMP, RIGHT_JUMP, LEFT_FALLING, RIGHT_FALLING, CLIMB, DIE = range(10)
	MOVE_PPS = 250
	GRAVITY = 3000
	JUMP = 900
	JUMP_WAV = None
	LIFE_LOST_WAV = None

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
		[ (609, 0, 50, 76) ],
		# Right Falling
		[ (757, 0, 50, 76) ],

		# Climb
		[ (49, 0, 46, 76), (193, 0, 42, 76) ],
		# Die
		[ (327, 0, 56 ,76), (467, 0, 56, 76) ]
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
		self.is_collide = False

		if (Mario.JUMP_WAV == None):
			Mario.JUMP_WAV = load_wav("SOUND/jump.wav")
		if (Mario.LIFE_LOST_WAV == None):
			Mario.LIFE_LOST_WAV = load_wav("SOUND/life lost.wav")
			Mario.LIFE_LOST_WAV.set_volume(60)

	def draw(self):
		self.fidx = round(self.time * self.FPS) % len(Mario.IMAGE_RECT[self.state])
		self.image.clip_draw(*Mario.IMAGE_RECT[self.state][self.fidx], *self.pos)

	def update(self):
		(x, y) = self.pos
		(dx, dy) = self.delta
		x += dx * Mario.MOVE_PPS * GameFramework.delta_time
		# y += dy * Mario.MOVE_PPS * GameFramework.delta_time
		self.pos = (x, y)
		self.time += GameFramework.delta_time
		self.die()

		if (self.state in [Mario.LEFT_JUMP, Mario.RIGHT_JUMP, Mario.LEFT_FALLING, Mario.RIGHT_FALLING]):
			(x, y) = self.pos
			y = y + self.falling_speed * GameFramework.delta_time
			self.pos = (x, y)
			self.falling_speed -= Mario.GRAVITY * GameFramework.delta_time

		(_, foot, _, _) = self.get_bb()
		platform = self.get_platform(foot)

		if (platform != None):
			(left, bottom, right, top) = platform.get_bb()

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
					(x, y) = self.pos
					y = y + (top - foot)
					self.pos = (x, y)
					self.state = Mario.LEFT_RUN
					self.falling_speed = 0
			elif (self.state == Mario.RIGHT_FALLING or self.state == Mario.RIGHT_JUMP):
				if (self.falling_speed < 0 and int(foot) <= top):
					(x, y) = self.pos
					y = y + (top - foot)
					self.pos = (x, y)
					self.state = Mario.RIGHT_RUN
					self.falling_speed = 0

		self.update_ladder()

	def update_delta(self, ddx, ddy):
		if (self.state != Mario.DIE):
			(dx, dy) = self.delta
			
			if (ddx != 0):
				dx += ddx
				if self.state == Mario.LEFT_JUMP:
					if dx > 0: self.state = Mario.RIGHT_JUMP
				elif self.state == Mario.LEFT_FALLING:
					if dx > 0: self.state = Mario.RIGHT_FALLING
				elif self.state == Mario.RIGHT_JUMP:
					if dx < 0: self.state = Mario.LEFT_JUMP
				elif self.state == Mario.RIGHT_FALLING:
					if dx < 0: self.state = Mario.LEFT_FALLING
				else:
					self.state = \
						Mario.LEFT_RUN if dx < 0 else \
						Mario.RIGHT_RUN if dx > 0 else \
						Mario.LEFT_IDLE if ddx > 0 else Mario.RIGHT_IDLE
				
			if (self.prev_state == None):
				self.prev_state = self.state
				
			dy += ddy
			# if (ddy != 0):
			# 	for object in GameWorld.objects_at(GameWorld.layer.platform):
			# 		if "Ladder" in object.name:
			# 			if GameObject.collides_box(self, object):
			# 				(_, bottom, _, top) = object.get_bb()
			# 				(_, foot, _, _) = self.get_bb()
			# 				print("[Foot] : ", foot, ", [Top] : ", top)

			# 				if (ddy > 0 and foot >= top): break
			# 				if (ddy < 0 and foot <= bottom): break
			# 				# 위의 조건식을 써도 KEY_DOWN일 때는 문제가 되지 않는데, KEY_UP이 일어나면서 문제 발생
							
			# 				dy += ddy
			# 				self.state = Mario.CLIMB
							
			# 				if (foot + dy >= top):
			# 					self.state = self.prev_state
			# 					self.prev_state = None
			# 					ddy = 0
			# 					break
							
			self.delta = (dx, dy)

	def update_ladder(self):
		if not self.in_ladder():
			if self.state == Mario.CLIMB:
				self.state = self.prev_state
			return
		x,y = self.pos
		dx,dy = self.delta
		y += dy * Mario.MOVE_PPS * GameFramework.delta_time
		self.pos = x,y

		self.prev_state = self.state
		self.state = Mario.CLIMB

	def in_ladder(self):
		for object in GameWorld.objects_at(GameWorld.layer.platform):
			if "Ladder" in object.name:
				if GameObject.collides_box(self, object):
					return True
		return False


	def jump(self):
		if (self.state in [Mario.LEFT_IDLE, Mario.LEFT_RUN]):
			self.state = Mario.LEFT_JUMP
			self.falling_speed = Mario.JUMP
			Mario.JUMP_WAV.play()
		elif (self.state in [Mario.RIGHT_IDLE, Mario.RIGHT_RUN]):
			self.state = Mario.RIGHT_JUMP
			self.falling_speed = Mario.JUMP
			Mario.JUMP_WAV.play()

	def die(self):
		(x, y) = self.pos
		h = Mario.IMAGE_RECT[self.state][self.fidx % len(Mario.IMAGE_RECT[self.state])][3] // 2

		if (self.state != Mario.DIE):
			if (y + h <= 0):
				y += 200
				self.pos = (x, y)
				self.state = Mario.DIE
				self.falling_speed = 0
				Mario.LIFE_LOST_WAV.play()
			elif (self.is_collide):
				y += 50
				self.pos = (x, y)
				self.state = Mario.DIE
				self.falling_speed = 0
				Mario.LIFE_LOST_WAV.play()
		else:
			(x, y) = self.pos
			y = y + self.falling_speed * GameFramework.delta_time
			self.pos = (x, y)
			self.delta = (0, 0)
			self.falling_speed -= Mario.GRAVITY * GameFramework.delta_time // 10

			if (y + h <= 0): return True

		return False

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (Mario.IMAGE_RECT[self.state][self.fidx % len(Mario.IMAGE_RECT[self.state])][2] // 2, Mario.IMAGE_RECT[self.state][self.fidx % len(Mario.IMAGE_RECT[self.state])][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	def get_platform(self, foot):
		selected = None
		select_top = 0
		(x, y) = self.pos

		for platform in GameWorld.objects_at(GameWorld.layer.platform):
			left, bottom, right, top = platform.get_bb()
			if (x < left or x > right): continue
			if (foot < top - 20): continue
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

		if (pair in Mario.KEY_MAP):
			self.update_delta(*Mario.KEY_MAP[pair])
		elif (pair == Mario.KEY_SPACE):
			self.jump()