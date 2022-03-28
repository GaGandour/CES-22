from glob import glob
import turtle # Tess becomes a traffic light.
import threading

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def increase_pen_width():
    global tess
    width = tess.shapesize()[0]
    if width < 20:
        tess.shapesize(width+1)
    print(tess.shapesize()[0])


def decrease_pen_width():
    global tess
    width = tess.shapesize()[0]
    if width > 1:
        tess.shapesize(width-1)
    print(tess.shapesize()[0])

def change_color(color):
    global tess
    tess.fillcolor(color)

# Timer to change the state of the traffic light
def set_timed_traffic_light():
  threading.Timer(5.0, set_timed_traffic_light).start()
  advance_state_machine()

set_timed_traffic_light()

# Go to left or right
def go_left():
    tess.left(90)
    tess.forward(50)
    tess.right(90)

def go_right():
    tess.right(90)
    tess.forward(50)
    tess.left(90)

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.onkey(increase_pen_width, "+")
wn.onkey(decrease_pen_width, "-")
wn.onkey(lambda : change_color("red"), "r")
wn.onkey(lambda : change_color("green"), "g")
wn.onkey(lambda : change_color("blue"), "b")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

wn.listen() # Listen for events
wn.mainloop()