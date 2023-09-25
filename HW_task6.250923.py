from turtle import *

color("red")
scale = 10
limit = 25
speed(0)
hideturtle()

pd()
begin_fill()
for i in range(2):
    forward(8 * scale)
    right(90)
    forward(18 * scale)
    right(90)
end_fill()


forward(4 * scale)
right(90)
forward(10 * scale)
left(90)

begin_fill()
for i in range(2):
    forward(17 * scale)
    right(90)
    forward(7 * scale)
    right(90)
end_fill()

pu()
count = 0
canvas = getcanvas()
tracer(0)
for y in range(0, limit * scale, scale):
    for x in range(0, limit * scale, scale):
        item = canvas.find_overlapping(x, y, x, y)
        if item:
            count += 1
            goto(x, -y)
            dot(5, 'black')

print(count)
done()