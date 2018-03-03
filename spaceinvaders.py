# Space Invaders
# Python 3.6 Linux
# Sound only aviable on Linux but can be modified for other os
# Sounds tooken from freesound.org
# Pictures token by web and modified on gimp
# All credits go to Anaconda | GitHub KnownAsDon

# Modules
import turtle
import os
import math
import random


# Screen setup
mainScreen = turtle.Screen()
mainScreen.bgcolor("#3B1849")
mainScreen.title("Space Invaders")
mainScreen.bgpic("images/background.gif")

#Register shapes
turtle.register_shape("images/invader.gif")
turtle.register_shape("images/player.gif")
turtle.register_shape("images/lazer.gif")

# Draw Border
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("#ffffff")
borderPen.penup()
borderPen.setposition(-300, -300)
borderPen.pendown()
borderPen.pensize(3)
for side in range(4):
    borderPen.forward(600)
    borderPen.left(90)
borderPen.hideturtle()

#Set score to 0
score = 0

#Draw the score
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.color("#ffffff")
scorePen.penup()
scorePen.setposition(-290, 270)
scorestring = "Score: %s" %score
scorePen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
scorePen.hideturtle()

# Player Turtle
player = turtle.Turtle()
player.color("#2980b9")
player.shape("images/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Number of enemies
numberOfEnemies = 5
# Empty enemy list
enemies = []
# Add enemies to list
for i in range(numberOfEnemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("images/invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(200, 250)
	enemy.setposition(x, y)
enemyspeed = 2

# Player's Defense
bullet = turtle.Turtle()
bullet.color("#f1c40f")
bullet.shape("images/lazer.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20
# Bullet State
bulletstate = "ready"
# Ready
# Fire

# Player's Movment
playerspeed = 15
def moveLeft():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def moveRight():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fireBullet():
    #Define global bulet state
    global bulletstate
    if bulletstate == "ready":
        os.system("aplay sounds/laser.wav&")
        bulletstate = "fire"
        #Move bullet above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1 ,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Keyboard Bindings
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(fireBullet, "space")


# Main Game Loop
while True:

    for enemy in enemies:
        #Enemy Movment
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #Enemy move back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Check for collision betwen the bullet and the enemy
        if isCollision(bullet, enemy):
            os.system("aplay sounds/explosion.wav&")
            #Reset bullet
            bullet.hideturtle()
            bulletstate = "ready" 
            bullet.setposition(0, -400)
            #Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            score += 10
            scorestring = "Score: %s" %score
            scorePen.clear()
            scorePen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            print("Your score was", score)
            break

	
    #Move bullet in general 
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
   
    #Check if bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    
delay = input("Press enter to finish...")
