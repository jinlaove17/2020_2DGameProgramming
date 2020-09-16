import turtle

# 이름을 적을 시작좌표를 설정
init_x = -200
init_y = 0

# 펜의 위치를 설정하는 함수
def set_pos(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)

# 자음 'ㅈ'을 그리는 함수
def write_ja1():
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(60)
    turtle.backward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.backward(60)
    turtle.left(60)
    turtle.forward(40)
    
# 자음 'ㄴ'을 그리는 함수
def write_ja2():
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(70)

# 자음 'ㅇ'을 그리는 함수
def write_ja3():
    turtle.circle(25)

# 모음 'ㅓ'를 그리는 함수
def write_mo1():
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.backward(80)

# 모음 'ㅗ'를 그리는 함수
def write_mo2():
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(100)

# 모음 'ㅜ'를 그리는 함수
def write_mo3():
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.backward(60)
    turtle.left(90)
    turtle.forward(50)

turtle.speed(0)

set_pos(init_x, init_y)
write_ja1()

set_pos(init_x + 60, init_y - 25)
write_mo1()

set_pos(init_x + 40, init_y - 60)
write_ja2()

set_pos(init_x + 160, init_y)
write_ja1()

set_pos(init_x + 200, init_y - 30)
write_mo2()

set_pos(init_x + 200, init_y - 110)
write_ja3()

set_pos(init_x + 340, init_y - 40)
write_ja3()

set_pos(init_x + 290, init_y - 55)
write_mo3()

turtle.exitonclick()
