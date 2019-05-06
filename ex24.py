print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n \t \t where there is none.
"""

print("-----------------")
print(poem)
print("-----------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print(f"with a starting point of {start_point}") #this is one way of formatting a print string
print("Or we can print like this, With a starting point of:{}".format(start_point)) #this is another way of formatting a print string
print(f"We'd have {beans} beans, {jars} Jars, and {crates} crates")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point) #easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} creates.".format(*formula)) #shows the list results in a print function.
