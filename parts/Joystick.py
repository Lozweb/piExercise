import RPi.GPIO as GPIO
import time
from ADCDevice import *

Z_Pin = 12
adc = ADCDevice()


def setup():
    global adc
    if adc.detect_i2_c(0x48):
        adc = PCF8591()
    elif adc.detect_i2_c(0x4b):
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
              "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
              "Program Exit. \n");
        exit(-1)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Z_Pin, GPIO.IN, GPIO.PUD_UP)


def loop():
    while True:
        val_Z = GPIO.input(Z_Pin)
        val_Y = adc.analog_read(0)
        val_X = adc.analog_read(1)
        print('value_X: %d ,\tvlue_Y: %d ,\tvalue_Z: %d' % (val_X, val_Y, val_Z))
        time.sleep(0.01)


def destroy():
    adc.close()
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting ... ')  # Program entrance
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
