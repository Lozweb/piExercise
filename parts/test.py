import RPi.GPIO as GPIO
from manette import Manette
from servo_sg90 import Sg90
import time


debug = True
manette = Manette(0)
servo = Sg90(90, 12)


def setup():
    servo.PI_PORT.start(0)
    servo.servo_write(servo.SERVO_DEFAULT_POS)


def destroy():
    servo.PI_PORT.stop()
    manette.controler.close()
    GPIO.cleanup()


def log(ly_pos, servo_current_pos, target):
    if debug:
        print("ly pos: {0} - servo pos: {1} - target : {2}"
              .format(ly_pos, servo_current_pos, target))


if __name__ == '__main__':
    print('Program is starting ... ')
    setup()
    try:

        while True:
            manette.controler.axis_l.when_moved = manette.on_axis_l_moved
            target_pos = servo.current_pos + round(manette.ly_pos)
            servo.servo_write(target_pos)
            log(manette.ly_pos, servo.current_pos, target_pos)
            time.sleep(0.01)

    except KeyboardInterrupt:
        destroy()



