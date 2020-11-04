from pico2d import *
import GameFramework
import GameObject
import GameState

class Mario:
	# State
	LEFT_IDLE = 0
	RIGHT_IDLE = 1
	LEFT_RUN = 2
	RIGHT_RUN = 3
	LEFT_JUMP = 4
	RIGHT_JUMP = 5
	CLIMB = 6
	DIE = 7

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

		# Climb
		[ (253, 91, 48, 76), (323, 92, 46, 74) ],

		# Die
		[ (245, 4, 57, 78), (324, 6, 57, 80) ]
	]

	def __init__(self):
		self.pos = (100, 140)
		self.delta = (0, 0)
		self.fidx = 0
		self.time = 0
		self.state = Mario.RIGHT_IDLE
		self.image = load_image("image/Mario.png")

	def draw(self):
		 self.image.clip_draw(*Mario.IMAGE_RECT[self.state][self.fidx], *self.pos)

	def update(self):
		x, y = self.pos
		dx, dy = self.delta
		self.pos = x + dx, y + dy
		self.time += GameFramework.delta_time
		self.fidx = int(self.time * 7) % len(Mario.IMAGE_RECT[self.state])
		
	def update_delta(self, ddx, ddy):
		dx, dy = self.delta
						
		if (ddx != 0):
			dx += 3 * ddx
			self.state = \
				Mario.LEFT_RUN if dx < 0 else \
				Mario.RIGHT_RUN if dx > 0 else \
				Mario.LEFT_IDLE if ddx > 0 else Mario.RIGHT_IDLE

		for object in GameState.interact_object:
			if GameObject.collides_box(self, object):
				if (ddy != 0 ):
					dy += 3 * ddy
					self.state = Mario.CLIMB
					print("Climb ladder")

		self.delta = dx, dy

	def get_bb(self):
		x, y = self.pos
		w, h = (Mario.IMAGE_RECT[self.state][self.fidx][2] // 2, Mario.IMAGE_RECT[self.state][self.fidx][3] // 2)

		left = x - w
		bottom = y - h
		right = x + w
		top = y + h

		return (left, bottom, right, top)

	def handle_event(self, event):
		pair = (event.type, event.key)

		if pair in Mario.KEY_MAP:
			self.update_delta(*Mario.KEY_MAP[pair])
		elif (pair == Mario.KEY_SPACE):
			pass
