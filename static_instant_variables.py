class Car:
    wheel=4             # static or class variable
    def __init__(self):
        self.color="red" # color & mileage are instanteous variable
        self.mileage=34

c1=Car()
c2=Car()
c2.color="blue"
c1.wheel=3
print(c1.color)
print(c2.color)
print(c1.wheel)