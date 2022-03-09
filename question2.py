import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
my_turtle = turtle.Turtle()
my_turtle.color("red")


def draw_poly(t: turtle.Turtle, n , sz):
    for _ in range(n):
        angle = 360/n
        t.forward(sz)
        t.left(angle)


draw_poly(my_turtle, 8, 50)

wn.mainloop()
