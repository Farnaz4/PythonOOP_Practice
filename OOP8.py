#Operator Overloading (VIDEO 15)
class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house has", self.window, "window(s) and", self.door, "door(s)")

    def __add__(self, other):
        new_window =self.window + other.window
        new_door = self.door + other.door
        obj = House(new_window, new_door)
        return obj
        #return "The house has", self.window, "window(s) and", self.door, "door(s)"
#==================================================

h1 = House(10,2 )
h2 = House(108, 5)
h1.view()
h2.view()
h3 = h1 + h2
h3.view()
#print(str1+str2)
