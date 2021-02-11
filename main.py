import turtle as trtl
import random
wn = trtl.Screen()
#---------Setup---------
wn.addshape("Main_Character.gif")
player = trtl.Turtle()
player.pu()
player.shape("Main_Character.gif")

vertical = 1000
horizontal = 1800
drawer = trtl.Turtle()
drawer.pu()
drawer.speed(0)
drawer.goto(1920,vertical)
drawer.pendown()

#---------Functions---------
def draw_gridx():
    global vertical
    for i in range(20):
        wn.tracer(False)
        drawer.setheading(0)
        drawer.goto(-1920,vertical)
        vertical = vertical - 80
        drawer.goto(-1920,vertical)
        drawer.goto(1920,vertical)
    wn.tracer(True)

def draw_gridy():
    global horizontal
    for i in range(80):
        wn.tracer(False)
        drawer.setheading(0)
        drawer.goto(horizontal,-1080)
        horizontal = horizontal - 80
        drawer.goto(horizontal,-1080)
        drawer.goto(horizontal,1080)
    wn.tracer(True)

def bound():
    x = player.xcor()
    y = player.ycor()
    if x > 880:
        player.goto((x-80)*-1,y)
    if x < -880:
        player.goto((x+80)*-1,y)
    if y > 480:
        player.goto(x,(y-80)*-1)
    if y < -480:
        player.goto(x,(y+80)*-1)
    

def up():
    wn.tracer(False)
    player.setheading(90)
    player.forward(80)
    bound()
    wn.tracer(True)
def down():
    wn.tracer(False)
    player.setheading(270)
    player.forward(80)
    bound()
    wn.tracer(True)
def left():
    wn.tracer(False)
    player.setheading(180)
    player.forward(80)
    bound()
    wn.tracer(True)
def right():
    wn.tracer(False)
    player.setheading(0)
    player.forward(80)
    bound()
    wn.tracer(True)

#---------Main---------
draw_gridx()
drawer.pu()
drawer.goto(horizontal, 1080)
drawer.pendown()
draw_gridy()

wn.onkeypress(up,'w')
wn.onkeypress(down,'s')
wn.onkeypress(left,'a')
wn.onkeypress(right,'d')

wn.listen()
wn.mainloop()
