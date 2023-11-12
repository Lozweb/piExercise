import time
import RPi.GPIO as GPIO
from parts.servo_sg90 import Sg90
from parts.manette import Manette
from parts.motor import Motor
from parts.led import Led

servo = Sg90(90, 12, 105, 78)
motor = Motor(24, 23, 25)
manette = Manette(0)
stopLight = Led(18)
phare = Led


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

            manette.controler.button_x.when_released = manette.on_button_x_release
            manette.controler.trigger_r.when_moved = manette.on_trigger_rt_moved

            direction = manette.direction
            acceleration = manette.trig_rt_pos
            motor.set_motor(direction, acceleration)

            if manette.lx_pos < 0:
                print("turn left")
                servo.move_to("left")

            elif manette.lx_pos > 0:
                print("turn right")
                servo.move_to("right")

            else:
                servo.move_to("straight")

            if not motor.isRunning:
                stopLight.on()
            else:
                stopLight.off()

            time.sleep(0.1)

    except KeyboardInterrupt:
        destroy()
