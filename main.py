import turtle

bob = turtle.Turtle()


def draw_bob(left_or_right, angle, length):
    if left_or_right == "right":
        bob.right(angle)
    else:
        bob.left(angle)

    bob.forward(length)


def draw_turtle(left_or_right, angle, length):
    if left_or_right == "right":
        turtle.right(angle)
    else:
        turtle.left(angle)

    turtle.forward(length)


#Создание вилки для розетки
bob.fillcolor("#FF7A00")
bob.begin_fill()

draw_bob("left",180,80)
draw_bob("right",90,30)
draw_bob("right",90,80)
draw_bob("left",90,30)
draw_bob("left",90,80)
draw_bob("right",90,30)
draw_bob("right",90,80)
bob.end_fill()

#Создание корпуса вилки
bob.fillcolor("#C7C7C7")
bob.begin_fill()

draw_bob("left",90,20)
draw_bob("right",90,120)
draw_bob("right",90,140)
draw_bob("right",90,90)
draw_bob("left",90,20)
draw_bob("left",90,110)
draw_bob("right",90,20)
draw_bob("right",90,130)
draw_bob("right",90,40)
draw_bob("left",90,10)
draw_bob("right",90,140)
draw_bob("right",90,50)
draw_bob("right",90,140)
draw_bob("left",180,30)
bob.end_fill()

#Внутренняя часть вилки
bob.fillcolor("#6C6C6C")
bob.begin_fill()
draw_bob("right",45,20)
draw_bob("left",45,60)
draw_bob("left",45,20)
draw_bob("left",135,90)
bob.end_fill()
bob.begin_fill()
draw_bob("right",150,15)
draw_bob("right",30,60)
draw_bob("right",30,15)
draw_bob("right",150,90)
bob.end_fill()
turtle.done()