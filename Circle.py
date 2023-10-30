class Circle:
    def __init__(self):
        self.posX = None
        self.posY = None
        

    def setPos(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def print(self):
        return "olá"
    
    def getPos(self):
        return (self.posX, self.posY)