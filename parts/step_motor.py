import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22)  # define pins connected to four phase ABCD of stepper motor
CCWStep = (0x01, 0x02, 0x04, 0x08)  # define power supply order for rotating anticlockwise
CWStep = (0x08, 0x04, 0x02, 0x01)  # define power supply order for rotating clockwise


def setup():
    GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)


def move_one_period(direction, ms):

    for j in range(0, 4, 1):  # cycle for power supply order

        for i in range(0, 4, 1):  # assign to each pin

            if direction == 1:
                GPIO.output(motorPins[i], ((CCWStep[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))

            else:
                GPIO.output(motorPins[i], ((CWStep[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))

        if ms < 3:
            ms = 3

        time.sleep(ms * 0.001)


def move_steps(direction, ms, steps):
    for i in range(steps):
        move_one_period(direction, ms)


def motor_stop():
    for i in range(0, 4, 1):
        GPIO.output(motorPins[i], GPIO.LOW)


def loop():
    while True:
        # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
        move_steps(1, 3, 512)
        time.sleep(0.5)
        # rotating 360 deg anticlockwise
        move_steps(0, 3, 512)
        time.sleep(0.5)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


