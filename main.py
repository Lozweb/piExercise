import time

import RPi.GPIO as GPIO
from parts.servo_sg90 import Sg90
from parts.manette import Manette

servo = Sg90(90, 17, 105, 78)
manette = Manette(0)


def setup():
    servo.PI_PORT.start(0)
    servo.set_angle(servo.SERVO_DEFAULT_POS)


def destroy():
    servo.PI_PORT.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting ... ')
    setup()
    try:

        while True:

            manette.controler.axis_l.when_moved = manette.on_axis_l_moved

            if manette.ly_pos < 0:
                servo.move_to("left")

            elif manette.ly_pos > 0:
                servo.move_to("right")

            else:
                servo.move_to("straight")

            time.sleep(0.1)

    except KeyboardInterrupt:
        destroy()