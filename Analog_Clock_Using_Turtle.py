from turtle import *
import time
time.time()
r=Turtle()
ws=Screen()
ws.title("Analog Clock")
ws.bgcolor("white")
ws.setup(700,700)
r.speed(1)
r.pensize(3)
#r.hideturtle()
ws.tracer(0)

def draw_clock(h,s,m,r):
    r.penup()
    r.goto(0,210)
    r.setheading(180)
    r.pencolor("green")
    r.pendown()
    r.circle(210)
    # draw the clock marking for hand hours
    r.penup()
    r.goto(0,0)
    r.setheading(90)
    for v in range(12):
       r.forward(190)
       r.pendown()
       r.fd(20) # forward can be written as fd
       r.penup()
       r.goto(0,0)
       r.right(30)


    # draw the clock marking for minute and second hours
    r.penup()
    r.goto(0, 0)
    r.setheading(90)
    for v in range(60):
        r.forward(200)
        r.pendown()
        r.fd(10)  # forward can be written as fd
        r.penup()
        r.goto(0, 0)
        r.right(6)

    #drawing number on the clock
    #one
    r.penup()
    r.goto(0,0)
    r.setheading(60)
    r.fd(145)
    r.setheading(0)
    r.fd(15)
    r.write(1,move=False,align="center",font=("arial",25,"italic"))
    # two
    r.penup()
    r.goto(0, 0)
    r.setheading(30)
    r.fd(135)
    r.setheading(0)
    r.fd(35)
    r.write(2, move=False, align="center", font=("arial", 25, "italic"))
    # three
    r.penup()
    r.goto(0, 0)
    r.setheading(352)
    r.fd(150)
    r.setheading(0)
    r.fd(25)
    r.write(3, move=False, align="center", font=("arial", 25, "italic"))
    # four
    r.penup()
    r.goto(0, 0)
    r.setheading(315)
    r.fd(150)
    r.setheading(0)
    r.fd(45)
    r.write(4, move=False, align="center", font=("arial", 25, "italic"))
    # five
    r.penup()
    r.goto(0, 0)
    r.setheading(290)
    r.fd(178)
    r.setheading(0)
    r.fd(25)
    r.write(5, move=False, align="center", font=("arial", 25, "italic"))
    # six
    r.penup()
    r.goto(0, 0)
    r.setheading(270)
    r.fd(190)
    r.write(6, move=False, align="center", font=("arial", 25, "italic"))
    # seven
    r.penup()
    r.goto(0, 0)
    r.setheading(258)
    r.fd(178)
    r.setheading(188)
    r.fd(48)
    r.write(7, move=False, align="center", font=("arial", 25, "italic"))
    # eight
    r.penup()
    r.goto(0, 0)
    r.setheading(228)
    r.fd(150)
    r.setheading(188)
    r.fd(45)
    r.write(8, move=False, align="center", font=("arial", 25, "italic"))
    # nine
    r.penup()
    r.goto(0, 0)
    r.setheading(188)
    r.fd(150)
    r.setheading(188)
    r.fd(25)
    r.write(9, move=False, align="center", font=("arial", 25, "italic"))
    # ten
    r.penup()
    r.goto(0, 0)
    r.setheading(150)
    r.fd(135)
    r.setheading(180)
    r.fd(25)
    r.write(10, move=False, align="center", font=("arial", 25, "italic"))
    # eleven
    r.penup()
    r.goto(0, 0)
    r.setheading(120)
    r.fd(145)
    r.setheading(180)
    r.fd(15)
    r.write(11, move=False, align="center", font=("arial", 25, "italic"))
    # twelve
    r.penup()
    r.goto(0, 0)
    r.setheading(90)
    r.fd(150)
    r.write(12, move=False, align="center", font=("arial", 25, "italic"))

#  drawing clock hour hand
    r.pu()   #pu and penup is same
    r.goto(0,0)
    r.pencolor("red")
    r.setheading(90)
    angle=(h/12)*360
    r.rt(angle)
    r.pendown()
    r.fd(80)

    #drawing clock minute hand
    r.pu()  # pu and penup is same
    r.goto(0, 0)
    r.pencolor("blue")
    r.setheading(90)
    angle = (m / 60) * 360
    r.rt(angle)
    r.pendown()
    r.fd(120)

    # drawing clock second hand
    r.pu()  # pu and penup is same
    r.goto(0, 0)
    r.pencolor("yellow")
    r.setheading(90)
    angle = (s / 60) * 360
    r.rt(angle)
    r.pendown()
    r.fd(160)
    #design by-
    r.penup()
    r.goto(0,0)
    r.pencolor("black")
    r.setheading(268)
    r.fd(125)
    r.setheading(0)
    r.fd(5)
    r.write("Designed by Amitabh", move=False, align="center", font=("arial", 12, "italic"))
    r.hideturtle()

while True:
    h=int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    draw_clock(h,s,m,r)
    ws.update()
    time.sleep(1)
    r.clear()

mainloop()