class Student:

    def __init__(self, name, Id):
        self.name = name
        self.id = Id


    def details(self):   #instance method
        print("Name:", self.name, "ID", self.id)

#========================================
class CSEStudent(Student):

    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE student is crying because of ", self.no_of_labs, "labs")

#============================================

class CSEFresher(CSEStudent):

    def enroll_CSE110(self):
        print("Enroll in CSE110")

#============================================

s1 = CSEStudent("Bob", 11, 3)
s2 = CSEFresher("Carol", 25, 5)
s2.details()
s1.details()
s1.cry()
s1.enroll_CSE110()
