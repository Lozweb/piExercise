import RPi.GPIO as GPIO
from parts.servo_sg90 import Sg90
import time

servo = Sg90(90, 17)


def setup():
    servo.PI_PORT.start(0)
    servo.servo_write(servo.SERVO_DEFAULT_POS)


def destroy():
    servo.PI_PORT.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting ... ')
    setup()
    try:

        while True:
            print("target 90°")
            servo.servo_write(90)
            time.sleep(5)

            print("target 0°")
            servo.servo_write(0)
            time.sleep(5)

            print("target 180")
            servo.servo_write(100)
            time.sleep(5)

    except KeyboardInterrupt:
        destroy()