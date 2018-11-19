from Card import Card

class Reader:
    
    cards = set()
    
    def __init__(self, IDs):
        for ID in IDs:
            card = Card(ID)
            self.cards.add(card)

    def isValid(self, ID):
        for card in self.cards:
            #print(str(card.getID()) + ", " + str(ID))
            if (str(card.getID()) == str(ID)):
                return True
        return False
    
    def getCards(self):
        return self.cards

        
    
        