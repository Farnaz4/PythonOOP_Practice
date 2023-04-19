#Abstract Class
from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def method1(self):
        pass
#===================================

class B(A):

    def method1(self):
        print("Method 1 is overridden")

#==========================================
# class B(A):
#
#     @abstractmethod
#     def method2(self):
#         pass
# #==========================================
# class C(B):
#
#     def method3(self):
#         pass



b = B()
b.method1()
