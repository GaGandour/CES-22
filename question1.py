import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
my_turtle = turtle.Turtle()
my_turtle.color("red")


def draw_square(t: turtle.Turtle, sz):
    for _ in range(4):
        t.forward(sz)
        t.left(90)
    t.goto(t.position() - (10,10))


for i in range(5):
    draw_square(my_turtle, 20*(i+1))

wn.mainloop()
