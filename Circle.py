class Circle:
    def __init__(self, name):
        self.posX = None
        self.posY = None
        self.name = name
        

    def setPos(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def print(self):
        return "olá"
    
    def getPos(self):
        return (self.posX, self.posY)
    
    def getName(self):
        return self.name
    
    def getPosName(self, posY):
        return (self.posX, self.posY + posY)