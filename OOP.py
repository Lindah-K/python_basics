class Cars:
    # constructor
    def __init__(self, type, color,model):
        self.type = type
        self.color = color
        self.model = model

    # method
    def onyesha(self):
        print(f"I love {self.model} cars which is a {self.type} being {self.color} in color")

# creating an object
myobj = Cars("Saloon", "white", "toyota")
myobj.onyesha()
myobj2 = Cars("S.Wagon", "Black", "Benz")
myobj2.onyesha()