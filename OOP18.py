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
class BBAStudents(Student):

    #def __init__(self, name, Id):

    def party(self):
        print("All day party WOOHOO")

#============================================

s1 = CSEStudent("Jhandaya", 11, 3)
s2 = BBAStudents("Tammy", 36)
s1.details()
s2.details()
s1.cry()
s2.party()
print(help(s2))