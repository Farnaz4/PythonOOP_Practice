class Student:
    uni_name = "Bracu"

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):
        print("Name:", self.name, "ID:", self.__id, Student.uni_name)


    @classmethod
    def update_uni_name(cls, u_name):
        cls.uni_name = u_name

    @classmethod
    def from_string(cls, info):
        name, Id = info.split('-')
        obj = cls(name,Id)
        return obj


#=======================================

s1 = Student("Bob", 11)
s2 = Student.from_string("Carol-47")
s1.details()
s2.details()



