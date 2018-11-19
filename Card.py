class Card:

    ID = -1
    
    def __init__(self, cardID):
        self.ID = cardID
        
    def getID(self):
        return self.ID