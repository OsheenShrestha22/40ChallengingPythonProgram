print("Welcome to Binary/Hexadecimal Converter App")
num = int(input("Compute binary and hexadecimal values up to the following decimal number: "))

list = list(range(0,num+1))
print("Generating list....complete")
print("Using slices, we will now show a portion of each list")
start = int(input("What decimal number would you like to start at:"))
end = int(input("What decimal number would you like to stop at:"))

binary = []
hexacal = []
for num in list:
    binary.append(bin(num))
    hexacal.append(hex(num))

print(f"\nDecimal values from {start} to {end} :")
for i in list[start:end+1]:
    print(i)

print(f"\nBinary values from {start} to {end} :")
for i in binary[start:end+1]:
    print(i)

print(f"\nHexacal values from {start} to {end} :")
for i in hexacal[start:end+1]:
    print(i)


print(f"\n Enter to see all of the values from 1 to {num}")
print("Decimal-----------Binary---------Hexadecimal")
print("---------------------------------------------------")
for a,b,c in zip(list,binary,hexacal):
    print(f"{a} --------{b}-----{c}")