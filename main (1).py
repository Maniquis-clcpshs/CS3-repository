class glassware:
    def __init__(self, material):
        self.material = material
    
class beaker(glassware):
    def __init__(self,material, mL):
        super().__init__(material)
        self.mL = mL
    
class Tray:
    def __init__(self):
        self.beakers = [
        beaker("Borosilicate glass",500),
        beaker("Borosilicate glass",400),
        beaker("Borosilicate glass",300),
        beaker("Borosilicate glass",200),
        beaker("Borosilicate glass",100)
        ]

    def printbeakers(self):
        for i in self.beakers:
            print(i.material,i.mL)
tray= Tray()
tray.printbeakers()

del tray
print("The tray is deleted, the beakers have been lost")