#Encapsulation
class Student:
    def __init__(self, name, Id):
        self.name = name
        # self.id = Id #normal instance variable
        self.__id = Id #private instance variable

    def details(self):
        print("Name:", self.name, "ID", self.__id)

    def update_ID(self, Id):
        if(Id>0):
            self.__id = Id
        else:
            print("Invalid ID, REEntr")



#====================================================

s1 = Student("Carol", 33)
s2 = Student("bob", 11)

# s1.__id = -6666
# # print(s1.__id)

s1.update_ID(-66)

s1.details()
s2.details()
