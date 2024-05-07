import turtle

# Creates a Turtle screen
screen = turtle.Screen()

# Creates a Turtle object
t = turtle.Turtle()

# Drawing a rectangle
for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)

# Keep the screen open until the user closes it
screen.mainloop()
