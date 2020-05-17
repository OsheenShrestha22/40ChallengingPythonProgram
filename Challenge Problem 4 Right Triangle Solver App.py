import math

print("Welcome to the Right Triangle Solver App")

p=float(input("\nWhat is the first leg of the triangle:"))
b=float(input("\nWhat is the second leg of the triangle:"))
hypotenuse = math.hypot(p,b)
hypotenuse = round(hypotenuse,3)

area = 0.5 * p * b
print(f"\nFor a tringle with legs of {p} and {b} the hypotenuse is {hypotenuse} ")
print(f"\n For a triangle with legs of {p} and {b}, the area is {area}")