class Engine:
    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")

#================================================

class Car:
    def __init__(self, name, cc):
        self.name = name
        self.engine = Engine(cc) #created an object of a class inside a class

    def run(self):
        print(self.engine)
        self.engine.start()
        print("Car is running")

#=================================================

c1 = Car("BMW", 2000)
c1.run()


#e1 = Engine(2000) basically this