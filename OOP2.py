class House:
    def __init__(self):
        self.window = 4  #instance variable
        self. door = 2

    def view(self):
        print(self.window, "windows", self.door, "doors")

#==============================================================

h1 = House()
h2 = House()

h2.window = 6
h1.door = 3
h1.view()
h2.view()
