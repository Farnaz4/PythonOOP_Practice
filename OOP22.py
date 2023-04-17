"Method Overriding"

class A:
    def __init__(self):
        print("__init__of class A")

    def method(self):
        print("Don't Study")

    def method2(self):
        print("You will get all of my methods and properties")

#============================================

class B(A):
    def __init__(self):
        pass
        #print("__init__ of B")
    def method(self):
        super().method()
        print("Always Study")

#==============================================

b1 = B()
b1.method()
b1.method2()

