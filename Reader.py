from Card import Card

class Reader:
    
    cards: set = set()
    
    def __init__(self, IDs):
        for ID in IDs:
            card = Card(ID)
            self.cards.add(card)

    def isValid(self, ID):
        for card in self.cards:
            #print(str(card.getID()) + ", " + str(ID))
            if (float(card.getID()) == float(ID)):
                return True
        return False
    
    def getCards(self):
        return self.cards

#print(createValidCards([1111, 2222]))
#create cards
#wait for input
#check if valid
        
    
        