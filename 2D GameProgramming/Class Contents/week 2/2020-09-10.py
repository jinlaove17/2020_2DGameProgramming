Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> pos = turtle.pos()
>>> pos
(0.00,0.00)
>>> pos[0]
0.0
>>> pos[1]
0.0
>>> x, y = pos
>>> x
0.0
>>> y
0.0
>>> pos = 100, 200
>>> pos[1]
200
>>> pos[2]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pos[2]
IndexError: tuple index out of range
>>> x, y = pos
>>> x
100
>>> y
200
>>> pos
(100, 200)
>>> turtle.goto(*pos)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    turtle.goto(*pos)
  File "<string>", line 5, in goto
turtle.Terminator
>>> turtle.goto(*pos)
>>> a = "aaa"
>>> b = "bbb"
>>> a, b = b, a
>>> a
'bbb'
>>> b
'aaa'
>>> a, b, c = "a", "b", "c"
>>> a, b, c = b, c, a
>>> print(a, b, c)
b c a
>>> turtle.setheading(90)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    turtle.setheading(90)
  File "<string>", line 5, in setheading
turtle.Terminator
>>> turtle.setheading(90)
>>> turtle.setheading(180)
>>> turtle.reset()
>>> import random
>>> turtle.shape("turtle")
>>> while (True):
	turtle.setheading(random.randint(0, 50))
	turtle.forward(random.randint(100, 200))
	turtle.stamp()

6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
Traceback (most recent call last):
  File "<pyshell#35>", line 4, in <module>
    turtle.stamp()
  File "<string>", line 5, in stamp
turtle.Terminator
>>> for i in range(5):
	print(i)

0
1
2
3
4
>>> for i in range(0, 5):
	print(i)

0
1
2
3
4
>>> for i in range(0, 10 + 1):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
>>> for n in [1, 3, 4, 5]:
	print(n)

1
3
4
5
>>> for c in "Jeon JongWoo":
	print(c)

J
e
o
n
 
J
o
n
g
W
o
o
>>> for x, y, r in [(200, 200, 50), (-200, -200, 30), (100, 100, 50)]:
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(r)
	turtle.write(str(x, y))

Traceback (most recent call last):
  File "<pyshell#56>", line 6, in <module>
    turtle.write(str(x, y))
TypeError: str() argument 2 must be str, not int
>>> for x, y, r in [(200, 200, 50), (-200, -200, 30), (100, 100, 50)]:
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(r)
	turtle.write(str((x, y)))

Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    turtle.penup()
  File "<string>", line 5, in penup
turtle.Terminator
>>> for x, y, r in [(200, 200, 50), (-200, -200, 30), (100, 100, 50)]:
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(r)
	turtle.write(str((x, y)))

>>> def add(a, b):
	sum = a + b
	return sum

>>> result = sum(30, 60)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    result = sum(30, 60)
TypeError: 'int' object is not iterable
>>> result = add(30, 60)
>>> result
90
>>> def sum_and_mul(a, b):
	return a + b, a * b

>>> a = sum_and_mul(3, 4)
>>> print(a)
(7, 12)
>>> sum, mul = sum_and_mul(100, 200)
>>> print("sum = %d" % sum)
sum = 300
>>> print("mul = %d" % mul)
mul = 20000
>>> add("jong", "Woo")
'jongWoo'
>>> def drunken_move():
	turtle.setheading(random.randint(0, 50))
	turtle.forward(random.randint(100, 200))
	turtle.stamp()

	
>>> turtle.onkey(drunken_move, ' ')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    turtle.onkey(drunken_move, ' ')
  File "<string>", line 5, in onkey
turtle.Terminator
>>> turtle.onkey(drunken_move, ' ')
>>> turtle.iisten()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    turtle.iisten()
AttributeError: module 'turtle' has no attribute 'iisten'
>>> turtle.listen()
>>> turtle.reset()
>>> turtle.onkey(drunken_move, ' ')
>>> def restart():
	turtle.reset()

	
>>> turtle.onkey(restart, "Escape")
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    turtle.onkey(restart, "Escape")
  File "<string>", line 5, in onkey
turtle.Terminator
>>> turtle.onkey(restart, "Escape")
>>> turtle.onkey(drunken_move, ' ')
>>> turtle.reset()
>>> turtle.onkey(drunken_move, ' ')
>>> 