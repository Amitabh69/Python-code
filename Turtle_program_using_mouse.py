from turtle import *
r = Turtle()
ws = Screen()
ws.title("draw using mouse")
r.pencolor("green")
r.speed(-1)
# ondrag function will be used which is used to bind this function to mouse event
def paint(x,y):
    r.ondrag(None)
    r.setheading(r.towards(x,y))
    r.goto(x,y)
    r.ondrag(paint)

def erase(x,y):
    r.clear()


def main():
    ws.listen()
    r.ondrag(paint)
    ws.onscreenclick(erase,3)
    done()

main()
