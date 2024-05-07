def triangle_area(base, height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = triangle_area(base, height)
print("Area of the triangle:", area)
