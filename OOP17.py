class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

#===========================================

class Dog(Animal):

    def bark(self):
        print(self.name, "is barking")

#==========================================

a1 = Animal("Max")
d1 = Dog("Rover")
# d1.bark()
# d1.eat()
# a1.bark()

#isinstance(Object, ClassName)
#print(isinstance(a1.Dog))
#issubclass(Class, ClassName)
print(issubclass(Animal, Dog))