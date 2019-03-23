name = 'Zed A. Shaw'
age = 29 # not a lie
height = 72.4409 # inches
weight = 198.416 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_conv = 2.54 # 1 inch = 2.54cm's
pound_conv = 0.453592 # 1 pound = 0.453592 Kg's
height_cm = round(height * inch_conv)
weight_kg = round(weight * pound_conv)
height_rounded = round(height) #rounding height to numerials before decimal place
weight_rounded = round(weight) #rounding height to numerials before decimal place

print(f"Let's talk about {name}.")
print(f"he's {height} inches tall.")
print(f"he's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"he's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right

total = age + height_rounded + weight_rounded
total2 = age + height_cm + weight_kg #cm and kg conversion totals
print(f"If I add {age}, {height_rounded}inchs, and {weight_rounded}pounds, I get {total}.")
print(f"if I add {age}, {height_cm}cm, and {weight_kg}kg, I get {total2}.")


# Try to write some variables that convert the inches and pounds to centimeters and kilograms.
# Do not just typ ein the measurements. Work out the math in python
