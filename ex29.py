people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("the world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("people are less than or equal to dogs.")

if people == dogs:
    print("people are dogs")

if people != dogs:
    print("this was a test argument")



print("""
Q: What does the if statement do?
A: The if statement looks at the formula above it to see if the outcome is true.
If the specified outcome is true then it shows the result. E.g.

if people > dogs
if 20 > 15 (equals True) then show
Print("The world is drooled on")

Q: Why does the code under the if need to be indented four spaces?
A: Requirement of python so it knows that arguement is related to the statement above it.

Q: What happens if it isn't indented?
A: You get an error in the terminal to indent the line of code

Q: What happens if you change the inital variables for people, cats and dogs?
A: Then you will get different True and False outcomes pending on what you change the variables to.

""")
