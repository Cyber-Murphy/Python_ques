class Computer:
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("The model of the computer is :",self.cpu,self.ram)

comp1= Computer('ryzen','4gb')
comp1.config()
        