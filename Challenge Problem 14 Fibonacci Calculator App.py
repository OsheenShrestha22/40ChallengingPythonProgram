print("Welcome to Fibonancci Calculatop App")

n= int(input("How many digits of Fibonancci Sequence would you like to compute:"))
f = [1,1]
for i in range(n -2):
    new_feb= f[i] + f[i+1]
    f.append(new_feb)

print(f"\nThe first {n} numbers of the fibonanci sequence are:")
for number in f:
    print(number)


gold =[]

for i in range(len(f)-1):
    ratio = f[i+1]/f[i]
    gold.append(ratio)

print("The corresponding Golden ratio values are:")
for num in gold:
    print(num)


"""
this is alternative way to calculate fibonanci 

a,b = 0,1
for _ in range(n):
    a,b = b,a+b
    print(a)

print("")

for _ in range(n):
    a,b = b,a+b
    print(a/b)"""

