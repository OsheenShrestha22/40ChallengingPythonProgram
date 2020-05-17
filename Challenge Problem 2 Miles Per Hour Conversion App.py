print("Welcome to Miles per hour(MPH) to meters per second(MPS) Conversion App")
MPH = float(input("\nWhat is your speed in miles per hour:"))
MSP = MPH *0.44704
MSP = round(MSP,2) # Alternative Way to  round MSP_2 = "{:.2f}".format(MSP)
print(f"Your speed in meters per second is {MSP}")

