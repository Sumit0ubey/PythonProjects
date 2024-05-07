import turtle

# Creates a Turtle screen
screen = turtle.Screen()

# Creates a Turtle object
t = turtle.Turtle()

# Draws a square with pen up and down
t.penup()
t.goto(-50, 0)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)

# Keep the screen open until the user closes it
screen.mainloop()
