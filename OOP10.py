class Student:
    def __init__(self, name, Id):
        self.name = name
        self.__id = Id
    def details(self):
        print("Name:", self.name, "ID:", self.__id)

    def set__ID(self,Id):
        if (Id>0):
            self.__id = Id
        else:
            print("Invalid ID, enter id again")

    def get_ID(self):
        return self.__id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s2.set__ID(55)
s2.set__ID(6)
s1.details()
s2.details()