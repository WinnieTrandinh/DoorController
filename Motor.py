import RPi.GPIO as GPIO

class Motor:
    
    pins = tuple()
    
    def __init__(self, enable, input1, input2):
        GPIO.setmode(GPIO.BOARD)
        self.pins = (enable, input1, input2)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        
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

    def stop(self):
        GPIO.output(self.pins[0], GPIO.LOW)
        
    def cleanup(self):
        self.stop()
        GPIO.cleanup()