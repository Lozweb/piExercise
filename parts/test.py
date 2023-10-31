import RPi.GPIO as GPIO
from manette import Manette
from servo_sg90 import Sg90
import time


manette = Manette(0)
servo = Sg90(90, 12)


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
            manette.controler.axis_l.when_moved = manette.on_axis_l_moved
            manette.controler.axis_r.when_moved = manette.on_axis_l_moved
            target_pos = round(manette.current_ly_pos + 5)
            print(manette.current_ly_pos)
            print(target_pos)
            servo.servo_write(target_pos)
            time.sleep(0.001)

    except KeyboardInterrupt:
        destroy()