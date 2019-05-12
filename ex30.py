people = 30
cars = 40
buses = 15


if cars > people: # looks to see if the number of cars is greater than the number of people
    print("We should take the cars")
elif cars < people: # if the statement is true then this is printed
    print("We should not take the cars")
else: # if the statement is false then this statement is printed.
    print("We can't decide")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("may we could take the buses")
else:
    print("We Still can't decide")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
