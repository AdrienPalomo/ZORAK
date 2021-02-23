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
wn.addshape("Main_Character_Attack.gif")

player = trtl.Turtle()
player.pu()
player.shape("Main_Character.gif")

ball = trtl.Turtle()
ball.pu()
ball.shape("Ball.gif")
ball.hideturtle()
ball.speed(4)

#enemy = trtl.Turtle()
#enemy.pu()
#enemy.shape("Enemy.gif")
#enemy.goto(240,0)

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

ball_distance = 160

drawer = trtl.Turtle()
drawer.hideturtle
drawer.color("white")
drawer.pu()
drawer.speed(0)

pointer = trtl.Turtle()
pointer.pu()
pointer.hideturtle()
pointer.goto(-370,335)
pointer.speed(0)
pointer.turtlesize(2)

pointer_possition = 1

enemy_count = 0
enemy_list = []
wn.tracer(True)
#---------Functions---------
def all_enemy(function):
    for i in range(enemy_count):
        function(enemy_list[i])

def all_enemy_damage(direction):
    for i in range(enemy_count):
        player_attack(direction, enemy_list[i])
    all_enemy(enemy_move)
    time.sleep(.05)
    all_enemy(enemy_attack)

def make_enemy():
    global enemy_count, enemy_list
    enemy_list.append(str(enemy_count))
    enemy_list[enemy_count] = trtl.Turtle()
    enemy_list[enemy_count].shape("Enemy.gif")
    enemy_list[enemy_count].pu()
    x = random.randint(-11,11)
    y = random.randint(-6,6)
    enemy_list[enemy_count].goto(x*80, y*80)
    enemy_count = enemy_count + 1

#SENDS BALL FORWARD
def ball_animation(heading):
    global attack_status, ball_distance
    attack_status = hold
    attack_status = 2
    x = player.xcor()
    y = player.ycor()
    ball.goto(x,y)
    ball.setheading(heading)
    ball.showturtle()
    ball.forward(ball_distance + 40)
    ball.hideturtle()
    attack_status = hold

#FLASHES PLAYER/ENEMY FOR A HURT ANIMATION
def hurt_animation(sprite):
    global attack_status
    attack_status = 2
    for i in range(5):
        sprite.hideturtle()
        time.sleep(.01)
        sprite.showturtle()
        time.sleep(.01)
    attack_status = 0

#MAKES ENEMY ATTACK IF THEY ARE WITHIN A CERTAIN DISTANCE
def enemy_attack(enemy):
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

#ALL ENEMY MOVEMENT THIS WAS PAIN
def enemy_move(enemy):
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

#MAKES THE PLAYER ATTACK, CHECKS TO SEE IF IT HITS, THEN MAKES MULTIPLE ANIMATIONS
def player_attack(direction,enemy):
    global attack_status, ball_distance
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
        #UP
        if (direction == 1) and (xf <= 40) and (xf >= -40) and (yf >= 0) and (yf <= ball_distance + 40):
            wn.tracer(False)
            enemy.goto(10**99,10**99)
            wn.tracer(True)
        #DOWN
        elif (direction == 2) and (xf <= 40) and (xf >= -40) and (yf <= 0) and (yf >= (-1 * ball_distance) - 40):
            hurt_animation(enemy)
            wn.tracer(False)
            enemy.goto(10**99,10**99)
            wn.tracer(True)
        #LEFT
        elif direction == 3 and (yf <= 40) and (yf >= -40) and (xf <= 0) and (xf >= (-1 * ball_distance) - 40):
            hurt_animation(enemy)
            wn.tracer(False)
            enemy.goto(10**99,10**99)
            wn.tracer(True)
        #RIGHT
        elif direction == 4 and (yf <= 40) and (yf >= -40) and (xf >= 0) and (xf <= ball_distance + 40):
            hurt_animation(enemy)
            wn.tracer(False)
            enemy.goto(10**99,10**99)
            wn.tracer(True)
    attack_status = 0
    player.shape("Main_Character.gif")

#GETS THE CHARACTER READY TO ATTACK
def set_attack():
    global attack_status, menu_status
    if attack_status == 0 and menu_status == 0:
        attack_status = 1
        player.shape("Main_Character_Attack.gif")
    elif attack_status == 1 and menu_status == 0:
        attack_status = 0
        player.shape("Main_Character.gif")

#SETS THE ENEMY ATTACK DIRECTION TO UP
def set_up():
    global attack_status, menu_status
    if attack_status == 1 and menu_status == 0:
        all_enemy_damage(1)

#SETS THE ENEMY ATTACK DIRECTION TO DOWN
def set_down():
    global attack_status, menu_status
    if attack_status == 1 and menu_status == 0:
        all_enemy_damage(2)

#SETS THE ENEMY ATTACK DIRECTION TO THE LEFT
def set_left():
    global attack_status, menu_status
    if attack_status == 1 and menu_status == 0:
        all_enemy_damage(3)

#SETS THE ENEMY ATTACK DIRECTION TO THE RIGHT
def set_right():
    global attack_status, menu_status
    if attack_status == 1 and menu_status == 0:
        all_enemy_damage(4)

#MAKES DRAWER DISPLAY HERO HEALTH, AND PAUSES FOR 1 SECOND BEFORE ENDING THE GAME IF HEALTH REACHES 0
def display_health():
    global player_health
    player_hp.clear()
    player_hp.write(str(player_health) + "/3 HP", font=("Impact", 40, "bold"))
    if player_health == 0:
        time.sleep(1)
        sys.exit()

#DRAWS VERTICAL LINES FOR GRID (I KNOW THE NAME IS HORRIBLE)
def draw_gridx():
    vertical = 1000
    for i in range(20):
        wn.tracer(False)
        drawer.setheading(0)
        drawer.goto(-1920,vertical)
        vertical = vertical - 80
        drawer.goto(-1920,vertical)
        drawer.goto(1920,vertical)
    wn.tracer(True)
    
#DRAWS HORIZONTAL LINES FOR GRID (I KNOW THE NAME IS HORRIBLE)
def draw_gridy():
    horizontal = 1800
    for i in range(80):
        wn.tracer(False)
        drawer.setheading(0)
        drawer.goto(horizontal,-1080)
        horizontal = horizontal - 80
        drawer.goto(horizontal,-1080)
        drawer.goto(horizontal,1080)
    wn.tracer(True)
    
#IF PLAYER STEPS OUT OF BOUNDS, THIS TELEPORTS THEM TO THE OTHER SIDE
def player_bound():
    x = player.xcor()
    y = player.ycor()
    if x > 880:
        player.goto((x-80)*-1,y)
    elif x < -880:
        player.goto((x+80)*-1,y)
    elif y > 480:
        player.goto(x,(y-80)*-1)
    elif y < -480:
        player.goto(x,(y+80)*-1)
    elif y <= -120 and y >= -200 and x <= 520 and x >= 440:
        player.goto(800,0)
    
#MOVES CHARACTER UP, THEN DOES ENEMY MOVEMENT
def up():
    global attack_status, menu_status
    if attack_status == 0 and menu_status == 0:
        wn.tracer(False)
        player.setheading(90)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy(enemy_attack)
#MOVES CHARACTER DOWN, THEN DOES ENEMY MOVEMENT
def down():
    global attack_status, menu_status
    if attack_status == 0 and menu_status == 0:
        wn.tracer(False)
        player.setheading(270)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy(enemy_attack)
#MOVES CHARACTER LEFT, THEN DOES ENEMY MOVEMENT
def left():
    global attack_status, menu_status
    if attack_status == 0 and menu_status == 0:
        wn.tracer(False)
        player.setheading(180)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy(enemy_attack)
#MOVES CHARACTER RIGHT, THEN DOES ENEMY MOVEMENT
def right():
    global attack_status, menu_status
    if attack_status == 0 and menu_status == 0:
        wn.tracer(False)
        player.setheading(0)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy(enemy_attack)

#MAKES MENU/SHOP
def make_menu():
    global menu_status
    if menu_status == 0:
        wn.tracer(False)
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
        drawer.pu()
        drawer.goto(-350,300)
        drawer.write("RANGE UP: 40 GOLD", font=("Impact", 40, "bold"))
        drawer.goto(-350,0)
        drawer.write("SPREAD SHOT: 100 GOLD", font=("Impact", 40, "bold"))
        drawer.goto(-350,-300)
        drawer.write("EXPERT MODE", font=("Impact", 40, "bold"))
        drawer.color("white")
        pointer.showturtle()
        wn.tracer(True)
        menu_status = 1
    elif menu_status == 1:
        wn.tracer(False)
        drawer.clear()
        drawer.pu()
        drawer.goto(1920,1000)
        drawer.pendown()
        draw_gridx()
        drawer.pu()
        drawer.goto(1800, 1080)
        drawer.pendown()
        draw_gridy()
        display_health()
        pointer.hideturtle()
        wn.tracer(True)
        menu_status = 0
        
def pointer_up():
    global pointer_possition, menu_status
    x = pointer.xcor()
    y = pointer.ycor()
    if pointer_possition > 1 and menu_status == 1:
        pointer.goto(x,y + 300)
        pointer_possition = pointer_possition - 1
def pointer_down():
    global pointer_possition, menu_status
    x = pointer.xcor()
    y = pointer.ycor()
    if pointer_possition < 3 and menu_status == 1:
        pointer.goto(x,y - 300)
        pointer_possition = pointer_possition + 1

#---------Main---------
menu_status = 0
drawer.goto(1920,1000)
drawer.pendown()
draw_gridx()
drawer.pu()
drawer.goto(1800, 1080)
drawer.pendown()
draw_gridy()
display_health()
make_enemy()
make_enemy()


wn.onkey(up,'w')
wn.onkey(down,'s')
wn.onkey(left,'a')
wn.onkey(right,'d')

wn.onkeypress(set_up,'i')
wn.onkeypress(set_down,'k')
wn.onkeypress(set_left,'j')
wn.onkeypress(set_right,'l')

wn.onkeypress(set_attack, 'z')

wn.onkey(make_menu, 'm')

wn.onkey(pointer_up, "Up")
wn.onkey(pointer_down, "Down")

wn.listen()
wn.mainloop()