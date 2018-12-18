#this class holds information about the valid RFID cards
class Card:

    ID = -1
    
    #called during creation; sets ID of the card
    def __init__(self, cardID):
        self.ID = cardID
    
    #returns the ID of the card
    def getID(self):
        return self.ID