from pico2d import *
import GameFramework
import GameState
import GameObject
import Image

GAME_START, DESCRIPTION, EXIT = range(3)
LBUTTON_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)
LBUTTON_UP = (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT)

class Button:
	SELECT_WAV = None

	def __init__(self, left, bottom, width, x, y, menu):
		self.image = Image.load("IMAGE/TitleMenu.png")
		self.src_rect = (self.left, self.bottom, self.width, self.height) = (left, bottom, width, 90)
		self.pos = (x, y)
		self.menu = menu
		self.mouse_point = None

		if (Button.SELECT_WAV == None):
			Button.SELECT_WAV = load_wav("SOUND/stomp.wav")

	def draw(self):
		self.image.clip_draw(*self.src_rect, *self.pos)

	def update(self):
		pass

	def handle_event(self, event):
		pair = (event.type, event.button)

		if (self.mouse_point == None):
			if (pair == LBUTTON_DOWN):
				if (GameObject.point_in_rect(GameObject.get_pico2d_pos(event), self.get_bb())):
					self.mouse_point = GameObject.get_pico2d_pos(event)

					if (self.menu == EXIT): self.left = 400
					else: self.left = 300

					return self

			if (event.type == SDL_MOUSEMOTION):
				mouse_pos = GameObject.get_pico2d_pos(event)
				in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

				if (in_rect):
					if (self.menu == EXIT): self.left = 400
					else: self.left = 300
					Button.SELECT_WAV.play()
				else:
					if (self.menu == EXIT): self.left = 100
					else: self.left = 0
					
			self.src_rect = (self.left, self.bottom, self.width, self.height)

			return False

		if (pair == LBUTTON_UP):
			self.mouse_point = None
			mouse_pos = GameObject.get_pico2d_pos(event)
			in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

			if (in_rect):
				if (self.menu == GAME_START):
					GameFramework.push(GameState)
				elif (self.menu == DESCRIPTION):
					pass
				elif (self.menu == EXIT):
					GameFramework.quit()

			return False

		if (event.type == SDL_MOUSEMOTION):
			mouse_pos = GameObject.get_pico2d_pos(event)
			in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

			if (in_rect):
				if (self.menu == EXIT): self.left = 400
				else: self.left = 300
				self.src_rect = (self.left, self.bottom, self.width, self.height)

			return False

	def get_bb(self):
		(x, y) = self.pos
		(w, h) = (self.width, self.height)

		left = x - w // 2 
		bottom = y - h // 2
		right = x + w // 2
		top = y + h // 2

		return (left, bottom, right, top)