print("Welcome to  the Temperature Conversion Program")
farenheit = float(input("\nWhat is the given temperatute in degress Fahrenheit:"))

celsius = (5/9)*(farenheit-32)
kelvin = celsius+273.15

farenheit = round(farenheit,4)
celsius = round(celsius,4)
kelvin = round(kelvin,4)

print(f"Degrees Farenheit\t: {farenheit}")
print(f"Degrees Celsius\t\t: {celsius}")
print(f"Degrees Kelvin\t\t: {kelvin}")
