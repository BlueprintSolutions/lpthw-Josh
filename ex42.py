## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object): # can be written as class Animal: or class Animal():
    pass

## class dog is-a Animal
class Dog(Animal):

    def __init__(self, name, owner):
        ## class dog has-a __init__ that takes self and name parameters.
        self.name = name
        self.owner = owner
        print(f"My name is {name} and my owner is {owner}.")

## class cat is-a Animal
class Cat(Animal):

    def __init__ (self,name, owner):
        ## class cat has-a __init__ that takes self and name parameters.
        self.name = name
        self.owner = owner
        print(f"My name is {name} and my owner is {owner}.")

## class Person is-a object
class Person(object):

    def __init__ (self,name):
        ## class Person has-a __init__ that takes self and name parameters.
        self.name = name

        ## person has-a pet of some kind
        self.pet = None # making sure the elif class here is set to none.
        print(f"My name is {name} and I have no pets.")

## class Employee is-a person
class Employee(Person):

    def __init__ (self, name, salary):
        ## ?? hmm what is this strange magic?
        ## Return a proxy object that delegates method calls to a parent or sibling class of type.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary
        print(f"My name is {name} and my salary is {salary}")

## Class Fish is-a object
class Fish(object):
    pass # this is in here so passes onto the next class without throwing up an error.

## Class Salmon is-a object
class Salmon(Fish):
    # pass
    def __init__(self,type, colour):
        self.type = type
        self.colour = colour
        self.owner = None
        print(f"I am a {type} fish and my colour is {colour}. Currently I don't have an owner.")

## Class Halibut is-a object
class Halibut(Fish):
    # pass
    school = [] #empty list

    def __init__(self,name):
        self.name = name
        halibut.school.append(self)
        print(f"Hi I live in the {school}")


## rover is-a Dog
## Set rover to an instance of class Dog, which has-a attribute of name set to Rover. Class Dog was called with params self and Rover.
rover = Dog("Rover", "Frank")
print(rover)

## Satan is-a cat
## set satan to an instance of Cat, which has-a attrbute of name set to Satan. Class Cat was called with params self and Satan.
Satan = Cat("Satan", "Frank")
print(Satan)

## set mary to an instance of Person, which has-a attribute name set to Mary. Class person was called with params self, Mary and the attribute pet.
mary = Person("Mary")
print(Person)

## from Mary get the pet attribute and set it to Satan
mary.pet = Satan

## Frank is-a employee instance has-a attribute of Frank and attributes salary of 120,000
frank = Employee("Frank", 120000)
print(Employee)

## pet attribute of franks is-a rover
frank.pet = rover

## flipper is-a fish instance
flipper = Fish()

## crouse is-a salmon instance
crouse = Salmon("Salmon", "blue")

## harry is-a halibut instance
harry = Halibut("Great Barrier Reef")
sam = Halibut("Great Ocean")
print(Halibut.school)


print("""
Study Drills:
Q: Research why python added this strange object class and what that means:
A:http://python-history.blogspot.com/2009/02/adding-support-for-user-defined-classes.html

Q: IS it possible to use a class like it's an object?
A: Yes everything in python is an object including classes. (https://softwareengineering.stackexchange.com/questions/245929/using-class-like-an-object-in-python)

Q: Fill out the animals, fish and people in this excerise with functions that make them do things. See what happens when fuctions are in a "bare class" like Animal versus Dog.
A: see above

Q: Find other people's code and work out all the is-a and has-a relationships:
A: Done

Q: Make sure new relationships that are lists and dicts so you also have "has-many" relationships. (This is when you use a dict or lists in a class.)
A: Tried to do a list but couldn't get it to work under the class Halibut

Q: Do you think there's such thing as an "is-many" relationship? Read about "multiple in-heritance," then avoid it if you can.
A: There is and it can get really messy see here - https://www.programiz.com/python-programming/multiple-inheritance

Q: Search for "Python super" and read the various advice on it being evil and good for you:
A: https://www.pythonforbeginners.com/super/working-python-super-function

""")
