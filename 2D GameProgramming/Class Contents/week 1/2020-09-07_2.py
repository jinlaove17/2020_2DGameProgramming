Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle
<module 'turtle' from 'D:\\Python\\lib\\turtle.py'>
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.shape("turtle")
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(30)
>>> turtle.forward(100)
>>> turtle.left(120)
>>> turtle.forward(100)
>>> turtle.reset()
>>> for i in range(4):
	turtle.forward(100)
	turtle.left(90)

>>> turtle.reset()
>>> for i in range(3):
	turtle.forward(100)
	turtle.left(120)

>>> turtle.reset()
>>> for i in range(5):
	turtle.forward(100)
	turtle.left(72)

>>> turtle.reset()
>>> 
>>> for i in range(5):
	turtle.forward(100)
	turtle.left(144)

	
>>> turtle.reset()
>>> for i in range(6):
	turtle.forward(100)
	turtle.left(60)

>>> turtle.reset()
>>> turtle.circle(200)
turtle.right(90)
>>> turtle.right(90)
>>> turtle.circle(144)
>>> turtle.undo
<function undo at 0x000002A0D01131F0>
>>> turtle.undo()
>>> turtle.goto(100, 100)
>>> turtle.undo()
>>> turtle.reset()
>>> turtle.forward(100)
>>> turtle.penup()
>>> turtle.forward(50)
>>>  turtle.pendown()
 
SyntaxError: unexpected indent
>>> turtle.pendown()
>>> turtle.forward(100)
>>> turtle.reset()
>>> import random
>>> random
<module 'random' from 'D:\\Python\\lib\\random.py'>
>>> random.randint(10, 20)
14
>>> random.randint(10, 20)
14
>>> random.randint(10, 20)
18
>>> random.randint(10, 20)
11
>>> random.randint(10, 20)
12
>>> random.randint(10, 20)
19
>>> freq = [0, 0, 0, 0, 0, 0]
>>> for i in range(1000):
	freq[random.randint(0, 5)] += 1

	
>>> freq
[174, 162, 149, 189, 160, 166]
>>> random.uniform(10, 20)
16.052243400302416
>>> random.uniform(10, 20)
10.951898773431239
>>> random.random()
0.9237230919611458
>>> mins = input("Enter hour : ")
Enter hour : 4
>>> sec = mins * 60
>>> print(sec)
444444444444444444444444444444444444444444444444444444444444
>>> print((int)sec)
SyntaxError: invalid syntax
>>> sec = (int)sec
SyntaxError: invalid syntax
>>> sec = int(sec)
>>> print(sec)
444444444444444444444444444444444444444444444444444444444444
>>> type(sec)
<class 'int'>
>>> sec = mins * 60
>>> type(sec)
<class 'str'>
>>> sec = int(sec)
>>> print(sec)
444444444444444444444444444444444444444444444444444444444444
>>> sec = mins * 60
>>> mins = int(mins)
>>> mins
4
>>> sec = int(sec)
>>> print(sec)
444444444444444444444444444444444444444444444444444444444444
>>> sec = mins * 60
>>> print(sec)
240
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
>>> type(sec)
<class 'int'>
>>> str(sec)
'240'
>>> "elpased : " + sec + "seconds"
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    "elpased : " + sec + "seconds"
TypeError: can only concatenate str (not "int") to str
>>> "elpased : " + str(sec) + "seconds"
'elpased : 240seconds'
>>> 4 > 3
True
>>> 3.5 < -1.3
False
>>> 100 == 100
True
>>> 10 >= 10
True
>>> a = 365 > 366
>>> print(a)
False
>>> type(a)
<class 'bool'>
>>> "KOREA" == "korea"
False
>>> 'abcd' == "abcd"
True
>>> age = 23
>>> if (age >= 60):
	print(age)
	print("You are very old")

	
>>> age = 100
>>> if (age >= 60):
	print(age)
	print("You are very old")

100
You are very old
>>> if (age >= 60):
	print(age)
	print("You're very old")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if (age >= 60):
	print(age)
	print("You're very old")
	else:
		
SyntaxError: invalid syntax
>>> if (age >= 60):
	print(age)
	print("You're very old")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if (age >= 60):
	print(age)
	print("You're very old")
     else:
	     
SyntaxError: unindent does not match any outer indentation level
>>> if (age >= 60):
	print(age)
	print("You're very old")else:
		
SyntaxError: invalid syntax
>>> if (age >= 60):
	print(age)
	print("You're very old")
else:
	print(age)
	print("You're young")

	
100
You're very old
>>> if (age >= 60):
	print(age)
	print("You're very old")
elif (age <= 20):
	print(age)
	print("You're very young")
else
SyntaxError: invalid syntax
>>> if (age >= 60):
	print(age)
	print("You're very old")
elif (age <= 20):
	print(age)
	print("You're very young")
else:
	print(age)
	print("You're young")

100
You're very old
>>> age_str = input("Enter Your Age : ")
Enter Your Age : 23
>>> age = int(age_str)
>>> if (age <= 6):
	print("Bus is free.")
elif (age <= 12):
	print("Bus fare is 450 won.")
elif (age <= 18):
	print("Bus fare is 720 won.")
elif (age <= 64):
	print("Bus fare is 1200 won.")
	else:
		
SyntaxError: invalid syntax
>>> if (age <= 6):
	print("Bus is free.")
elif (age <= 12):
	print("Bus fare is 450 won.")
elif (age <= 18):
	print("Bus fare is 720 won.")
elif (age <= 64):
	print("Bus fare is 1200 won.")
else:
	print("Bus is free")

Bus fare is 1200 won.
>>> import turtle
>>> count = 10
>>> while (count > 0):
	turtle.forward(100)
	turtle.left(30)
	count -= 1

Traceback (most recent call last):
  File "<pyshell#150>", line 2, in <module>
    turtle.forward(100)
  File "<string>", line 5, in forward
turtle.Terminator
>>> while (count > 0):
	turtle.forward(100)
	turtle.left(30)
	count = count - 1

>>> 