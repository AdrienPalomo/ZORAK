import turtle as trtl
import random
import sys
import time
wn = trtl.Screen()
wn.bgpic("background.gif")
#---------Setup---------
wn.tracer(False)

wn.addshape("Main_Character.gif")
wn.addshape("Enemy.gif")
wn.addshape("Ball.gif")

player = trtl.Turtle()
player.pu()
player.shape("Main_Character.gif")

ball = trtl.Turtle()
ball.pu()
ball.shape("Ball.gif")
ball.hideturtle()
ball.speed(7)

enemy = trtl.Turtle()
enemy.pu()
enemy.shape("Enemy.gif")
enemy.goto(240,0)

player_health = 3
player_hp = trtl.Turtle()
player_hp.color("red")
player_hp.hideturtle()
player_hp.pu()
player_hp.goto(-950,440)

wait = 0

attack_status = 0

direction = 0

hold = "placeholder"

menu_status = 0

vertical = 1000
horizontal = 1800
drawer = trtl.Turtle()
drawer.hideturtle
drawer.color("white")
drawer.pu()
drawer.speed(0)

wn.tracer(True)
#---------Functions---------
def ball_animation(heading):
    global attack_status
    attack_status = hold
    attack_status = 2
    x = player.xcor()
    y = player.ycor()
    ball.goto(x,y)
    ball.setheading(heading)
    ball.showturtle()
    ball.forward(2000)
    ball.hideturtle()
    attack_status = hold

def hurt_animation(sprite):
    global attack_status
    attack_status = 2
    for i in range(5):
        sprite.hideturtle()
        time.sleep(.01)
        sprite.showturtle()
        time.sleep(.01)
    attack_status = 0

def enemy_attack():
    global player_health, wait
    xe = enemy.xcor()
    ye = enemy.ycor()
    x = player.xcor()
    y = player.ycor()
    if wait > 0:
        wait = wait - 1
    if abs(xe - x) <= 80 and abs(ye - y) <= 80 and wait == 0:
        wait = 3
        player_health = player_health - 1
        hurt_animation(player)
        display_health()

def enemy_move():
    global wait
    wn.tracer(False)
    xe = enemy.xcor()
    ye = enemy.ycor()
    x = player.xcor()
    y = player.ycor()
    if wait == 0:
        if xe - x > 0:
            if ye - y < 0:
                if (xe - x) > (ye - y) * -1:
                    enemy.goto(xe-80,ye)
                elif (xe - x) < (ye - y) * -1:
                    enemy.goto(xe,ye + 80)
                elif (xe - x) == (ye - y) * -1:
                    enemy.goto(xe - 80, ye)
            elif ye - y > 0:
                if (xe - x) > (ye - y):
                    enemy.goto(xe-80,ye)
                elif (xe - x) < (ye - y):
                    enemy.goto(xe, ye - 80)
                elif (xe - x) == (ye - y):
                    enemy.goto(xe - 80, ye)
            elif ye - y == 0:
                enemy.goto(xe - 80, ye)  
        elif xe - x < 0:
            if ye - y < 0:
                if (xe - x) * -1 > (ye - y) * -1:
                    enemy.goto(xe + 80,ye)
                elif (xe - x) * -1 < (ye - y) * -1:
                    enemy.goto(xe,ye+80)
                elif (xe - x) == (ye - y):
                    enemy.goto(xe + 80, ye)
            elif ye - y > 0:
                if (xe - x) * -1 > (ye - y):
                    enemy.goto(xe + 80,ye)
                elif (xe - x) * -1 < (ye - y):
                    enemy.goto(xe,ye-80)
                elif (xe - x) * -1 == (ye - y):
                    enemy.goto(xe + 80, ye)
            elif ye - y == 0:
                enemy.goto(xe + 80, ye)
        elif xe == x:
            if ye - y < 0:
                enemy.goto(xe, ye + 80)
            elif ye - y > 0:
                enemy.goto(xe, ye - 80)
            elif ye == y:
                pass
    wn.tracer(True)

def player_attack(direction):
    global attack_status
    if attack_status == 1:
        xe = enemy.xcor()
        ye = enemy.ycor()
        x = player.xcor()
        y = player.ycor()
        xf = xe - x
        yf = ye - y

        if direction == 1:
            ball_animation(90)
        elif direction == 2:
            ball_animation(270)
        elif direction == 3:
            ball_animation(180)
        elif direction == 4:
            ball_animation(0)

        if (direction == 1) and (xf <= 40) and (xf >= -40) and (yf >= 0):
            wn.tracer(False)
            enemy.goto(99999999999999,99999999999999)
            wn.tracer(True)
        elif (direction == 2) and (xf <= 40) and (xf >= -40) and (yf <= 0):
            hurt_animation(enemy)
            wn.tracer(False)
            enemy.goto(99999999999999,99999999999999)
            wn.tracer(True)
        elif direction == 3 and (yf <= 40) and (yf >= -40) and (xf <= 0):
            hurt_animation(enemy)
            wn.tracer(False)
            enemy.goto(99999999999999,99999999999999)
            wn.tracer(True)
        elif direction == 4 and (yf <= 40) and (yf >= -40) and (xf >= 0):
            hurt_animation(enemy)
            wn.tracer(False)
            enemy.goto(99999999999999,99999999999999)
            wn.tracer(True)
    attack_status = 0
    player.shape("Main_Character.gif")
    enemy_move()
    time.sleep(.05)
    enemy_attack()

def set_attack():
    global attack_status
    if attack_status == 0:
        attack_status = 1
        player.shape("Enemy.gif")
    elif attack_status == 1:
        attack_status = 0
        player.shape("Main_Character.gif")

def set_up():
    global attack_status
    if attack_status == 1:
        #direction = 1
        player_attack(1)

def set_down():
    global attack_status
    if attack_status == 1:
        #direction = 2
        player_attack(2)

def set_left():
    global attack_status
    if attack_status == 1:
        #direction = 3
        player_attack(3)

def set_right():
    global attack_status
    if attack_status == 1:
        #direction = 4
        player_attack(4)
     
def display_health():
    global player_health
    player_hp.clear()
    player_hp.write(str(player_health) + "/3 HP", font=("Impact", 40, "bold"))
    if player_health == 0:
        time.sleep(1)
        sys.exit()

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

def player_bound():
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
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(90)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        enemy_move()
        time.sleep(.05)
        enemy_attack()
def down():
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(270)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        enemy_move()
        time.sleep(.05)
        enemy_attack()
def left():
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(180)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        enemy_move()
        time.sleep(.05)
        enemy_attack()
def right():
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(0)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        enemy_move()
        time.sleep(.05)
        enemy_attack()

def make_menu():
    if menu_status == 0:
        drawer.clear()
        drawer.pu()
        drawer.goto(-400,400)
        drawer.begin_fill()
        drawer.pendown()
        drawer.goto(400,400)
        drawer.goto(400,-400)
        drawer.goto(-400,-400)
        drawer.end_fill()
        drawer.color("black")
        drawer.pensize(5)
        drawer.goto(-400,400)
        drawer.goto(400,400)
        drawer.goto(400,-400)
        drawer.goto(-400,-400)
        drawer.pensize(1)
        drawer.color("white")
        menu_status = 1
    if menu_status == 1:
        drawer.clear()
        drawer.

#---------Main---------
drawer.goto(1920,vertical)
drawer.pendown()
draw_gridx()
drawer.pu()
drawer.goto(horizontal, 1080)
drawer.pendown()
draw_gridy()
display_health()

wn.onkeypress(up,'w')
wn.onkeypress(down,'s')
wn.onkeypress(left,'a')
wn.onkeypress(right,'d')

wn.onkeypress(set_up,'i')
wn.onkeypress(set_down,'k')
wn.onkeypress(set_left,'j')
wn.onkeypress(set_right,'l')

wn.onkeypress(set_attack, 'z')

wn.onkeypress(make_menu, 'm')

wn.listen()
wn.mainloop()