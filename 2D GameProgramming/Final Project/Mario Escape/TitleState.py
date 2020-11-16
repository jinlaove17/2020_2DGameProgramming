from pico2d import *
from Background import *
from Button import *
import GameFramework
import GameState
import GameWorld

capture = None

def enter():
	GameWorld.title_init(["background", "ui"])

	background = Background("Image/Title.png")
	background.set_rect(250, 80)
	GameWorld.add(GameWorld.layer.background, background)

	start_button = Button(180, 620, 300, Button.GAME_START)
	GameWorld.add(GameWorld.layer.ui, start_button)

	des_button = Button(90, 620, 200, Button.DESCRIPTION)
	GameWorld.add(GameWorld.layer.ui, des_button)

	exit_button = Button(0, 620, 100, Button.EXIT)
	GameWorld.add(GameWorld.layer.ui, exit_button)

	GameWorld.curr_objects = GameWorld.title_objects

	load_sound()

def update():
	GameWorld.update()

def draw():
	GameWorld.draw()

def handle_event(event):
	global running

	if (event.type == SDL_QUIT):
		GameFramework.quit()

	if (handle_mouse(event)):
		return

def load_sound():
	global bgm, select_wav, move_wav

	bgm = load_music("SOUND/game on boy.mp3")
	select_wav = load_wav("SOUND/game start.wav")
	move_wav = load_wav("SOUND/stomp.wav")

	bgm.set_volume(100)
	bgm.repeat_play()
	

def handle_mouse(event):
	global capture

	if (capture != None):
		holding = capture.handle_event(event)

		if (not holding):
			capture = None
		
		return True

	for object in GameWorld.objects_at(GameWorld.layer.ui):
		if (object.handle_event(event)):
			capture = object

			return True

	return False

def exit():
	pass

def pause():
	pass

def resume():
	pass

if (__name__ == "__main__"):
	GameFramework.run_main()