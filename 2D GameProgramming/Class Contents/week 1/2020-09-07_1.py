Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name1 = "Trump"
>>> name2 = "강다니엘"
>>> print(name1)
Trump
>>> print(name2)
강다니엘
>>> pi = 3.14
>>> a= p = pi
>>> a
3.14
>>> p
3.14
>>> s = "Hello"
>>> s
'Hello'
>>> d = 'Hello'
>>> d
'Hello'
>>> s = "Hello \"Dave\""
>>> s
'Hello "Dave"'
>>> d = 'Hello "Dave"'
>>> d
'Hello "Dave"'
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 10.0
>>> type(a)
<class 'float'>
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> a = 10 > 3
>>> a
True
>>> type(a)
<class 'bool'>
>>> first = "JongWoo"
>>> last = "Jeon"
>>> name = first + " " + last
>>> print(name)
JongWoo Jeon
>>> name * 2
'JongWoo JeonJongWoo Jeon'
>>> name * 3
'JongWoo JeonJongWoo JeonJongWoo Jeon'
>>> name[0]
'J'
>>> name[8]
'J'
>>> name[-1]
'n'
>>> name[-2]
'o'
>>> title = "Python 2D Game Programming"
>>> title[0:6]
'Python'
>>> title[7:9]
'2D'
>>> title[10:14]
'Game'
>>> title[:6]
'Python'
>>> title[-11:]
'Programming'
>>> title[::2]
'Pto DGm rgamn'
>>> title[::-1]
'gnimmargorP emaG D2 nohtyP'
>>> title[::-2]
'gimroPea 2nhy'
>>> twice = ["momo", "sana", "zwi", "nayun", "dahyun"]
>>> black_pink = ["jisu", "jeni", "rose", "risa"]
>>> twice
['momo', 'sana', 'zwi', 'nayun', 'dahyun']
>>> twice.append("jihyo")
>>> twice
['momo', 'sana', 'zwi', 'nayun', 'dahyun', 'jihyo']
>>> twice.sort()
>>> twice
['dahyun', 'jihyo', 'momo', 'nayun', 'sana', 'zwi']
>>> len(twice)
6
>>> unite = twice + black_pink
>>> unite
['dahyun', 'jihyo', 'momo', 'nayun', 'sana', 'zwi', 'jisu', 'jeni', 'rose', 'risa']
>>> unite.remove("momo")
>>> unite
['dahyun', 'jihyo', 'nayun', 'sana', 'zwi', 'jisu', 'jeni', 'rose', 'risa']
>>> unite[0]
'dahyun'
>>> unite[-1]
'risa'
>>> unite[:3]
['dahyun', 'jihyo', 'nayun']
>>> untie[-3:]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    untie[-3:]
NameError: name 'untie' is not defined
>>> unite[-3:]
['jeni', 'rose', 'risa']
>>> score = {"momo" : 80, "zwi" : 85, "sana" : 98 }
>>> type(score)
<class 'dict'>
>>> score["momo"]
80
>>> score["nayun"]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    score["nayun"]
KeyError: 'nayun'
>>> score["nayun"] = 100
>>> score
{'momo': 80, 'zwi': 85, 'sana': 98, 'nayun': 100}
>>> del score["momo"]
>>> score
{'zwi': 85, 'sana': 98, 'nayun': 100}
>>> score.keys()
dict_keys(['zwi', 'sana', 'nayun'])
>>> score.values()
dict_values([85, 98, 100])
>>> "zwi" in score
True
>>> "momo" in score
False
>>> score.clear()
>>> score
{}
>>> a = 10. 10
SyntaxError: invalid syntax
>>> a = 10, 10
>>> a
(10, 10)
>>> a = 10, 20, 30
>>> a
(10, 20, 30)
>>> a = [10, 20, 30, 40, 50]
>>> a
[10, 20, 30, 40, 50]
>>> x = 10
>>> y = 20
>>> pos = 10, 20
>>> pos
(10, 20)
>>> pos = 30, 40
>>> x, y = pos
>>> x, y
(30, 40)
>>> pos = 100, 200
>>> x, y = pos
>>> x, y
(100, 200)
>>> pos[0]
100
>>> pos[1]
200
>>> t1 = (1, 2, 3)
>>> t2 = (1,)
>>> t3 = ()
>>> t4 = 1, 2, 3, 4
>>> type(t3)
<class 'tuple'>
>>> type(t4)
<class 'tuple'>
>>> t5 = (1, 'a', "Park", (1, 2))
>>> t1 + t5
(1, 2, 3, 1, 'a', 'Park', (1, 2))
>>> t4 * t4
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    t4 * t4
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> t4 * 3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> style = {"bold", "italic", "underline"}
>>> style
{'underline', 'italic', 'bold'}
>>> new_style = style | {"strike"}
>>> new_style
{'underline', 'italic', 'strike', 'bold'}
>>> "strike" in new_style
True
>>> "strike" in style
False
>>> s1 = {1, 2, 3}
>>> type(s1)
<class 'set'>
>>> s1 = {1, 2, 2, 4}
>>> s1
{1, 2, 4}
>>> l1 = {1, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 5}
>>> s1 = set(l1)
>>> s1
{1, 2, 3, 5}
>>> s2 = {3, 5, 6, 7}
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1 | s2
{1, 2, 3, 5, 6, 7}
>>> s1 & s2
{3, 5}
>>> s2 - s1
{6, 7}
>>> s1 - s2
{1, 2}
>>> s1.add(8)
>>> s1
{1, 2, 3, 5, 8}
>>> s2.remove(6)
>>> s2
{3, 5, 7}
>>> 