ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"thre's {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some thing with stuff.")

print(stuff[1])
print(stuff[-1]) # Whoa! Fancy
print(stuff.pop())
print(' '.join(stuff)) # What? Cool!
print(' '.join(stuff[3:5])) # Super Stellar! # The 3:5 is getting a "Slice" from the stuff list that is from element 3 to element 4. It does not include element5, kinda like how range (3,5) would work.


print("""
-----Study Drills-----

Q: Take each function that is called, and go through the steps outlined above to translate them to what python does.
For example ' '.join(things) is join(' ', things).
A:

Q: Translate these two ways to view the function calls. For example, ' '.join(things) reads as, "join things with '' between them."
meanwhile,join('', things)means, "Call join with ' ' and things." Understand how they are really the same thing.
A:

Q: Go read about "object-oriented programing" online. Confused? I was too. Do not worry. You will learn enough to be dangerous, and
you can slowly learn more later.
A:  Explanations: https://medium.freecodecamp.org/object-oriented-programming-concepts-21bb035f7260

Python is a Object-Oriented programming (OOP) language and focuses on createing reusable patterms of code, in contrast to Procedural Programming, which focuses on explicit sequencde instructions.

The four principles of object-oriented programming are
1. Encapsulation:
Is achieved when each object keeps its state private, inside a class. Other objects don't have direct access to this state. Instead, they can only call a list of public functions - called methods.

2. Abstraction:
This mechanism should hide internal implementation details. It should only reveal operations relevant for the other objects. e.g. A coffee Machine. It does a lot of stuff and has a lot of operational parts under the the hood.
But all you have do is put in coffee and press a button. Preferably, this mechanism should be easy to use and should rarely change over time.

3. Inheritence:
A common problem in OOP(Object-Oriented Design) design is objects are often very similar. They share common logic but they're not entirely the same. To reuse common logic and extra the unique logics into a seperate clasee we use inheritance.
It means you create a (child) class by derving frome another (parent) class. To form a hierachy.

4. Polymorphism:
Means "Many shapes" in Greek
Polymorphism gives a way to use a class exactly like its parent so there's no confusion with mixing types. But each child class keeps its own methods as they are.

This typically happens by defining a (parent) interface to be reused. It outlines a bunch of common methods. Then, each child class implements its own version of the methods.

Any time a collection (such as a list) or a method expects an instance of the parent (where common methods are outlined), the language takes care of evaluating the right implementation of the common method - regardless of which child is passed.

E.g. https://medium.freecodecamp.org/object-oriented-programming-concepts-21bb035f7260 (see diagram)
Geometric figures reuse a common interface for calculating surface area and perimeter. "Figure interface" let's you create a mixed list of "triangles", "circles", and "rectangles". And treat them like the same type of object.
Then, if this list attempts to calculate the surface for an element, the correct method is found and executed. This means you don't have to define it 3 times. You can define it once and accept a "figure" as an argument. Whether you pass a triange, circle, or a rectangle. As long as they implement CalculateParameter(), their type doesn't matter.


Q: Read up on what a "class" is in Python. DO NOT read about how other languages use the word "class". That Will only mess you up
A:
Resources:
https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3

Class:
A blueprint created by a programmer for an object. This defines a set of attributes that will characterize any object that is instantiated from this class.

Object:
An instance of a class. This is the realized version of the class, where the class is manifested in the program.

Example:

Classes:

We define classes by using the class keyword, similar to how we define functions by using the def keyword.

Let's define a class called Shark that has two fucntions associate with it, one for swimming and one for being awesome.
""")

class Shark:
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("the shark is being awesome")

print("""
Because there functions are indented under the class "Shark". they are called Methods.
Methods are a special kind of function that are defined in a class.

The argument to these functions is the word "self", which is reference to objects that are made based on this class. To reference instances(or objects) of the class, "self" will alwys be the first parameter, but it need not be the only one.

Defining this class did not create any "Shark" objects, only the pattern for a "Shark" object that we can define later. That is, if you run the program above at this stage nothing will returned.

Creating the "Shark" class above procided us with a blueprint for an object.


Objects:
An object is an instance of a class. We can take the "Shark" class defined above, and use it to create an object or an instance of it.
We'll make a "Shark" object called "sammy":
""")

sammy = Shark()

print("""
Here, we initialized the object "sammy" as an instance of the class by settting it equal to "Shark()"
""")

sammy.swim()
sammy.be_awesome()

print("""
The "Shark" object "sammy" is using the two methods "swim()" and "be_awesome()". We called these using the dot operator (.), which is used to reference an attribute of the object. In this case, the attribute is a methid and it's called with parentheses, like how you would also call a function.

Because the keyword "self" was a parameter of the methods as defined in the "Shark" class, the "sammy" object gets passed to the methods. The "sef" parameter ensures that the methods have a way of referring to object attributes.

When we call the methods, however, nothing is passed inside the parentheses, the object "sammy" is being automatically passed with the dot operator.
""")

def main():
    sammy = Shark()
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()

# what does the program do?
####### Output ########
# The shark is swimming
# The shark is being awesome
print("""
The object "sammy" calls the two methids in the "main()" function of the program, causing those methods to run.
""")

print("""
Q: What's the realtionship between dir(something) and that "class" of something?
A:
Syntax: dir({object})
dir() tries to return a valid list of attributes of the object it is called upon. dir() function behaves differently with different types of objects, as it aims to produce the most relevant one, rather than the complete information.
- Class Objects: Returns the list of names of all the valid attributes and base attributes as well.
- Modules/Library objects: Rries to return a list of names of all the attributes, contained in that module.
- No parameters: Returns a list of names in the current local scope.
/
Q: If you dont have any idea what i'm talking about, do not worry. Programmers like to feel smart, so they invented Object Oriented
Programming named it OOP, and the used it way too much. If you think that's hard, you should try to use "Functional Programming."
A:
""")
