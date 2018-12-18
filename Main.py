#Door Controller Program
#Author: Winnie Trandinh
#Last Modified: December 18, 2018
#This program scans RFID cards and checks if they are valid.
#If valid, it controls a motor that would open a door handle.
#For setup instructions, see README.md.

from Reader import Reader
from Motor import Motor
import threading
import time
import os

#creates the list of valid card IDs
def createValidIDs():
    #add more IDs if necessary
    IDs = set()
    IDs.add("062301632603431110")

    reader_ = Reader(IDs)
        
    return reader_

#called whenever a new card is scanned
#tests and returns true if card is valid
def checkInput(input):
    return reader.isValid(input)

#method responsible for opening the door
def openDoor(motor_):
    print("running forward")
    motor_.run(True)
    time.sleep(1.5)
    print("stopping")
    motor_.stop()
    time.sleep(10)
    print("running backwards")
    motor_.run(False)
    time.sleep(1.5)
    print("stopping")
    motor_.stop()

#called whenever a system reboot is necessary
def reboot():
    motor.cleanup()
    time.sleep(1)
    print("reboot")
    os.system("sudo reboot")

#reboots pi daily to remove cache
    #86400 seconds
#starts a new timer thread that activates daily
t = threading.Timer(86400, reboot)
t.start()

#sets up reader and motor classes
reader = createValidIDs()
motor = Motor(12, 11, 13)

#continuous loop to check for new inputs
try:
    while True:
        if (checkInput(input() ) ):
            print("card validated")
            openDoor(motor)
except KeyboardInterrupt:
    #interrupted with ctrl+c
    print("keyboard interrupt")
    motor.cleanup()
