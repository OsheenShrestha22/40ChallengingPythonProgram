import math
print("Welcome to Factorial Calculator App")

num = int(input("What number would you like to compute the factorial of?"))
print(f"{num}! =",end ='' )
for i in range(1,num):
    print(f"{i}*",end ='')
print(f"{num}")

print("\nHere is the result from the math library")
print(math.factorial(num))

print("\nHere is the result from own algorithm")

my_factorial = 1
for i in range(1,num+1):
    my_factorial = my_factorial * i
print(my_factorial)


print(f"It is shown twice that 10! = {my_factorial} (with excitement)")