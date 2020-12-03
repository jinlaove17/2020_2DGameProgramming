from pico2d import *
import GameFramework
import GameWorld
import Font

FONT_COLOR = (0, 0, 0)

def enter():
	global background

	background = load_image("IMAGE/Ending.png")

	global font
	
	font = Font.load("FONT/koverwatch.ttf", 30)

	global bgm, clear_wav

	bgm = load_music("SOUND/Ending.mp3")
	clear_wav = load_wav("SOUND/clear.wav")
	
	bgm.repeat_play()
	clear_wav.play()

	global y
	
	y = 0

def update():
	pass

def draw():
	global y

	background.draw(400, 300)

	FPS = 30
	y += FPS * GameFramework.delta_time
	font.draw(480, y, "Mario escaped successfully !", FONT_COLOR)
	font.draw(540, y - 100, "< MARIO ESCAPE >", FONT_COLOR)
	font.draw(480, y - 160, "DIRECTOR : 2017180038 전종우", FONT_COLOR)
	font.draw(450, y - 220, "2D Game Programming Final Project", FONT_COLOR)
	font.draw(560, y - 400, "THANK YOU !", FONT_COLOR)

def handle_event(event):
	if (event.type == SDL_QUIT):
		GameFramework.quit()
	elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		GameFramework.quit()

def exit():
	global background, font, bgm
	del background
	del font
	del bgm

def pause():
	pass

def resume():
	pass

if (__name__ == "__main__"):
	GameFramework.run_main()