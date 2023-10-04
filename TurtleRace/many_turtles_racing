import turtle 
import random

screen = turtle.Screen()
screen.bgcolor('green')

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-140, 140)

for step in range(15):
  t.write(step, align='center')
  t.right(90)
  for num in range(16):
    t.penup()
    t.forward(5)
    t.pencolor('white')
    t.pendown()
    t.forward(5)
  t.penup()
  t.backward(160)
  t.left(90)
  t.forward(20)
  t.hideturtle()
  
t1 = turtle.Turtle()
t1.color('red')
t1.shape('turtle')

t1.penup()
t1.goto(-160, 100)
t1.pendown()

t2 = turtle.Turtle()
t2.color('pink')
t2.shape('turtle')

t2.penup()
t2.goto(-160, 70)
t2.pendown()

t3 = turtle.Turtle()
t3.shape('turtle')
t3.color('blue')

t3.penup()
t3.goto(-160, 40)
t3.pendown()

t4 = turtle.Turtle()
t4.shape('turtle')
t4.color('orange')

t4.penup()
t4.goto(-160, 10)
t4.pendown()

for turn in range(100):
  t1.forward(random.randint(1,5))
  t2.forward(random.randint(1,5))
  t3.forward(random.randint(1,5))
  t4.forward(random.randint(1,5))
     
