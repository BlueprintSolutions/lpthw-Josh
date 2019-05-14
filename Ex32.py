the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kid of for-loop goes through a list.
for number in the_count:
    print(f"this is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type {fruit}")

# also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it.
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one.
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0, 6):
     print(f"Adding {i} to the list.")
     # append is a function that lists understand?
     elements.append(i)

#now we can print them out too.
for i in elements:
    print(f"elemts was {i}")


print("""
Q: Take a look at how you used range. Look up the range function to understand it.
A: The range() function is a built in function of python that generates the integer numbers between the given start integer to the stop integer.

Q: Could you have avoided the for-loop entirely on line 22 and just assigned range (0,6) directly to elements?
A: No as then elements would not of functioned inside the loopp that we have created and would of counted to 6 instead of 5. Would cause a syntax error as well.

Q: Find the python documentation on lists and read about them. What other operations can you do to lists besides append?
A: With lists you can insert, append, extend, remove, pop, index, count, sort, reverse, zip, compare and more see here (https://python-reference.readthedocs.io/en/latest/docs/list/)

""")
