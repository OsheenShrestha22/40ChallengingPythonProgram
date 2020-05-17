import cmath
print("Welcome to Quadratic Solver App.")
print("The quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solution can be a real or complex numbers.")
print("A complex number has two parts: a+bj")
print("Where a is an real portion and bj is the imaginary portion:")

num = int(input("\nHow many equations would you like to solve todday:"))



for i in range(num):
    print(f"\nSolving equation #{i+1}")
    print("--------------------------------------------------------------------------------------------------------")
    a = int(input("\nPlease enter your value of a(coefficient of x^2):"))
    b = int(input("Please enter your value of b(coefficient of x):"))
    c = int(input("Please enter your value of c(coefficient):"))
    print(f"The solution to {a}x^2 + {b}x + {c} are:")
    d = b**2 -(4*a*c)
    x1 =(-b-cmath.sqrt(d))/(2*a)
    x2 =(-b+cmath.sqrt(d))/(2*a)
    print(f"x1 ={x1}")
    print(f"x2 ={x2}")