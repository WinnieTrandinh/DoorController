from Card import Card

#this class handless the verification of the cards
class Reader:
    
    #set to store all valid cards
    cards = set()
    
    #called during creation; adds all valid cards into local set
    def __init__(self, IDs):
        for ID in IDs:
            card = Card(ID)
            self.cards.add(card)

    #checks if given ID matches ID of any valid cards
    def isValid(self, ID):
        for card in self.cards:
            if (str(card.getID()) == str(ID)):
                return True
        return False
    
    #returns list of valid cards
    def getCards(self):
        return self.cards

        
    
        