import turtle

# 터틀의 초기위치를 설정하는 함수
def set_turtle():
    turtle.penup()
    turtle.goto(-280, 100)
    turtle.pendown()

# 가로 선을 긋는 함수
def write_row(count):
    for i in range(count + 1):
        turtle.penup()
        turtle.goto(-250, 250 - 100 * i)
        turtle.pendown()
        turtle.forward(500)
        
# 세로 선을 긋는 함수
def write_cul(count):
    for i in range(count + 1):
        turtle.penup()
        turtle.goto(-250 + 100 * i, 250)
        turtle.pendown()
        turtle.forward(500)
        
set_turtle()
write_row(5)
set_turtle()
turtle.setheading(-90)
write_cul(5)
turtle.exitonclick()
