#Str overriding

class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = id
        #print(self)

    def __str__(self):
        return "My name is " + self.name

#==============================================
s1 = Student("Bob", 11)
s2 = Student("Carol", 12)
print(s1)
#print(s1.__str__())