i = 0
numbers = []

print("what sort of number sequence do you want? Choose a number between 1 and 10")
choosennumber = input("> ")

print("How much do you want it to increase by?")
increasenumber = input("> ")


while i < int(choosennumber):
    print(f"At the top is {i}")
    numbers.append(i)

    i = i + int(increasenumber) #Added a variable the user can adjust for how much it counts by.
    print("Numbers now:", numbers)
    print(f"At the bottom is {i}")


print("The numbers:")
for num in numbers:
    print(num)


print("""
Q: Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
A: Added a input of choosennumber so the user can select the number they want to input and replaced the (i < 6) with this value.

Q: Now use this function to rewrite the script to try different Numbers
A: Did that with my input function above

Q: Add another variable to the function arguments that you pass in that lets you change the + 1 on line 8, so you can change how much it increments by.
A: Did this as part of question 1 as well.

Q: Rewrite the script again to use this function to see what effect that has.
A:
""")

print("For loops function")

ii = 0
numbers2 = []

for ii in range (0,int(choosennumber) + 1):
    print(f"At the top is {ii}")
    numbers2.append(ii)
    print("Numbers now:", numbers2)
    print(f"At the bottom is {ii}")

print ("The numbers:")
for num in numbers2:
    print(num)
