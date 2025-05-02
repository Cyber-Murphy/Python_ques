class Person:
    def __init__(self):
        self.name="Gaurav"
        self.age=24

    def check(self, other):

        if self.name==other.name:
            return True
        else:
            return False





c1=Person()
c1.name="rahul"
c2=Person()


if c1.check(c2):
    print("Same name")
else:
    print("different name")


