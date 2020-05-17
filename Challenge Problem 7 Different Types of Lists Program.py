num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [2.2,5.0,1.245,0.142857]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

print("\t\t\tSummary Table\n")
print("The variable num_strings is a class " + str(type(num_strings)))
print(f"It contains the elements: {num_strings}")
print(f"The element {num_strings[0]} is a {str(type(num_strings[0]))}\n")

print("The variable num_ints is a class " + str(type(num_ints)))
print(f"It contains the elements: {num_ints}")
print(f"The element {num_ints[0]} is a {str(type(num_ints[0]))}\n")

print("The variable num_floats is a class " + str(type(num_floats)))
print(f"It contains the elements: {num_floats}")
print(f"The element {num_floats[0]} is a {str(type(num_floats[0]))}\n")

print("The variable num_lists is a class " + str(type(num_lists)))
print(f"It contains the elements: {num_lists}")
print(f"The element {num_lists[0]} is a {str(type(num_lists[0]))}\n")

print("Now sorting num_strings and num_ints....")
num_strings.sort()
num_ints.sort(reverse=False)
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}\n")

print("String are sorted alphabetically while integers are sorted numerically")