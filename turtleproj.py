import turtle

turtle.setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.goto(-220, 220)
turtle.write('Hello World!')
turtle.goto(170, -220)
turtle.write("Bottom Left")
turtle.goto(-25, -50)
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()


turtle.reset()
turtle.hideturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.done()