from turtle import *
r=Turtle()
ws=Screen()
ws.title("my first turtle programme")
#ws.bgcolor("red")
ws.bgpic("SmallFullColourGIF.gif")
r.shape("turtle")
r.hideturtle()
r.speed(1)
r.color("blue","yellow")# first color is pen color and second color is fillcolor
r.begin_fill()
for i in range(4):
    r.forward(100)
    r.left(90)
r.penup()
r.forward(200)
r.pendown()
for i in range(4):
    r.forward(100)
    r.left(90)
#r.forward(100)
#r.left(90)
#r.forward(100)
#r.left(90)
#r.forward(100)
r.end_fill()
done()