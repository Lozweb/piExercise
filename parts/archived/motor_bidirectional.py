import RPi.GPIO as GPIO
import time
from manette import Manette
from servo_sg90 import Sg90

# define the pins connected to L293D

debug = True
Motor1A = 24
Motor1B = 23
Motor1E = 25
servo = Sg90(80, 17)
manette = Manette(0)


def setup():
    global p
    servo.PI_PORT.start(0)
    servo.servo_write(servo.SERVO_DEFAULT_POS)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)  # set pins to OUTPUT mode
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)


# mapNUM function: map the value from a range of mapping to another range.
def mapNUM(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow


# motor function: determine the direction and speed of the motor according to the input ADC value input
def motor(direction, trig_pos):
    tpos = 0

    if 0.3 > trig_pos > 0:
        tpos = 0
    elif -0.3 < trig_pos < 0:
        tpos = 0
    else:
        tpos = trig_pos

    value = (round(tpos * 100))

    print(value)

    if direction == "forward" and value > 0:
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)
        print('Turn Forward...')

    elif direction == "backward" and value > 0:
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor1E, GPIO.HIGH)
        print('Turn Backward...')

    elif value == 0:
        GPIO.output(Motor1E, GPIO.LOW)
        print('Motor Stop...')

    else:
        GPIO.output(Motor1E, GPIO.LOW)
        print('Motor Stop...')


def change_direction(current_direction):
    if current_direction == "forward":
        return "backward"
    else:
        return "forward"


def log(ly_pos, servo_current_pos, target, direction, acceleration):
    if debug:
        print("ly pos: {0} - servo pos: {1} - target : {2}"
              .format(ly_pos, servo_current_pos, target))

        # print("direction : {0} acceleration : {1}".format(direction, acceleration))


def loop():
    while True:
        manette.controler.button_trigger_r.when_released = manette.on_button_trigger_r_released
        manette.controler.trigger_r.when_moved = manette.on_trigger_rt_moved
        direction = manette.direction
        acceleration = manette.trig_rt_pos

        motor(direction, acceleration)

        manette.controler.axis_l.when_moved = manette.on_axis_l_moved
        target_pos = servo.current_pos + round(manette.ly_pos)

        servo.servo_write(target_pos)

        log(manette.ly_pos, servo.current_pos, target_pos, direction, acceleration)

        time.sleep(0.01)


def destroy():
    servo.PI_PORT.stop()
    manette.controler.close()
    GPIO.cleanup()


if __name__ == '__main__':  # Program entrance
    print('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
