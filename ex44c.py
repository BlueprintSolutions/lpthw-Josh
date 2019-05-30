class Parent(object):

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def altered(self):
        print("Child, BEFORE Parent altered()")
        super(Child,self).altered() # call super with arguements Child and self, then call the function altered on whatever it returns.
        print("Child, AFTER Parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
