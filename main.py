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

player = trtl.Turtle()
player.pu()
player.shape("Main_Character.gif")

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

vertical = 1000
horizontal = 1800
drawer = trtl.Turtle()
drawer.color("white")
drawer.pu()
drawer.speed(0)
drawer.goto(1920,vertical)
drawer.pendown()

wn.tracer(True)
#---------Functions---------
def player_attack():
    global attack_status, direction
    xe = enemy.xcor()
    ye = enemy.ycor()
    x = player.xcor()
    y = player.ycor()
    if attack_status == 1:
        if direction == 1:
            if xe - x == 0 and ye - y <= 160 and ye - y >= 0:
                enemy.hideturtle()
        elif direction == 2:
            if xe - x == 0 and (ye - y == -160 or ye - y == -80 or ye - y == 0):
                enemy.hideturtle()
        elif direction == 3:
            if ye - y == 0 and (xe - x == -160 or xe - x == -80 or xe - x == 0):
                enemy.hideturtle()
        elif direction == 4:
            if ye - y == 0 and (xe - x == 160 or xe - x == 80 or xe - x == 0):
                enemy.hideturtle()
    attack_status = 0

def set_attack():
    global attack_status
    if attack_status == 0:
        attack_status = 1
        player.shape("Enemy.gif")
    elif attack_status == 1:
        attack_status = 0
        player.shape("Main_Character.gif")

def set_up():
    global direction, attack_status
    if attack_status == 1:
        direction = 1
        player_attack()

def set_down():
    global direction, attack_status
    if attack_status == 1:
        direction = 2
        player_attack()

def set_left():
    global direction, attack_status
    if attack_status == 1:
        direction = 3
        player_attack()

def set_right():
    global direction, attack_status, direction
    if attack_status == 1:
        direction = 4
        player_attack()
     
def display_health():
    global player_health
    player_hp.clear()
    player_hp.write(str(player_health) + "/3 HP", font=("Impact", 40, "bold"))
    if player_health == 0:
        time.sleep(1)
        sys.exit()

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
        display_health()

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

def enemy_move():
    global wait
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
        enemy_move()
        time.sleep(.05)
        enemy_attack()
        wn.tracer(True)
def down():
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(270)
        player.forward(80)
        player_bound()
        enemy_move()
        time.sleep(.05)
        enemy_attack()
        wn.tracer(True)
def left():
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(180)
        player.forward(80)
        player_bound()
        enemy_move()
        time.sleep(.05)
        enemy_attack()
        wn.tracer(True)
def right():
    global attack_status
    if attack_status == 0:
        wn.tracer(False)
        player.setheading(0)
        player.forward(80)
        player_bound()
        enemy_move()
        time.sleep(.05)
        enemy_attack()
        wn.tracer(True)

#---------Main---------
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
wn.onkeypress(set_down,'l')
wn.onkeypress(set_left,'k')
wn.onkeypress(set_right,'j')
wn.onkeypress(set_attack, 'z')

wn.listen()
wn.mainloop()
