#Remember PEMDAS as PE(M&D)(A&S) (Please Excuse My Dear Aunt Sally)
#P = Parentheses (Brackets)
#E = Exponents (Powers, Roots)
#M = Multiplication (*)
#D = Division (/ or %)
#A = Addition (+)
#S = Subtraction (-)

#modulus operators = Whatevers on the right side is the length of the circle And when you reach the limit you go back to zero So 2 % 4 = 2 because the length of the circle is 4.
# 3 % 4 = 3
# 4 % 4 = 0
# 5 % 4 = 1

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6) # Adds 25 to (30/6) which is 25 + 5 to give 30 hens
print("Roosters", 100 - 25 * 3 % 4) #due to PEMDAS it's 100 - 3 (25*3 = 75. then 75 *0.04(4%) = 3) there for there are 97 Roosters.

print("now I will count the eggs:")

### Answer is 6.75 but I keep getting 6.83
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) #due to PEMDAS the simple formula is
#print(3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6)
#print(6.00 - 5.00 + 0.08 - 0.00 + 6.00) #(4 % 2) is a modulus operator which means that the result is the remainder of 4/2 which is 0

#print(6.75)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)
#print(5 < -2) = true

print("What is 3 + 2?", 3 + 2) # = 5
print("What is 5 - 7?", 5 - 7) # = = -2

print("oh, that's why it's False")

print("How about some more.")

print("Is it greater?", 5 > -2) #= true
print("Is it greater or equal?", 5 >= -2) #= true
print("Is it less or equal?", 5 <= -2) #= false

print("this is 7.0 / 4.0", 7.0 / 4.0)
print("this is 7 /4 ", 7 / 4)
