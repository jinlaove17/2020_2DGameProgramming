Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pico2d
Pico2d is prepared.
>>> pico2d
<module 'pico2d' from 'D:\\Python\\lib\\site-packages\\pico2d\\__init__.py'>
>>> pico2d.open_canvas()
>>> pico2d.hide_lattice()
>>> pico2d.show_lattice()
>>> pico2d.close_canvas()
>>> import pico2d as p
>>> p.open_canvas()
>>> p.close_canvas()
>>> from random import randint
>>> randint(1, 6)
2
>>> randint(1, 6)
6
>>> random.random()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    random.random()
NameError: name 'random' is not defined
>>> from random import uniform as rndf
>>> rndf(0.1, 0.5)
0.15403934983703219
>>> r = rndf
>>> r(0.4, 0.8)
0.5079230579999989
>>> from random import *
>>> randrange(10, 20)
17
>>> uniform(4.5, 9.5)
8.447663956761659
>>> from pico2d import *
>>> import os
>>> os.getcwd()
'D:\\Python'
>>> os.chdir("D:/Python/2D GameProgramming")
>>> os.getcwd()
'D:\\Python\\2D GameProgramming'
>>> os.listdir()
['.git', '.gitignore', 'homework', 'Image', 'py_02_03_2017180038_1', 'py_02_03_2017180038_2', 'README.md', 'week 1', 'week 2', '이미지 연습용.py']
>>> open_canvas()
>>> ch = load_image("Image/character.png")
>>> ch.draw_now(400, 85)
>>> ch.draw_now(400, 85)
>>> ch.draw_now(500, 85)
>>> for i in range(7):
	ch.draw_now(100 * i, 85)

	
>>> for y in range(100, 500 + 1, 100):
	for x in range(100, 700 + 1, 100):
		ch.draw_now(x, y)

		
>>> for y in range(100, 500 + 1, 100):
	for x in range(100, 700 + 1, 100):
		ch.draw_now(x, y)

		
>>> clear_canvas_now()
>>> for x in range(0, 8 + 1):
	for y in range(0, 6 + 1):
		ch.draw_now(100 * x, 100 * y)

	
>>> for s in range(100, 500 + 1):
	clear_canvas_now()
        for y in range(100, 500 + 1, 100):
	    for x in range(s, 700 + 1, 100):
		ch.draw_now(x, y)
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for s in range(100, 500 + 1):
	clear_canvas_now()
        for y in range(100, 500 + 1, 100):
		for x in range(s, 700 + 1, 100):
			
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for s in range(100, 500 + 1):
	clear_canvas_now()
	for y in range(100, 500 + 1, 100):
		for x in range(s, 700 + 1, 100):
			ch.draw_now(x, y)

>>> for s in range(100, 500 + 1):
	clear_canvas_now()
	for y in range(100, 500 + 1, 100):
		for x in range(s, 700 + 1, 100):
			ch.draw_now(x, y)

			
>>> for s in range(100, 500 + 1):
	#clear_canvas_now()
	for y in range(100, 500 + 1, 100):
		for x in range(s, 700 + 1, 100):
			ch.draw_now(x, y)

			
>>> gra = load_image("Image/grass.png")
>>> gra.draw_now(400, 30)
>>> clear_canvas_now()
>>> gra.draw_now(400, 30)
>>> ch.draw_now(400, 85)
>>> x = 0
>>> while (x < 800):
	clear_canvas_now()
	grass.draw_now(400, 30)
	ch.draw_now(x, 85)
	x += 2
	delay(0.01)

Traceback (most recent call last):
  File "<pyshell#72>", line 3, in <module>
    grass.draw_now(400, 30)
NameError: name 'grass' is not defined
>>> while (x < 800):
	clear_canvas_now()
	gra.draw_now(400, 30)
	ch.draw_now(x, 85)
	x += 2
	delay(0.01)

>>> while (x < 800):
	delay(1)
	clear_canvas_now()
	delay(1)
	gra.draw_now(400, 30)
	delay(1)
	ch.draw_now(x, 85)
	x += 2
	delay(0.01)

	
>>> while (x < 800):
	delay(1)
	clear_canvas_now()
	delay(1)
	gra.draw_now(400, 30)
	delay(1)
	ch.draw_now(x, 85)
	x += 2
	delay(0.01)

	
>>> x = 0
>>> while (x < 800):
	delay(1)
	clear_canvas_now()
	delay(1)
	gra.draw_now(400, 30)
	delay(1)
	ch.draw_now(x, 85)
	x += 2
	delay(0.01)

	

================================ RESTART: Shell ================================
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	x += 2
	delay(0.01)

	
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    while (x < 800):
NameError: name 'x' is not defined
>>> x = 0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	x += 2
	delay(0.01)

Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    clear_canvas()
NameError: name 'clear_canvas' is not defined
>>> open_canvas()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    open_canvas()
NameError: name 'open_canvas' is not defined
>>> from pico2d import *
Pico2d is prepared.
>>> open_canvas()
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	x += 2
	delay(0.01)

Traceback (most recent call last):
  File "<pyshell#91>", line 3, in <module>
    gra.draw(400, 30)
NameError: name 'gra' is not defined
>>> gra = load_image("Image/grass.png")
cannot load Image/grass.png
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    gra = load_image("Image/grass.png")
  File "D:\Python\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> import os
>>> os.chos.getcwd()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    os.chos.getcwd()
AttributeError: module 'os' has no attribute 'chos'
>>> os.getcwd()
'D:\\Python'
>>> os.chdir("D:/Python/2D GameProgramming")
>>> gra = load_image("Image/grass.png")
>>> ch = load_image("Image/character.png")
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	x += 2
	delay(0.01)

	
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	get_events()
	x += 2
	delay(0.01)

	
>>> ㅌ = 0
>>> x = 0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	get_events()
	x += 2
	delay(0.01)

	
[<pico2d.pico2d.Event object at 0x000001DDB1AD39A0>, <pico2d.pico2d.Event object at 0x000001DDB1AD3CD0>, <pico2d.pico2d.Event object at 0x000001DDB1AD32B0>, <pico2d.pico2d.Event object at 0x000001DDB204B790>, <pico2d.pico2d.Event object at 0x000001DDB204B7F0>, <pico2d.pico2d.Event object at 0x000001DDB204B850>, <pico2d.pico2d.Event object at 0x000001DDB204B8B0>, <pico2d.pico2d.Event object at 0x000001DDB204B910>, <pico2d.pico2d.Event object at 0x000001DDB204B940>, <pico2d.pico2d.Event object at 0x000001DDB204B9D0>, <pico2d.pico2d.Event object at 0x000001DDB204BA90>, <pico2d.pico2d.Event object at 0x000001DDB204BA30>, <pico2d.pico2d.Event object at 0x000001DDB204BAF0>, <pico2d.pico2d.Event object at 0x000001DDB204BB50>, <pico2d.pico2d.Event object at 0x000001DDB204BBB0>, <pico2d.pico2d.Event object at 0x000001DDB204BC10>, <pico2d.pico2d.Event object at 0x000001DDB204BC70>, <pico2d.pico2d.Event object at 0x000001DDB204BCD0>, <pico2d.pico2d.Event object at 0x000001DDB204BD30>, <pico2d.pico2d.Event object at 0x000001DDB204BD90>, <pico2d.pico2d.Event object at 0x000001DDB204BDF0>, <pico2d.pico2d.Event object at 0x000001DDB204BEB0>, <pico2d.pico2d.Event object at 0x000001DDB204BE50>, <pico2d.pico2d.Event object at 0x000001DDB204BF10>, <pico2d.pico2d.Event object at 0x000001DDB204BF70>, <pico2d.pico2d.Event object at 0x000001DDB2060070>, <pico2d.pico2d.Event object at 0x000001DDB204BFD0>, <pico2d.pico2d.Event object at 0x000001DDB2060130>, <pico2d.pico2d.Event object at 0x000001DDB20600D0>, <pico2d.pico2d.Event object at 0x000001DDB2060190>, <pico2d.pico2d.Event object at 0x000001DDB20601F0>, <pico2d.pico2d.Event object at 0x000001DDB2060250>, <pico2d.pico2d.Event object at 0x000001DDB20602B0>, <pico2d.pico2d.Event object at 0x000001DDB2060310>, <pico2d.pico2d.Event object at 0x000001DDB2060370>, <pico2d.pico2d.Event object at 0x000001DDB20603D0>, <pico2d.pico2d.Event object at 0x000001DDB2060430>, <pico2d.pico2d.Event object at 0x000001DDB2060490>, <pico2d.pico2d.Event object at 0x000001DDB20604F0>, <pico2d.pico2d.Event object at 0x000001DDB2060550>, <pico2d.pico2d.Event object at 0x000001DDB20605B0>, <pico2d.pico2d.Event object at 0x000001DDB2060610>, <pico2d.pico2d.Event object at 0x000001DDB2060670>, <pico2d.pico2d.Event object at 0x000001DDB20606D0>, <pico2d.pico2d.Event object at 0x000001DDB2060730>, <pico2d.pico2d.Event object at 0x000001DDB2060790>, <pico2d.pico2d.Event object at 0x000001DDB2060850>, <pico2d.pico2d.Event object at 0x000001DDB20607F0>, <pico2d.pico2d.Event object at 0x000001DDB20608B0>, <pico2d.pico2d.Event object at 0x000001DDB2060910>, <pico2d.pico2d.Event object at 0x000001DDB20609D0>, <pico2d.pico2d.Event object at 0x000001DDB2060970>, <pico2d.pico2d.Event object at 0x000001DDB2060A30>, <pico2d.pico2d.Event object at 0x000001DDB2060A90>, <pico2d.pico2d.Event object at 0x000001DDB2060AF0>, <pico2d.pico2d.Event object at 0x000001DDB2060B50>, <pico2d.pico2d.Event object at 0x000001DDB2060BB0>]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CD0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD39A0>, <pico2d.pico2d.Event object at 0x000001DDB204B7F0>, <pico2d.pico2d.Event object at 0x000001DDB204B7C0>]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD39A0>]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD39A0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CD0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD39A0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CD0>]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CD0>]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[]
[]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>, <pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3C70>]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>, <pico2d.pico2d.Event object at 0x000001DDB204B7C0>]
[]
[<pico2d.pico2d.Event object at 0x000001DDB1AD3CA0>]
[]
[]
[]
[]
[]
>>> x = 0
>>> ani = load_image("Image/animation_sheet.png")
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(0, 0, 100, 100, x, 85)
	update_canvas()
	x += 2
	delay(0.01)

	
>>> ani = load_image("Image/run_animation.png")
>>> x = 0
>>> sx = 0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(sx, 0, 100, 100, x, 85)
	update_canvas()
	x += 2
	sx += 100
	delay(0.01)

	
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(sx, 0, 100, 100, x, 85)
	update_canvas()
	x += 2
	sx += 100
	delay(0.01)

	
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(sx, 0, 100, 100, x, 85)
	update_canvas()
	x += 2
	sx += 100
	delay(0.01)

	
>>> x = 0
>>> sx =0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(sx, 0, 100, 100, x, 85)
	update_canvas()
	x += 2
	sx += 100
	if sx >= 800: sx = 0
	delay(0.01)

	
>>> x = 0
>>> frame = 0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(100 * frame, 0, 100, 100, x, 85)
	update_canvas()
	x += 2
	frame = (frame + 1) % 8
	delay(0.01)

	
>>> x = 0
>>> frame = 0
>>> action = 0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(100 * frame, 100 * action, 100, 100, x, 85)
	update_canvas()
	x += 2
	frame = (frame + 1) % 8
	if x % 100 == 0: (action + 1) % 4
	delay(0.01)

	
1
1
1
1
1
1
1
1
>>> x = 0
>>> frame = 0
>>> action = 0
>>> ani = ani = load_image("Image/animation_sheet.png")
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(100 * frame, 100 * action, 100, 100, x, 85)
	update_canvas()
	x += 2
	frame = (frame + 1) % 8
	if x % 100 == 0: (action + 1) % 4
	delay(0.01)

	
1
1
1
1
1
1
1
1
>>> x = 0
>>> frame = 0
>>> action = 0
>>> while (x < 800):
	clear_canvas()
	gra.draw(400, 30)
	ani.clip_draw(100 * frame, 100 * action, 100, 100, x, 85)
	update_canvas()
	x += 2
	frame = (frame + 1) % 8
	if x % 100 == 0: action = (action + 1) % 4
	delay(0.01)

	
>>> 