# Set up screen
import turtle
import os

# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.setposition(-300, -300)
pen.pendown()
pen.pensize(5)
for side in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()

# Player setup
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Enemy
enemy = turtle.Turtle()
enemy.color("green")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

# Bullet
bullet = turtle.Turtle()
bullet.color("Green")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Bullet state
# Ready || Fire
bulletstate = "ready"


# Move player

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()



# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# main game loop
while True:
    # move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # Move eny back & down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # Move bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

wn.mainloop()
delay = input("Press enter to finish.")
