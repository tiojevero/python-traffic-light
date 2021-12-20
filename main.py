import turtle

ts = turtle.Screen()
ts.bgcolor('skyblue')

greenlight = turtle.Turtle()
yellowlight = turtle.Turtle()
redlight = turtle.Turtle()


def draw_housing():
    greenlight.pensize(3)
    greenlight.color('black', 'black')
    greenlight.begin_fill()
    greenlight.forward(80)
    greenlight.left(90)
    greenlight.forward(157)
    greenlight.circle(40, 180)
    greenlight.forward(157)
    greenlight.left(90)
    greenlight.end_fill()


draw_housing()


def circle(t, distance, color):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(distance)
    t.shape('circle')
    t.shapesize(2)
    t.fillcolor(color)


circle(greenlight, 40, 'green')
circle(yellowlight, 100, 'orange')
circle(redlight, 160, 'red')

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num  # The global keyword tells Python not to create a new local variable for state_num

    if state_num == 0:  # Transition from state 0 to state 1
        redlight.color('darkgrey')
        yellowlight.color('darkgrey')
        greenlight.color('green')
        ts.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3000 milliseconds (3 seconds)
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        redlight.color('darkgrey')
        yellowlight.color('orange')
        ts.ontimer(advance_state_machine, 1000)
        state_num = 2
    elif state_num == 2:  # Transition from state 2 to state 3
        greenlight.color('darkgrey')
        ts.ontimer(advance_state_machine, 1000)
        state_num = 3
    else:                 # Transition from state 3 to state 0
        redlight.color('red')
        yellowlight.color('darkgrey')
        ts.ontimer(advance_state_machine, 2000)
        state_num = 0


advance_state_machine()

ts.listen()  # Listen for events

ts.mainloop()  # Wait for user to close window