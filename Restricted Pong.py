import turtle
import random

wn = turtle.Screen()    #SCREEN CREATION
wn.title("Restricted Pong")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0)



#Score
score_a=0
score_b=0


#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto((-350,0))

#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto((350,0))

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto((0,0))
ball.dx=0.2
ball.dy=-0.2

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"bold"))

#design(MIDDLE LINE)
lines=turtle.Turtle()
lines.speed(0)
lines.color("white")
lines.penup()
lines.shape("square")
lines.goto(0,0)
lines.shapesize(stretch_wid=30, stretch_len=0.2)
lines.hideturtle()


#countdown
pen1=turtle.Turtle()
pen1.speed(0)
pen1.penup()
pen1.hideturtle()
pen1.goto(0,0)



#Function
def paddle_a_up():
    y=paddle_a.ycor()
    if(ball.dx<0):
        y+=30
    if(y>290):
        paddle_a.sety(-290)
    else:
        paddle_a.sety(y)



def paddle_a_down():
    y=paddle_a.ycor()
    if(ball.dx<0):
        y-=30
    if(y<-290):
        paddle_a.sety(290)
    else:
        paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    if(ball.dx>0):
        y+=30
    if (y > 290):
        paddle_b.sety(-290)
    else:
        paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    if(ball.dx>0):
        y-=30
    if (y <-290):
        paddle_b.sety(290)
    else:
        paddle_b.sety(y)





#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

time =1500
f=1
countdown=4000

while True:
    wn.update()

    countdown-=10
    if(countdown>=3000):
        #pen1.clear()
        lines.hideturtle()
        pen1.color("red")
        pen1.write("3", align="center", font=("Courier", 40, "bold"))
        if(countdown==3000):
            pen1.clear()
    elif(countdown>=2000):
        #pen1.clear()
        pen1.color("orange")
        pen1.write("2", align="center", font=("Courier", 40, "bold"))
        if (countdown == 2000):
            pen1.clear()
    elif (countdown >= 1000):
        #pen1.clear()
        pen1.color("yellow")
        pen1.write("1", align="center", font=("Courier", 40, "bold"))
        if (countdown == 1000):
            pen1.clear()
    elif (countdown >= 0):
        #pen1.clear()
        pen1.color("green")
        pen1.write("GO", align="center", font=("Courier", 40, "bold"))
        if (countdown == 0):
            pen1.clear()
    else:
        lines.showturtle()
        pen1.clear()
        #Move the ball
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

    if(ball.dx>0):
        if(ball.xcor()<0):
            ball.color("black")
        elif(ball.xcor()>0):
            ball.color("white")
    elif(ball.dx<0):
        if(ball.xcor()>0):
            ball.color("black")
        elif(ball.xcor()<0):
            ball.color("white")


   # if(time>0 and f==1 and countdown<0):
    #    ball.color("white")
     #   time-=1
    #elif(f==1 and countdown<0):
    #    time=-500
    #    f=0
    #if(time<0 and f==0 and countdown<0):
     #   ball.color("black")
     #   time+=1
    #elif(f==0 and countdown<0):
    #    time=1000
     #   f=1


    #Border checking
    if(ball.ycor()>290):
        ball.sety(290)
        ball.dy *= -1

    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        score_a += 1
        ball.goto(0, 0)
        time = 1500
        f=1
        sign = [-1, 1]
        rand = random.choice(sign)
        ball.dx = 0.2 * int(rand)
        countdown = 4000
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))


    if ball.xcor()<-390:
        score_b += 1
        ball.goto(0, 0)
        time = 1500
        f=1
        sign = [-1, 1]
        rand = random.choice(sign)
        ball.dx = 0.2 * int(rand)
        countdown = 4000
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    #collisions
    if ball.xcor()>=330 and ball.xcor()<=340 and (ball.ycor() <= paddle_b.ycor()+50 and ball.ycor()>=paddle_b.ycor()-50):
        ball.setx(330)
        ball.dx *= -1.2

    if ball.xcor()<=-330 and ball.xcor()>=-340 and (ball.ycor() <= paddle_a.ycor()+50 and ball.ycor()>=paddle_a.ycor()-50):
        ball.setx(-330)
        ball.dx *= -1.2

    if(score_a>1 or score_b>1):
        break;







