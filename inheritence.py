class A:
    def value1(self):
       return  print('This is level 1 class')
    def value2(self):
        print('This is level 2 class')


#Single level
class B(A):
    def value3(self):
       return  print('This is level 3 class')
    def value4(self):
        print('This is level 4 class')
#multilevel
class C(B):
    def value5(self):
       return  print('This is level 5 class')
    def value6(self):
        print('This is level 6 class')

#multiple
class D:
    def value7(self):
        return print("this is level 7 class")
    
class E(A,D):
    def value8(self):
        return print('this is level 8 class')
    


a1=A()
b1=B()
c1=C()
e1=E()
# a1.value1()
# b1.value2()
# c1.value3()
e1.value2()
