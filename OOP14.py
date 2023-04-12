class Student:

    uni_name= "BracU"

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id


    def details(self):   #instance method
        print("Name:", self.name, "ID", self.__Id, Student.uni_name)


    #def update_uni_name(self, u_name):
        #self.uni_name = u_name (will not work because self will call its own instance)    @classmethod
    def update_uni_name(cls, u_name):
        cls.uni_name = u_name


    #=============================================
s1 = Student("Bob", 22)
s2 = Student("Carol", 55)
s1.details()
s2.details()
Student.update_uni_name("Brac University")
s1.details()
s2.details()
