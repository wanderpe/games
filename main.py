import turtle as t
import winsound
playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# creating right padlle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# creating ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# creating pen for scorecard update

pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0       PlayerB: 0", align="center", font=('Arial;', 24, 'normal'))


# moving the leftpaddle

# Assign keys to play


def leftpaddleup():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)


# moving the rightpaddle

def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 50
    rightpaddle.sety(y)


def rightpaddleup():
    y = rightpaddle.ycor()
    y += 50
    rightpaddle.sety(y)


def events():
    window.listen()
    window.onkeypress(rightpaddleup, "Up")
    window.onkeypress(rightpaddledown, "Down")
    window.onkeypress(leftpaddleup, "w")
    window.onkeypress(leftpaddledown, "s")


while True:
    window.update()
    events()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerAscore += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(playerAscore, playerBscore), align="center", font=('Arial;', 24, 'normal'))




    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerBscore += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(playerAscore, playerBscore), align="center",
                  font=('Arial;', 24, 'normal'))





    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    # sounds

