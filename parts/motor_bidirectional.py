import RPi.GPIO as GPIO
import time
from manette import Manette

# define the pins connected to L293D
motoRPin1 = 13
motoRPin2 = 11
enablePin = 15
manette = Manette(0)

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motoRPin1, GPIO.OUT)  # set pins to OUTPUT mode
    GPIO.setup(motoRPin2, GPIO.OUT)
    GPIO.setup(enablePin, GPIO.OUT)
    p = GPIO.PWM(enablePin, 1000)  # creat PWM and set Frequence to 1KHz
    p.start(0)


# mapNUM function: map the value from a range of mapping to another range.
def mapNUM(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow


# motor function: determine the direction and speed of the motor according to the input ADC value input
def motor(direction, trig_pos):
    value = ((trig_pos*100) - 128)
    print(value)

    if direction == "forward":
        GPIO.output(motoRPin1, GPIO.HIGH)
        GPIO.output(motoRPin2, GPIO.LOW)
        print('Turn Forward...')

    elif direction == "backward":
        GPIO.output(motoRPin1, GPIO.LOW)
        GPIO.output(motoRPin2, GPIO.HIGH)
        print('Turn Backward...')

    else:
        GPIO.output(motoRPin1, GPIO.LOW)
        GPIO.output(motoRPin2, GPIO.LOW)
        print('Motor Stop...')

    p.start(mapNUM(abs(value), 0, 128, 0, 100))
    print('The PWM duty cycle is %d%%\n' % (abs(value) * 100 / 127))  # print PMW duty cycle.


def loop():

    global current_direction
    current_direction = "forward"

    while True:

        manette.controler.button_trigger_r.when_pressed = manette.on_trigger_l_pressed

        if manette.trig_r_press:
            if current_direction == "forward":
                current_direction = "backward"
            else:
                current_direction = "forward"

        manette.trig_l_press = False

        manette.controler.trigger_r.when_moved = manette.on_trigger_rt_moved

        acceleration = round(manette.trig_rt_pos)

        print("direction : {0} acceleration : {1}".format(current_direction, acceleration))

        motor(current_direction, acceleration)

        time.sleep(0.2)


def destroy():
    p.stop()  # stop PWM
    manette.controler.close()
    GPIO.cleanup()


if __name__ == '__main__':  # Program entrance
    print('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
