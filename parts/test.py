import RPi.GPIO as GPIO
import time
from ADCDevice import *

# pin 11 = GPIO17
# pin 12 = GPIO18

joy_pin = 12
servo_pin = 11
converter = ADCDevice()
OFFSET_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSET_DUTY
SERVO_MAX_DUTY = 12.5 + OFFSET_DUTY


def setup():
    global adc
    global p
    adc = ADS7830()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(joy_pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.output(servo_pin, GPIO.LOW)
    p = GPIO.PWM(servo_pin, 50)
    p.start(0)


def destroy():
    p.stop()
    adc.close()
    GPIO.cleanup()


def map(value, from_low, from_high, to_low, to_high):
    return (to_high - to_low) * (value - from_low) / (from_high - from_low) + to_low


def servo_write(angle):
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    p.ChangeDutyCycle(map(angle, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))


if __name__ == '__main__':
    print('Program is starting ... ')
    setup()
    try:

        while True:
            val_Z = GPIO.input(joy_pin)
            val_Y = adc.get_y()
            val_X = adc.get_x()

            print("x:" + val_X + " y: " + val_Y)

            # servo_write(val_X*0.70)

            time.sleep(0.01)

    except KeyboardInterrupt:
        destroy()