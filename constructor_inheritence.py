class A:
    def __init__(self):
        print('1')
    def value(self):
        print('value 1')

class B(A):
    def __init__(self):
        super.__init__()
        print('2')
    def value(self):
        print('value 2')

a1=B()