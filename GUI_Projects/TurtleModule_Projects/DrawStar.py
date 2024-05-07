import turtle

# Create a Turtle screen
screen = turtle.Screen()

# Create a Turtle object
t = turtle.Turtle()

# Draw a star
for _ in range(5):
    t.forward(100)
    t.right(144)

# Keep the screen open until the user closes it
screen.mainloop()
