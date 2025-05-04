class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.det=self.Details()

    def show(self):
        print(self.name,self.roll)
        self.det.hero()

    class Details:
        def __init__(self):
            self.address='mumbai'
            self.house=44
        def hero(self):
            print(self.address,self.house)

s2=Student('mohan',32)

print(s2.show())
# print(s2.name,s2.roll)