class Motor:
    import RPi.GPIO as GPIO
    
    pins: tuple
    
    def __init__(self, enable, input1, input2):
        GPIO.setMode(GPIO.BOARD)
        self.pins = (enable, input1, input2)
        for pin in pins:
            GPIO.setup(pin, GPIO.out)
        
    def run(self, forward):
        if forward:
            GPIO.output(pins[1], GPIO.LOW)
            GPIO.output(pins[2], GPIO.HIGH)
            GPIO.output(pins[0], GPIO.HIGH)
        else:
            GPIO.output(pins[1], GPIO.HIGH)
            GPIO.output(pins[2], GPIO.LOW)
            GPIO.output(pins[0], GPIO.HIGH)

    def stop(self):
        GPIO.output(pins[0], GPIO.LOW)