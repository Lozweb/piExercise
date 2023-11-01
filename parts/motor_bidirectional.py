import RPi.GPIO as GPIO
import time
from manette import Manette

# define the pins connected to L293D
Motor1A = 24
Motor1B = 23
Motor1E = 25
manette = Manette(0)

def setup():
    global p
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)  # set pins to OUTPUT mode
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)


# mapNUM function: map the value from a range of mapping to another range.
def mapNUM(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow


# motor function: determine the direction and speed of the motor according to the input ADC value input
def motor(direction, trig_pos):

    value = (round(trig_pos*100))

    print(value)

    if direction == "forward":
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)
        print('Turn Forward...')

    elif direction == "backward":
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


def loop():

    while True:

        manette.controler.button_trigger_r.when_released = manette.on_button_trigger_r_released
        manette.controler.trigger_r.when_moved = manette.on_trigger_rt_moved
        direction = manette.direction
        acceleration = manette.trig_rt_pos
        print("direction : {0} acceleration : {1}".format(direction, acceleration))
        motor(direction, acceleration)

        time.sleep(0.2)


def destroy():
    manette.controler.close()
    GPIO.cleanup()


if __name__ == '__main__':  # Program entrance
    print('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
