import math
def calculate_circumference(radius):
    if radius < 0:
        return "Radius cant be negative"
    return 2 * math.pi * radius
r = float(input("enter radius of circle: "))
circumference = calculate_circumference(r)
print("The circumference of circle is: ", circumference)