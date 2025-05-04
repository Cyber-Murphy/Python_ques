class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
c1=Student(10,10,10)
c2=Student(20,20,20)
    
print(c1.avg())
print(c2.avg())