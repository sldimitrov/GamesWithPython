import turtle 

sl = turtle.Turtle()
sl.pensize(5)
def square():
  for x in range(4):
    sl.back(100)
    sl.right(90)

sl.penup()
sl.setpos(-20,0)
sl.color('green')
sl.pendown()
square()

sl.penup()
sl.setpos(100,0)
sl.color('red')
sl.pendown()
square()

sl.penup()
sl.setpos(-20,-120)
sl.color('blue')
sl.pendown()
square()  

sl.penup()
sl.setpos(100,-120)
sl.color('yellow')
sl.pendown()
square()
