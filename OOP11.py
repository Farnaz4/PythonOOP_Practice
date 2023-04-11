# class ABC:
#     def __init__(self, x, y):
#         self.x = x
#         self.__y = y
#     def details(self):
#         print("X", self.x, "Y", self.__y)


class Student:
    def __init__(self, name, Id):
        self.name = name
        self.__id = Id
    def details(self):
        print("Name:", self.name, "ID:", self.__id)
        self.__method()

    def __method(self):
        print("private method executed")

#=====================================
s1 = Student("Bob", 11)
s2 = Student("Carol", 21)

#s1.__method()
s1.details()