import turtle

GAME_SPEED = 0.2


wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.tracer(0)

# Shapes default to 20px
bot1 = turtle.Turtle()
bot1.penup()
bot1.shape('square')
bot1.color('red')
bot1.shapesize(stretch_wid=5, stretch_len=1)
bot1.goto(-350, 0)
bot1_dy = 0 * GAME_SPEED

bot2 = turtle.Turtle()
bot2.penup()
bot2.shape('square')
bot2.color('blue')
bot2.shapesize(stretch_wid=5, stretch_len=1)
bot2.goto(350, 0)
bot2_dy = 0 * GAME_SPEED

ball = turtle.Turtle()
ball.penup()
ball.shape('circle')
ball.color('black')
ball_dx = 2 * GAME_SPEED
ball_dy = 2 * GAME_SPEED


while True:
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    bot1.sety(bot1.ycor() + bot1_dy)
    bot2.sety(bot2.ycor() + bot2_dy)
    
    wn.update()
    
