class Song(object): #class style

    def __init__(self, lyrics): # instantiation and shortcut for a creating a variable
        self.lyrics = lyrics # The variable could be equal to a text, a number or a variable

    def sing_me_a_song(self): # create a class function
        for line in self.lyrics:
            print(line)


# instance
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

# instance
bulls_on_parade = Song(["They rally around tha family",
                        "With a pocket full of shells"])

# instance
another_brick = Song(["We don't need no educaton", # New song
                      "We don't need no thought control",
                      "No dark sarcasm in the classroom"])

# not an instance
another_brick2 = ["We don't need no educaton",
                  "We don't need no thought control",
                  "No dark sarcasm in the classroom"]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

another_brick.sing_me_a_song()

lyricsImagine = ["image there's no heaven", # Q2: lyrics in a seperate variable.
                 "It's easy if your try",
                 "Imagine there's no country"]
SongImagine = Song(lyricsImagine)
SongImagine.sing_me_a_song()





print("-" * 10)
print("Study Drills")
print("""
Q: Write some more songs using this, and make sure you understand that you're passing a list of strings at the lyrics.
A: Added

Q: Put the lyrics in a seperate variable, then pass that variable to the class to use instead.
A: See Song Imagine

Q: See if you can hack on this and make it do more things. Don't worry if you have no idea how, just give it a try, see what happens. Break it, trash it, you cna't hurt it.
A:

Q: Search online for "Object-oriented programming" and try to over your brain with what you read. Don't worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me either.
A:
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

""")
