import RPi.GPIO as GPIO


class Led:

    def __init__(self, pin):
        self.LED_PIN = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN, GPIO.OUT)

    def on(self):
        GPIO.output(self.LED_PIN, GPIO.HIGH)

    def off(self):
        GPIO.output(self.LED_PIN, GPIO.LOW)



