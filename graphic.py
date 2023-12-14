from turtle import *
import colorsys

tracer(2)
pensize(2)
speed(0)
h = 1
bgcolor("black")
setheading(80)

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    pencolor(c[0], c[1], c[2])
    h += 0.008
    fd(i)
    rt(51)
    rt(50)
    fd(200)
    rt(120)

done()
exitonclick()  # This line adds a stopping point
