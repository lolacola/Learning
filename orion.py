# This program draws a stars of the Orion constellation,
# the names of the stars, and the constallation

import turtle

# Set the windows size
turtle.setup(500, 600)

# Setup the turtle
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates.

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw and name the stars.

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)               # Left shoulder
turtle.dot()
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)             # Right shoulder
turtle.dot()
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)               # Left belt star
turtle.dot()
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)           # Middle belt star
turtle.dot()
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)             # Right belt star
turtle.dot()
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)                       # Left Knee
turtle.dot()
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)                     # Right knee
turtle.dot()
turtle.write('Rigel')

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)               # Left shoulder
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)               # Left belt star
turtle.penup()

turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)             # Right shoulder
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)             # Right belt star
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)               # Left belt star
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)           # Middle belt star
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)             # Right belt star
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)               # Left belt star
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)                       # Left Knee
turtle.penup()

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)             # Right belt star
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)                     # Right knee
turtle.penup()





turtle.done()