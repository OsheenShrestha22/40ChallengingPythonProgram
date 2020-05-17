print("Welcome to the Multiplication/Exponential Table App")
name = input("\nWhat is your name:").title().strip()
number = float(input("\nWhat number would you like to work with:"))
print(f"\nMultiplication Table For {number}")
for i in range (1,10):
    print(number, 'x', i, '=', number * i)

print(f"\nExponential Table For {number}")
for i in range(1,10):
    print(number, 'x',i, '=',number ** i)

messgae = name+"Math is cool!"
print(f"\t{messgae}")
print(f"\t\t{messgae.lower()}")
print(f"\t\t\t{messgae.title()}")
print(f"\t\t\t\t{messgae.upper()}")