def add (a,b):
    print(f"ADDING {a} + {b}")
    return(a+b)

def subtract (a,b):
    print(f"SUBTRACTING {a} - {b}")
    return(a-b)

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return(a*b)

def divide(a,b):
    print(f"DIVIDING {a} / {b})")
    return(a/b)

def charisma(a,b): #my own definition
    print(f"Charmisa formula {a} / {b} * {b}")
    return(a/b*b)

def life (a,b,c):
    print(f"LIFE is {a} + {b} / ({c} * {a})")
    return(a+b/(c*a))



print("let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}")


# A puzzle for extra credit type it in anyway
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what2 = age + height - (weight * iq/2)


print(f"That becomes: {what} can you do it by hand?")
print(f"That becomes the simple {what2} formula")

#trying to figure out what Python is doing
print("formula")
add2 = subtract(height, multiply(weight, divide(iq, 2)))
print(">>>> add2", add2)
subtract2 = multiply(weight, divide(iq,2))
print(">>>> subtract2", subtract2)
multiply2 = divide(iq,2)
print(">>>> multiply2", multiply2)
divide2 = (iq,2)
print(">>>> divide 2", divide2)

print(f"""
To show how Python is calculating this
p1 = divide(iq,2)
p1 = ((100/2)/2)
p1 = 25

p2 = multiply(weight, 25)
p2 = ((90 * 2) * 25)
p2 = 180 * 25
p2 = 4500

p3 = subtract(height, 4500)
p3 = 74 - 4500
p3 = 4426

p4 = add(age, -4426)
p4 = 35 + -4426
p4 = -4391

A shorter formula would be age + height - (weight * iq/2)
""")
print("""

Let's add some space here for my equation
""")
#my equation

age2 = add(30, multiply(78,4))
height2 = int(divide(500,6))
weight2 = subtract(100,5)
iq2 = int(divide(2312,4))
strength2 = int(multiply(height2,iq2))
charisma2 = int(charisma(iq2,age2))
life2 = int(life(strength2,charisma2,age2))

print(f"""
Age: {age2},
Height: {height2},
Weight: {weight2},
IQ: {iq2},
Strength: {strength2},
Charisma: {charisma2},
Life: {life2}
""")
