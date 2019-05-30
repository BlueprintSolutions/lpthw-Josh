class Parent(object):

    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")
        print("Alter what?")

class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        print(">>> Child BEFORE Parent altered()")
        super(Child, self).altered()
        print(">>> Child AFTER Parent altered()")
        print("This is altered")

dad = Parent()
son = Child()

dad.implicit() # will print Parent implicit
son.implicit() # will print parent implicit as Parent Implict() it creates a class called child and inherits it's behaviour from Parent().

dad.override() # will print Parent override()
son.override() # will print Child override(), Child overrides the function of Parent by defining it's own version

dad.altered() # will print parent altered()
son.altered() # will print
# Child, BEFORE PARENT altered()
# Parent altered()
# Child, AFTER parent altered()  When Child is altered it adds to the function defined by Parent.
