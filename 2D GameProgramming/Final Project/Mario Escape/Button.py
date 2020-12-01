from pico2d import *
import GameFramework
import GameState
import GameObject
import Image

GAME_START, DESCRIPTION, EXIT = range(3)
LBUTTON_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)
LBUTTON_UP = (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT)

class Button:
	OFF_IMAGE_RECT = [
		# GAME START
		(19, 130, 258, 35),
		# DESCRIPTION
		(15, 70, 267, 35),
		# EXIT
		(100, 10, 96, 35)
		]
	ON_IMAGE_RECT = [
		# GAME START
		(315, 128, 263, 39),
		# DESCRIPTION
		(310, 69, 273, 39),
		# EXIT
		(395, 8, 103, 39)
		]
	SELECT_WAV = None
	IS_DES_DRAW = False
	DES_IMAGE = None
	DES_ON_WAV = None
	DES_OFF_WAV = None

	def __init__(self, x, y, menu):
		self.pos = (x, y)
		self.menu = menu
		self.rect = Button.OFF_IMAGE_RECT[self.menu]
		self.image = Image.load("IMAGE/TitleMenu.png")
		self.mouse_point = None

		if (Button.SELECT_WAV == None):
			Button.SELECT_WAV = load_wav("SOUND/stomp.wav")

		if (Button.DES_IMAGE == None):
			Button.DES_IMAGE = Image.load("IMAGE/Description.png")

		if (Button.DES_ON_WAV == None or Button.DES_OFF_WAV == None):
			Button.DES_ON_WAV = load_wav("SOUND/description_on.wav")
			Button.DES_OFF_WAV = load_wav("SOUND/description_off.wav")

	def draw(self):
		self.image.clip_draw(*self.rect, *self.pos)

		if (Button.IS_DES_DRAW):
			Button.DES_IMAGE.draw(get_canvas_width() // 2, get_canvas_height() // 2)

	def update(self):
		pass

	def handle_event(self, event):
		pair = (event.type, event.button)

		if (self.mouse_point == None):
			if (pair == LBUTTON_DOWN):
				if (GameObject.point_in_rect(GameObject.get_pico2d_pos(event), self.get_bb())):
					self.mouse_point = GameObject.get_pico2d_pos(event)
					self.rect = Button.ON_IMAGE_RECT[self.menu]

					return self

			if (event.type == SDL_MOUSEMOTION):
				mouse_pos = GameObject.get_pico2d_pos(event)
				in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

				if (in_rect):
					self.rect = Button.ON_IMAGE_RECT[self.menu]
					Button.SELECT_WAV.play()
				else:
					self.rect = Button.OFF_IMAGE_RECT[self.menu]
					
			return False

		if (pair == LBUTTON_UP):
			self.mouse_point = None
			mouse_pos = GameObject.get_pico2d_pos(event)
			in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

			if (in_rect):
				if (self.menu == GAME_START):
					GameFramework.push(GameState)
				elif (self.menu == DESCRIPTION):
					Button.IS_DES_DRAW = True
					Button.DES_ON_WAV.play()
				elif (self.menu == EXIT):
					GameFramework.quit()

			return False

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (self.rect[2], self.rect[3])

		left = x - w // 2 
		bottom = y - h // 2
		right = x + w // 2
		top = y + h // 2

		return (left, bottom, right, top)