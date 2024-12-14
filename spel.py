import turtle

wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("black")  
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("cyan")  
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")  
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")  
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("yellow")  
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  
ball.dy = -0.1  

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  
        paddle_b.sety(y - 20)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

def increase_ball_speed():
    ball.dx *= 1.25 
    ball.dy *= 1.25  

while True:
    wn.update() 

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  
        score_a += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b += 1  
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1  
        increase_ball_speed() 

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1  
        increase_ball_speed() 

