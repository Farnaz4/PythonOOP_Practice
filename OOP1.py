
class Student:
    def __init__(self, name, Id):
        self.name=name
        self.id= Id
        print("A student object has been created")
    def details(self):
        print("Name:", self.name, ", ID:", self.id)



#===========================================

#variable = class_name()
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s2.id = 33

s1.details()
s2.details()

print(s1.name)
print(s2.id)

#print("s1", s1)
#print("s1", s1)


