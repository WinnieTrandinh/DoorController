from Reader import Reader
from Motor import Motor
import threading
import time

def createValidIDs():
    #add more IDs if necessary
    IDs = set()
    IDs.add(123456789)
    IDs.add(234567890)

    reader_ = Reader(IDs)

    for card in reader_.getCards():
        print(card.getID())
        
    return reader_

def checkInput(input):
    return reader.isValid(input)


reader = createValidIDs()
print (checkInput(input() ) )

state = 0
#create reboot thread
#while state != -1:
#    if (checkInput(input() ) ):
        