import turtle

# Creates a Turtle screen
screen = turtle.Screen()

# Creates a Turtle object
t = turtle.Turtle()

# Taking the number of sides for the polygon input from the user
num_sides = int(input("Enter the number of sides for the polygon: "))

# Draws the polygon
for _ in range(num_sides):
    t.forward(100)
    t.right(360 / num_sides)

# Keep the screen open until the user closes it
screen.mainloop()
