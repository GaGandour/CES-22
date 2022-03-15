import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
my_turtle = turtle.Turtle()
my_turtle.color("magenta")
my_turtle.pensize(3)


def draw_square(t: turtle.Turtle, sz):
    for _ in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.goto(t.position() - (10,10))
    t.pendown()


for i in range(5):
    draw_square(my_turtle, 20*(i+1))

wn.mainloop()
