import RPi.GPIO as GPIO
from parts.servo_sg90 import Sg90
import time

servo = Sg90(90, 17, 105, 78)


def setup():
    servo.PI_PORT.start(0)
    servo.move_to(servo.SERVO_DEFAULT_POS)


def destroy():
    servo.PI_PORT.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting ... ')
    setup()
    try:

        while True:
            print("input target")
            angle = input()
            servo.move_to(int(angle))


    except KeyboardInterrupt:
        destroy()