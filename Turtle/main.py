from turtle import *

getscreen()
bgcolor("red")

pencolor("lime")
pensize(5)
shape("turtle")

speed(1)

init_size = 30

for i in range(36):
  for i in range(4):
    forward(init_size)
    left(360/4)
    left(10)

done()