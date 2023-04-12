class Student:
    counter = 0

    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        Student.counter += 1

    def details(self):
        print("Name:", self.name, "ID", self.Id)

#=======================================

print("Student Count", Student.counter)
s1 = Student("Bob", 11)
s2 = Student("Mike", 33)
s3 = Student ("Gigi", 44)
s1.details()
s1.details()

print("Student Count", Student.counter)