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
wn.addshape("Coins.gif")
wn.addshape("wizardogy.gif")
wn.addshape("explosion1.gif")
wn.addshape("explosion2.gif")
wn.addshape("explosion3.gif")
wn.addshape("Main_Character_Dead.gif")
wn.addshape("Boss.gif")
wn.addshape("Target.gif")
wn.addshape("Warning.gif")
wn.addshape("Rocket.gif")
wn.addshape("Bullets.gif")
wn.addshape("Remote.gif")
wn.addshape("Broken_Remote.gif")

player = trtl.Turtle()
player.pu()
player.shape("Main_Character.gif")
player.speed(6)

ball = trtl.Turtle()
ball.pu()
ball.shape("Ball.gif")
ball.hideturtle()
ball.speed(4)

player_health = 3
player_hp = trtl.Turtle()
player_hp.color("red")
player_hp.hideturtle()
player_hp.pu()
player_hp.goto(-950,440)

wait = 1

attack_status = 0

direction = 0

hold = "placeholder"

menu_status = 0

ball_distance = 160

drawer = trtl.Turtle()
drawer.hideturtle()
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

coin_count = 0
coin_list = []
coins = 0
coin_boy = trtl.Turtle()
coin_boy.color("yellow")
coin_boy.hideturtle()
coin_boy.pu()
coin_boy.goto(720,440)

ook = 0

timer = 10
timer_max = 10

ogy = trtl.Turtle()
ogy.pu()
ogy.goto(-300,0)
ogy.shape("wizardogy.gif")
ogy.hideturtle()
explosion = trtl.Turtle()
explosion.pu()
explosion.shape("explosion1.gif")
explosion.hideturtle()

price = 20

spread = False
animation = False

combo = 0
combo_boy = trtl.Turtle()
combo_boy.color("lime")
combo_boy.hideturtle()
combo_boy.pu()
combo_boy.goto(-950,380)


boss1_fight = False
boss1 = trtl.Turtle()
boss1.pu()
boss1.hideturtle()
boss1.speed(3)
boss1.shape("Boss.gif")
boss1.goto(480,-160)

boss1_attack_up = trtl.Turtle()
boss1_attack_down = trtl.Turtle()
boss1_attack_left = trtl.Turtle()
boss1_attack_right = trtl.Turtle()
boss1_attack_up.pu()
boss1_attack_down.pu()
boss1_attack_left.pu()
boss1_attack_right.pu()
boss1_attack_up.shape("Target.gif")
boss1_attack_down.shape("Target.gif")
boss1_attack_left.shape("Target.gif")
boss1_attack_right.shape("Target.gif")
boss1_attack_up.hideturtle()
boss1_attack_down.hideturtle()
boss1_attack_left.hideturtle()
boss1_attack_right.hideturtle()
boss1_attack_up.goto(480,-160)
boss1_attack_down.goto(480,-160)
boss1_attack_left.goto(480,-160)
boss1_attack_right.goto(480,-160)
boss1_attack_up.speed(8)
boss1_attack_down.speed(8)
boss1_attack_left.speed(8)
boss1_attack_right.speed(8)

boss1_attacking_target = False
boss1_attacking_bullet = False

warning_1 = trtl.Turtle()
warning_2 = trtl.Turtle()
warning_1.pu()
warning_2.pu()
warning_1.shape("Warning.gif")
warning_2.shape("Warning.gif")
warning_1.hideturtle()
warning_2.hideturtle()
warning_1.speed(8)
warning_2.speed(8)

rocketman = trtl.Turtle()
rocketman.pu()
rocketman.hideturtle()
rocketman.speed(6)
rocketman.shape("Rocket.gif")

remote_1 = trtl.Turtle()
remote_2 = trtl.Turtle()
remote_3 = trtl.Turtle()
remote_1.pu()
remote_2.pu()
remote_3.pu()
remote_1.hideturtle()
remote_2.hideturtle()
remote_3.hideturtle()
remote_1.shape("Remote.gif")
remote_2.shape("Remote.gif")
remote_3.shape("Remote.gif")

first_remote = True
second_remote = True
third_remote = True

boss_health = 3
wn.tracer(True)
#---------Functions---------
def remote_check():
    global first_remote, second_remote, third_remote, boss_health, boss1_fight, boss1_attacking_target, boss1_attacking_bullet
    if boss1_fight == True:
        x = player.xcor()
        y = player.ycor()
        if first_remote == True:
            xr = remote_1.xcor()
            yr = remote_1.ycor()
            xf = x - xr
            yf = y - yr
            if (xf >= -40) and (xf <= 40) and (yf >= -40) and (yf <= 40):
                rocket_animation(boss1)
                time.sleep(.05)
                remote_1.shape("Broken_Remote.gif")
                boss_health = boss_health - 1
                player.goto(-11 * 80, 0)
                boss1_attacking_target = False
                boss1_attacking_bullet = False
                warning_1.hideturtle()
                warning_2.hideturtle()
                boss1_attack_up.hideturtle()
                boss1_attack_down.hideturtle()
                boss1_attack_left.hideturtle()
                boss1_attack_right.hideturtle()
                first_remote = False
        if second_remote == True:
            xr = remote_2.xcor()
            yr = remote_2.ycor()
            xf = x - xr
            yf = y - yr
            if (xf >= -40) and (xf <= 40) and (yf >= -40) and (yf <= 40):
                rocket_animation(boss1)
                time.sleep(.05)
                remote_2.shape("Broken_Remote.gif")
                boss_health = boss_health - 1
                player.goto(-11 * 80, 0)
                boss1_attacking_target = False
                boss1_attacking_bullet = False
                warning_1.hideturtle()
                warning_2.hideturtle()
                boss1_attack_up.hideturtle()
                boss1_attack_down.hideturtle()
                boss1_attack_left.hideturtle()
                boss1_attack_right.hideturtle()
                second_remote = False
        if third_remote == True:
            xr = remote_3.xcor()
            yr = remote_3.ycor()
            xf = x - xr
            yf = y - yr
            if (xf >= -40) and (xf <= 40) and (yf >= -40) and (yf <= 40):
                rocket_animation(boss1)
                time.sleep(.05)
                remote_3.shape("Broken_Remote.gif")
                boss_health = boss_health - 1
                player.goto(-11 * 80, 0)
                boss1_attacking_target = False
                boss1_attacking_bullet = False
                warning_1.hideturtle()
                warning_2.hideturtle()
                boss1_attack_up.hideturtle()
                boss1_attack_down.hideturtle()
                boss1_attack_left.hideturtle()
                boss1_attack_right.hideturtle()
                third_remote = False
        if boss_health == 0:
            xe = boss1.xcor()
            ye = boss1.ycor()
            explosion_animation(xe - 160,ye + 80)
            explosion_animation(xe + 80,ye + 80)
            explosion_animation(xe,ye - 160)
            warning_1.hideturtle()
            warning_2.hideturtle()
            boss1_attack_up.hideturtle()
            boss1_attack_down.hideturtle()
            boss1_attack_left.hideturtle()
            boss1_attack_right.hideturtle()
            boss1.hideturtle()
            boss1_attacking_target = False
            boss1_attacking_bullet = False
            boss1_fight = False
            remote_1.hideturtle()
            remote_2.hideturtle()
            remote_3.hideturtle()

def rocket_animation(turtle):
    xt = turtle.xcor()
    yt = turtle.ycor()
    wn.tracer(False)
    rocketman.goto(xt, 540)
    rocketman.showturtle()
    wn.tracer(True)
    rocketman.goto(xt,yt)
    rocketman.shape("explosion1.gif")
    time.sleep(.01)
    rocketman.hideturtle()
    rocketman.shape("Rocket.gif")

def bullet_animation(turtle):
     turtle.shape("Bullets.gif")
     yt = turtle.ycor()
     turtle.goto(-960,yt)
     turtle.hideturtle()
     turtle.shape("Warning.gif")

def check_target(turtle):
    global player_health
    xt = turtle.xcor()
    yt = turtle.ycor()
    x = player.xcor()
    y = player.ycor()
    xf = xt - x
    yf = yt - y
    if (xf >= -40) and (xf <= 40) and (yf >= -40) and (yf <= 40):
        player_health = player_health - 1

def check_bullet(turtle, hold):
    global player_health
    xt = turtle.xcor()
    yt = turtle.ycor()
    x = player.xcor()
    y = player.ycor()
    xf = xt - x
    yf = yt - y
    if(yf >= -40) and (yf <= 40) and (hold - player_health != 1):
        player_health = player_health - 1

def start_boss():
    global boss1_fight, timer, timer_max
    if boss1_fight == False:
        boss1.showturtle()
        boss1.goto(560,0)
        boss1_fight = True
        timer = 8
        timer_max = 8
        wn.tracer(False)
        for i in range(enemy_count):
            enemy_list[i].goto(10**99,10**99)
        a = random.randint(4,6)
        remote_1.goto(320,a*80)
        a = random.randint(-1,1)
        remote_2.goto(320,a*80)
        a = random.randint(-6,-4)
        remote_3.goto(320,a*80)
        remote_1.showturtle()
        remote_2.showturtle()
        remote_3.showturtle()
        player.goto(-11 * 80, 0)
        wn.tracer(True)

def boss1_attack():
    global boss1_attacking_target, menu_status, player_health, boss1_attacking_bullet, combo
    if boss1_fight == True and player_health != 0 and combo == 0:
        if boss1_attacking_target == False:
            a = random.randint(0,5)
            if a == 1:
                x = player.xcor()
                y = player.ycor()
                hold = menu_status
                menu_status = 10
                boss1_attack_up.showturtle()
                boss1_attack_down.showturtle()
                boss1_attack_left.showturtle()
                boss1_attack_right.showturtle()
                boss1_attack_up.goto(x,y + 80)
                boss1_attack_down.goto(x,y - 80)
                boss1_attack_left.goto(x - 80,y)
                boss1_attack_right.goto(x + 80,y)
                menu_status = hold
                boss1_attacking_target = True
        elif boss1_attacking_target == True:
            wn.tracer(False)
            hold = player_health
            check_target(boss1_attack_up)
            check_target(boss1_attack_down)
            check_target(boss1_attack_left)
            check_target(boss1_attack_right)
            boss1_attack_up.hideturtle()
            boss1_attack_down.hideturtle()
            boss1_attack_left.hideturtle()
            boss1_attack_right.hideturtle()
            wn.tracer(True)
            rocket_animation(boss1_attack_up)
            rocket_animation(boss1_attack_left)
            rocket_animation(boss1_attack_down)
            rocket_animation(boss1_attack_right)
            wn.tracer(False)
            if hold - player_health == 1:
                wn.tracer(True)
                hurt_animation(player)
                wn.tracer(False)
            boss1_attack_up.goto(480,-160)
            boss1_attack_down.goto(480,-160)
            boss1_attack_left.goto(480,-160)
            boss1_attack_right.goto(480,-160)
            boss1_attacking_target = False
            wn.tracer(True)
            display_health()
        if boss1_attacking_bullet == False:
            b = random.randint(0,4)
            if b == 1:
                wn.tracer(False)
                yt = random.randint(-6,6)
                warning_1.goto(400,yt * 80)
                yt = random.randint(-6,6)
                warning_2.goto(400,yt * 80)
                warning_1.showturtle()
                warning_2.showturtle()
                wn.tracer(True)
                boss1_attacking_bullet = True
        elif boss1_attacking_bullet == True:
            hold = player_health
            check_bullet(warning_1, hold)
            check_bullet(warning_2, hold)
            bullet_animation(warning_1)
            bullet_animation(warning_2)
            if hold - player_health == 1:
                hurt_animation(player)
            warning_1.hideturtle()
            warning_2.hideturtle()
            wn.tracer(False)
            warning_1.goto(10**99,10**99)
            warning_2.goto(10**99,10**99)
            wn.tracer(True)
            display_health()
            boss1_attacking_bullet = False
            
#MAKES AN EXPLOSION AT THE SPECIFIED COORDINATE
def explosion_animation(xe, ye):
    wn.tracer(False)
    explosion.goto(xe, ye)
    wn.tracer(True)
    explosion.showturtle()
    time.sleep(.1)
    explosion.shape("explosion2.gif")
    time.sleep(.1)
    explosion.shape("explosion3.gif")
    explosion.hideturtle()
    explosion.shape("explosion1.gif")

#PICKS UP ALL COINS ON BOARD
def pickup_coins():
    x = player.xcor()
    y = player.ycor()
    for i in range(coin_count):
        ye = coin_list[i].ycor()
        xe = coin_list[i].xcor()
        if ye < 10000:
            player.goto(xe,ye)
            check_coin()
    player.goto(x,y)
            
#MAKES ALL ENEMIES DO A BASIC FUNCTION
def all_enemy(function):
    for i in range(enemy_count):
        ye = enemy_list[i].ycor()
        if ye < 10000:
            function(enemy_list[i])

#MAKES ALL ENEMIES ATTACK
def all_enemy_attack(function):
    global wait, combo
    for i in range(enemy_count):
        ye = enemy_list[i].ycor()
        if ye < 10000:
            function(enemy_list[i])
    if wait > 0:
        wait = wait - 1
        if wait == 0:
            if combo >= 10:
                pickup_coins()
            combo = 0
            display_combo()

#CHECKS TO SEE IF ENEMIES TAKE DAMAGE
def all_enemy_damage(direction):
    global attack_status, enemy_list, enemy_count, timer, wait
    if direction == 1:
        ball_animation(90)
    elif direction == 2:
        ball_animation(270)
    elif direction == 3:
        ball_animation(180)
    elif direction == 4:
        ball_animation(0)
    attack_status = 1
    for i in range(enemy_count):
        ye = enemy_list[i].ycor()
        if ye < 10000:
            player_attack(direction, i)
    a = random.randint(0,50)
    if a == 1:
        kill_everything()
    wn.tracer(False)
    all_enemy(enemy_move)
    time.sleep(.05)
    all_enemy(enemy_attack)
    boss1_attack()
    timer = timer - 1
    if timer <= 0:
        timer = timer_max
        make_enemy()
    if wait > 0:
        wait = wait - 1
    wn.tracer(True)
    attack_status = 0
    player.shape("Main_Character.gif")

#OGY MAKES A GUEST APPEARANCE AND KILLS EVERYTHING ON THE SCREEN
def kill_everything():
    global ook, attack_status, combo, wait
    if ook != 1:
        hold = attack_status
        attack_status = 1
        ook = 1
        a = 0
        ogy.showturtle()
        time.sleep(.5)
        for i in range(enemy_count):
            xe = enemy_list[i].xcor()
            ye = enemy_list[i].ycor()
            if ye < 10000:
                explosion_animation(xe, ye)
                a = a + 1
            make_coin(i, xe, ye)
            wn.tracer(False)
            enemy_list[i].goto(10**99,10**99)
        ogy.hideturtle()
        combo = combo + a
        wait = 1
        display_combo()
        wn.tracer(True)
        ook = 0
        attack_status = hold

#CHECKS TO SEE IF THE PLAYER IS STEPPING ON A COIN, THEN PICKS IT UP
def check_coin():
    global coins
    for i in range(coin_count):
        xc = coin_list[i].xcor()
        yc = coin_list[i].ycor()
        x = player.xcor()
        y = player.ycor()
        if x - xc >= -40 and x - xc <= 40 and y - yc >= -40 and y - yc <= 40:
            wn.tracer(False)
            a = random.randint(1,30)
            coins = coins + a
            display_coins()
            coin_list[i].goto(10**99,10**99)
            wn.tracer(True)

#MAKES AN ENEMY AT A RANDOM SPOT, ALSO CHECKS TO MAKE SURE THEY DON'T SPAWN WITHIN 2 TILES OF THE PLAYER
def make_enemy():
    global enemy_count, enemy_list
    wn.tracer(False)
    enemy_list.append(str(enemy_count))
    enemy_list[enemy_count] = trtl.Turtle()
    enemy_list[enemy_count].shape("Enemy.gif")
    enemy_list[enemy_count].pu()
    x = player.xcor()
    y = player.ycor()
    check = False
    if boss1_fight == False:
        xe = (random.randint(-11,11)) * 80
        ye = (random.randint(-6,6)) * 80
        while check == False:
            if x - xe >= -200 and x - xe <= 200 and y - ye >= -200 and y - ye <= 200:
                xe = (random.randint(-11,11)) * 80
                ye = (random.randint(-6,6)) * 80
            else:
                check = True
                
    elif boss1_fight == True:
        xe = (random.randint(6,11)) * 80
        ye = (random.randint(-6,6)) * 80
        while check == False:
            if x - xe >= -200 and x - xe <= 200 and y - ye >= -200 and y - ye <= 200:
                xe = (random.randint(6,11)) * 80
                ye = (random.randint(-6,6)) * 80
            else:
                check = True
    enemy_list[enemy_count].goto(xe, ye)
    enemy_count = enemy_count + 1
    wn.tracer(True)

#MAKES COIN AT THE SPECIFIED COORDINATE
def make_coin(turtle, xe, ye):
    global coin_count, coin_list
    wn.tracer(False)
    coin_list.append(str(coin_count))
    coin_list[coin_count] = trtl.Turtle()
    coin_list[coin_count].shape("Coins.gif")
    coin_list[coin_count].pu()
    x = enemy_list[turtle].xcor()
    y = enemy_list[turtle].ycor()
    coin_list[coin_count].goto(xe, ye)
    coin_count = coin_count + 1
    wn.tracer(True)

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
    if spread == True:
        #UP
        if heading == 90:
            wn.tracer(False)
            ball.goto(x-80,y)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
            wn.tracer(False)
            ball.goto(x+80,y)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
        #LEFT
        elif heading == 180:
            wn.tracer(False)
            ball.goto(x,y-80)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
            wn.tracer(False)
            ball.goto(x,y+80)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
        #DOWN
        elif heading == 270:
            wn.tracer(False)
            ball.goto(x-80,y)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
            wn.tracer(False)
            ball.goto(x+80,y)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
        #RIGHT
        elif heading == 0:
            wn.tracer(False)
            ball.goto(x,y-80)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()
            wn.tracer(False)
            ball.goto(x,y+80)
            wn.tracer(True)
            ball.showturtle()
            ball.forward(ball_distance + 40)
            ball.hideturtle()

    attack_status = hold

#FLASHES PLAYER/ENEMY FOR A HURT ANIMATION
def hurt_animation(sprite):
    global attack_status
    a = attack_status
    attack_status = 2
    for i in range(5):
        sprite.hideturtle()
        time.sleep(.01)
        sprite.showturtle()
        time.sleep(.01)
    attack_status = a

#MAKES ENEMY ATTACK IF THEY ARE WITHIN A CERTAIN DISTANCE
def enemy_attack(enemy):
    global player_health, wait
    xe = enemy.xcor()
    ye = enemy.ycor()
    x = player.xcor()
    y = player.ycor()
    if abs(xe - x) <= 120 and abs(ye - y) <= 120 and wait == 0:
        wait = 4
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
    global attack_status, ball_distance, enemy_list, combo, wait
    if attack_status == 1:
        xe = enemy_list[enemy].xcor()
        ye = enemy_list[enemy].ycor()
        x = player.xcor()
        y = player.ycor()
        xf = xe - x
        yf = ye - y
        if spread == False:
            #UP
            if (direction == 1) and (xf <= 40) and (xf >= -40) and (yf >= 0) and (yf <= ball_distance + 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
            #DOWN
            elif (direction == 2) and (xf <= 40) and (xf >= -40) and (yf <= 0) and (yf >= (-1 * ball_distance) - 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
            #LEFT
            elif direction == 3 and (yf <= 40) and (yf >= -40) and (xf <= 0) and (xf >= (-1 * ball_distance) - 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
            #RIGHT
            elif direction == 4 and (yf <= 40) and (yf >= -40) and (xf >= 0) and (xf <= ball_distance + 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
        elif spread == True:
            #UP
            if (direction == 1) and (xf <= 120) and (xf >= -120) and (yf >= 0) and (yf <= ball_distance + 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
            #DOWN
            elif (direction == 2) and (xf <= 120) and (xf >= -120) and (yf <= 0) and (yf >= (-1 * ball_distance) - 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
            #LEFT
            elif direction == 3 and (yf <= 120) and (yf >= -120) and (xf <= 0) and (xf >= (-1 * ball_distance) - 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)
            #RIGHT
            elif direction == 4 and (yf <= 120) and (yf >= -120) and (xf >= 0) and (xf <= ball_distance + 40):
                hurt_animation(enemy_list[enemy])
                wn.tracer(False)
                enemy_list[enemy].goto(10**99,10**99)
                make_coin(enemy, xe, ye)
                combo = combo + 1
                display_combo()
                wait = 4
                wn.tracer(True)

#GETS THE CHARACTER READY TO ATTACK
def set_attack():
    global attack_status, menu_status, player_health
    if player_health != 0:
        if attack_status == 0 and menu_status == 0:
            attack_status = 1
            player.shape("Main_Character_Attack.gif")
        elif attack_status == 1 and menu_status == 0:
            attack_status = 0
            player.shape("Main_Character.gif")

#SETS THE ENEMY ATTACK DIRECTION TO UP
def set_up():
    global attack_status, menu_status, player_health
    if attack_status == 1 and menu_status == 0 and player_health != 0:
        all_enemy_damage(1)

#SETS THE ENEMY ATTACK DIRECTION TO DOWN
def set_down():
    global attack_status, menu_status, player_health
    if attack_status == 1 and menu_status == 0 and player_health != 0:
        all_enemy_damage(2)

#SETS THE ENEMY ATTACK DIRECTION TO THE LEFT
def set_left():
    global attack_status, menu_status, player_health
    if attack_status == 1 and menu_status == 0 and player_health != 0:
        all_enemy_damage(3)

#SETS THE ENEMY ATTACK DIRECTION TO THE RIGHT
def set_right():
    global attack_status, menu_status, player_health
    if attack_status == 1 and menu_status == 0 and player_health != 0:
        all_enemy_damage(4)

#MAKES DRAWER DISPLAY HERO HEALTH, AND PAUSES FOR 1 SECOND BEFORE ENDING THE GAME IF HEALTH REACHES 0
def display_health():
    global player_health
    player_hp.clear()
    player_hp.write(str(player_health) + "/3 HP", font=("Impact", 40, "bold"))
    if player_health == 0:
        wn.tracer(False)
        drawer.pu()
        drawer.clear()
        for i in range(enemy_count):
            enemy_list[i].goto(10**99,10**99)
        for i in range(coin_count):
            coin_list[i].goto(10**99,10**99)
        warning_1.hideturtle()
        warning_2.hideturtle()
        boss1_attack_up.hideturtle()
        boss1_attack_down.hideturtle()
        boss1_attack_left.hideturtle()
        boss1_attack_right.hideturtle()
        boss1.hideturtle()
        player.shape("Main_Character_Dead.gif")
        drawer.goto(-170,-10)
        drawer.write("Press r to restart", font=("Impact", 40, "bold"))
        wn.tracer(True)
#MAKES DRAWER DISPLAY HERO COINS
def display_coins():
    global player_health
    coin_boy.clear()
    coin_boy.write(str(coins) + " Coins", font=("Impact", 40, "bold"))

def display_combo():
    global combo
    combo_boy.clear()
    combo_boy.write("Combo: " + str(combo), font=("Impact", 40, "bold"))
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
    global boss1_fight
    x = player.xcor()
    y = player.ycor()
    if x > 920:
        check_coin()
        player.goto((x-80)*-1,y)
    elif x < -920:
        check_coin()
        if boss1_fight == False:
            player.goto((x+80)*-1,y)
        elif boss1_fight == True:
            player.goto(x + 80, y)
    elif y > 520:
        check_coin()
        player.goto(x,(y-80)*-1)
    elif y < -520:
        check_coin()
        player.goto(x,(y+80)*-1)
    elif y <= -120 and y >= -200 and x <= 520 and x >= 440:
        check_coin()
        wn.tracer(False)
        player.goto(800,0)
        wn.tracer(True)
    check_coin()
    
#MOVES CHARACTER UP, THEN DOES ENEMY MOVEMENT
def up():
    global attack_status, menu_status, timer, player_health
    if attack_status == 0 and menu_status == 0:
        attack_status = 4
        wn.tracer(False)
        player.setheading(90)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        remote_check()
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy_attack(enemy_attack)
        if player_health != 0:
            if timer > 0:
                timer = timer - 1
            elif timer <= 0:
                timer = timer_max
                make_enemy()
        boss1_attack()
        attack_status = 0
#MOVES CHARACTER DOWN, THEN DOES ENEMY MOVEMENT
def down():
    global attack_status, menu_status, timer, player_health
    if attack_status == 0 and menu_status == 0:
        attack_status = 4
        wn.tracer(False)
        player.setheading(270)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        remote_check()
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy_attack(enemy_attack)
        if player_health != 0:
            if timer > 0:
                timer = timer - 1
            elif timer <= 0:
                timer = timer_max
                make_enemy()
        boss1_attack()
        attack_status = 0
#MOVES CHARACTER LEFT, THEN DOES ENEMY MOVEMENT
def left():
    global attack_status, menu_status, timer, player_health
    if attack_status == 0 and menu_status == 0:
        attack_status = 4
        wn.tracer(False)
        player.setheading(180)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        remote_check()
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy_attack(enemy_attack)
        if player_health != 0:
            if timer > 0:
                timer = timer - 1
            elif timer <= 0:
                timer = timer_max
                make_enemy()
        boss1_attack()
        attack_status = 0
#MOVES CHARACTER RIGHT, THEN DOES ENEMY MOVEMENT
def right():
    global attack_status, menu_status, timer, player_health
    if attack_status == 0 and menu_status == 0:
        attack_status = 4
        wn.tracer(False)
        player.setheading(0)
        player.forward(80)
        player_bound()
        wn.tracer(True)
        remote_check()
        all_enemy(enemy_move)
        time.sleep(.05)
        all_enemy_attack(enemy_attack)
        if player_health != 0:
            if timer > 0:
                timer = timer - 1
            elif timer <= 0:
                timer = timer_max
                make_enemy()
        boss1_attack()
        attack_status = 0
#MAKES MENU/SHOP
def make_menu():
    global menu_status, animation
    if animation == False:
        if menu_status == 0:
            wn.tracer(False)
            menu_status = 1
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
            drawer.write("RANGE UP: " + str(price) +  " GOLD", font=("Impact", 40, "bold"))
            drawer.goto(-350,0)
            drawer.write("SPREAD SHOT: 100 GOLD", font=("Impact", 40, "bold"))
            drawer.goto(-350,-300)
            drawer.write("START BOSS FIGHT", font=("Impact", 40, "bold"))
            display_coins()
            if spread == True:
                drawer.goto(180,20)
                drawer.color("green")
                drawer.begin_fill()
                drawer.circle(10)
                drawer.end_fill()
                drawer.pensize(4)
                drawer.color("black")
                drawer.circle(10)
                drawer.pensize(1)
            if boss1_fight == True:
                drawer.goto(60,-280)
                drawer.color("green")
                drawer.begin_fill()
                drawer.circle(10)
                drawer.end_fill()
                drawer.pensize(4)
                drawer.color("black")
                drawer.circle(10)
                drawer.pensize(1)
            drawer.color("white")
            pointer.showturtle()
            wn.tracer(True)
        elif menu_status == 1:
            wn.tracer(False)
            menu_status = 0
            drawer.clear()
            drawer.pu()
            drawer.goto(1920,1000)
            drawer.pendown()
            draw_gridx()
            drawer.pu()
            drawer.goto(1800, 1080)
            drawer.pendown()
            draw_gridy()
            display_coins()
            display_health()
            pointer.hideturtle()
            wn.tracer(True)

#MAKES THE POINTER IN THE SHOP GO UP AND DOWN
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

#USES POINTER TO BUY/SELECT THINGS IN SHOP
def select_menu():
    global menu_status, pointer_possition, ball_distance, coins, price, spread, timer_max, timer, animation, player_health, boss1_fight
    if animation == False and player_health > 0:
        if menu_status == 1 and pointer_possition == 1 and coins >= price and price < 130:
            animation = True
            wn.tracer(False)
            ball_distance = ball_distance + 160
            coins = coins - price
            price = price + 10
            if price >= 50 and price < 80:
                ball.speed(6)
            elif price >= 80:
                ball.speed(7)
            wn.tracer(True)
            display_coins()
            animation = False
            menu_status = 0
            make_menu()
        elif menu_status == 1 and pointer_possition == 1 and (coins < price or price >= 130):
            animation = True
            drawer.pu()
            drawer.goto(300,300)
            drawer.pendown()
            drawer.pensize(15)
            drawer.color("red")
            drawer.goto(-300,-300)
            drawer.pu()
            drawer.goto(-300,300)
            drawer.pendown()
            drawer.goto(300,-300)
            drawer.pensize(1)
            drawer.color("white")
            time.sleep(.5)
            wn.tracer(False)
            drawer.clear()
            wn.tracer(True)
            animation = False
            menu_status = 0
            make_menu()
        elif menu_status == 1 and pointer_possition == 2 and coins >= 100 and spread == False:
            animation = True
            wn.tracer(False)
            coins = coins - 100
            spread = True
            timer_max = 5
            if timer > timer_max:
                timer = timer - timer_max
            wn.tracer(True)
            animation = False
            menu_status = 0
            make_menu()
        elif menu_status == 1 and pointer_possition == 2 and coins < 100 or spread == True:
            animation = True
            drawer.pu()
            drawer.goto(300,300)
            drawer.pendown()
            drawer.pensize(15)
            drawer.color("red")
            drawer.goto(-300,-300)
            drawer.pu()
            drawer.goto(-300,300)
            drawer.pendown()
            drawer.goto(300,-300)
            drawer.pensize(1)
            drawer.color("white")
            time.sleep(.5)
            wn.tracer(False)
            drawer.clear()
            wn.tracer(True)
            animation = False
            menu_status = 0
            make_menu()
        elif menu_status == 1 and pointer_possition == 3 and boss1_fight == False:
            animation = True
            timer_max = 5
            if timer > timer_max:
                timer = timer - timer_max
            animation = False
            menu_status = 0
            start_boss()
            make_menu()
        elif menu_status == 1 and pointer_possition == 3 and boss1_fight == True:
            animation = True
            drawer.pu()
            drawer.goto(300,300)
            drawer.pendown()
            drawer.pensize(15)
            drawer.color("red")
            drawer.goto(-300,-300)
            drawer.pu()
            drawer.goto(-300,300)
            drawer.pendown()
            drawer.goto(300,-300)
            drawer.pensize(1)
            drawer.color("white")
            time.sleep(.5)
            wn.tracer(False)
            drawer.clear()
            wn.tracer(True)
            animation = False
            menu_status = 0
            make_menu()

#RESTARTS THE GAME ONCE GAME ENDS (AFTER PRESSING R)
def restart():
    global coins, player_health, menu_status, spread, timer, timer_max, price, ball_distance, wait, boss1_attacking_target, boss1_attacking_bullet, boss1_fight
    if player_health == 0 and menu_status == 0:
        wn.tracer(False)
        for i in range(enemy_count):
            enemy_list[i].goto(10**99,10**99)
        for i in range(coin_count):
            coin_list[i].goto(10**99,10**99)
        player.goto(0,0)
        make_enemy()
        make_enemy()
        coins = 0
        wait = 0
        display_coins()
        player_health = 3
        price = 20
        ball_distance = 160
        ball.speed(4)
        menu_status = 1
        make_menu()
        boss1_attacking_target = False
        boss1_attacking_bullet = False
        boss1_fight = False
        spread = False
        timer = 10
        timer_max = 10
        player.shape("Main_Character.gif")
        wn.tracer(True)
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
display_coins()
display_combo()
make_enemy()
make_enemy()

wn.onkey(up,'w')
wn.onkey(down,'s')
wn.onkey(left,'a')
wn.onkey(right,'d')

wn.onkey(set_up,'i')
wn.onkey(set_down,'k')
wn.onkey(set_left,'j')
wn.onkey(set_right,'l')

wn.onkeypress(set_attack, 'z')

wn.onkey(make_menu, 'm')

wn.onkey(pointer_up, "Up")
wn.onkey(pointer_down, "Down")
wn.onkey(kill_everything, "g")
wn.onkey(pickup_coins, 'p')
wn.onkey(boss1_attack,"o")

wn.onkey(select_menu, "b")
wn.onkey(restart, 'r')

wn.listen()
wn.mainloop()