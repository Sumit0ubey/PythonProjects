import turtle

# Create a Turtle screen
screen = turtle.Screen()

# Create a Turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Keep the screen open until the user closes it
screen.mainloop()
