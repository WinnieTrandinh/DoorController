import RPi.GPIO as GPIO
import time

#this class controls the movement of the attached motor
class Motor:
    
    #variables for storing pin numbers of motor
    pins = tuple()
    
    #called during creation, sets up specified pins
    def __init__(self, enable, input1, input2):
        GPIO.setmode(GPIO.BOARD)
        self.pins = (enable, input1, input2)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        
    #spins the motor, direction specified through "forward" boolean
    def run(self, forward):
        pins = self.pins
        if forward:
            GPIO.output(pins[1], GPIO.LOW)
            GPIO.output(pins[2], GPIO.HIGH)
            GPIO.output(pins[0], GPIO.HIGH)
        else:
            GPIO.output(pins[1], GPIO.HIGH)
            GPIO.output(pins[2], GPIO.LOW)
            GPIO.output(pins[0], GPIO.HIGH)

    #halts motor movement
    def stop(self):
        GPIO.output(self.pins[0], GPIO.LOW)
        
    #called before ending program, resets all used pins for future use
    def cleanup(self):
        self.stop()
        GPIO.cleanup()
        