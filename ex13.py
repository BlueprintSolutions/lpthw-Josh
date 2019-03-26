from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
name = input("what is your name? ")

print(">>>> argv=", repr(argv)) #lets me know what the computer is doing and what data it is seeing

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your thrid variable is:", third)
print(f"my name is {name}, and I am counting a script {first}, {second}, {third}. How cool is that.")
print(f"now if I wanted to add an input as part of a argv? How would I do that?")
