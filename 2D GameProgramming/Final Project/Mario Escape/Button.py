from pico2d import *
import GameFramework
import GameState
import GameWorld
import GameObject
import TitleState
import Image

LBUTTON_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)
LBUTTON_UP = (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT)

class Button:
	GAME_START, DESCRIPTION, EXIT = range(3)

	def __init__(self, left, bottom, width, x, y, menu):
		self.image = Image.load("IMAGE/TitleMenu.png")
		self.src_rect = (self.left, self.bottom, self.width, self.height) = (left, bottom, width, 90)
		self.pos = (x, y)
		self.menu = menu
		self.mouse_point = None

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

					if (self.menu == Button.EXIT): self.left = 400
					else: self.left = 300

					return self

			if (event.type == SDL_MOUSEMOTION):
				mouse_pos = GameObject.get_pico2d_pos(event)
				in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

				if (in_rect):
					if (self.menu == Button.EXIT): self.left = 400
					else: self.left = 300
					TitleState.in_rect_wav.play()
				else:
					if (self.menu == Button.EXIT): self.left = 100
					else: self.left = 0
					
			self.src_rect = (self.left, self.bottom, self.width, self.height)

			return False

		if (pair == LBUTTON_UP):
			self.mouse_point = None
			mouse_pos = GameObject.get_pico2d_pos(event)
			in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

			if (in_rect):
				if (self.menu == Button.GAME_START):
					GameFramework.change(GameState)
				elif (self.menu == Button.DESCRIPTION):
					pass
				elif (self.menu == Button.EXIT):
					GameFramework.quit()

			return False

		if (event.type == SDL_MOUSEMOTION):
			mouse_pos = GameObject.get_pico2d_pos(event)
			in_rect = GameObject.point_in_rect(mouse_pos, self.get_bb())

			if (in_rect):
				if (self.menu == Button.EXIT): self.left = 400
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