#composition

class Other(object):

    def override(self):
        print("Other Override()")

    def implicit(self):
        print("Other implicit")

    def altered(self):
        print("Other altered")

class Child(object):

    def __init__(self):
        self.Other = Other()

    def implicit(self):
        self.Other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, BEFORE other altered()")
        self.Other.altered()
        print("Child, AFTER other altered()")

son = Child()

son.implicit()
son.override()
son.altered()

print("Further reading about code styleguidelines https://www.python.org/dev/peps/pep-0008/")
