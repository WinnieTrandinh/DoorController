from Reader import Reader
from Motor import Motor
import threading
import time
import os

def createValidIDs():
    #add more IDs if necessary
    IDs = set()
    IDs.add("062301632603431110")
    IDs.add("123456789")

    reader_ = Reader(IDs)

    for card in reader_.getCards():
        print(card.getID())
        
    return reader_

def checkInput(input):
    return reader.isValid(input)

def openDoor(motor_):
    print("running forward")
    motor_.run(True)
    time.sleep(3)
    print("stopping")
    motor_.stop()
    time.sleep(5)
    print("running backwards")
    motor_.run(False)
    time.sleep(3)
    print("stopping")
    motor_.stop()

def reboot():
    motor.cleanup()
    time.sleep(1)
    print("reboot")
    os.system("sudo reboot")
    #change

#reboots pi daily
    #86400 seconds
t = threading.Timer(86400, reboot)
t.start()


reader = createValidIDs()
#print (checkInput(input() ) )
motor = Motor(15, 11, 16)

try:
    while True:
        if (checkInput(input() ) ):
            openDoor(motor)
except KeyboardInterrupt:
    print("keyboard interrupt")
    motor.cleanup()
