# DoorController
Reads data from USB RFID reader and compares against valid card IDs.
If valid, activates a mechanism to turn open the door handle.
Runs on Raspberry Pi Zero.

12V DC motor controller by L293D Driver.
Setup:
  Pin 1 -> Pi GPIO 12
  Pin 2 -> Pi GPIO 11
  Pin 3 -> Motor Terminal
  Pin 4 -> Pi Ground
  Pin 5 -> Pi Ground
  Pin 6 -> Motor Terminal
  Pin 7 -> Pi GPIO 13
  Pin 8 -> 12V Battery Terminal
  Pin 9 -> Empty
  Pin 10 -> Empty
  Pin 11 -> Empty
  Pin 12 -> Pi Ground
  Pin 13 -> Pi Ground
  Pin 14 -> Empty
  Pin 15 -> Empty
  Pin 16 -> Pi 5V
  
Pi Setup for Automatic Run on Startup:
  Add @lxterminal to /home/pi/.config/lxsession/LXDE-pi/autostart
  Add sudo python3 /'filePath'/DoorController/Main.py to /home/pi/.bashrc

Images of mechanism found in Fabrication folder.
