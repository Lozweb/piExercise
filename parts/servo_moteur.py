import RPi.GPIO as GPIO
import time

OFFSET_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSET_DUTY
SERVO_MAX_DUTY = 12.5 + OFFSET_DUTY
servo_pin = 12


def map(value, from_low, from_high, to_low, to_high):
    return (to_high - to_low) * (value - from_low) / (from_high - from_low) + to_low


def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.output(servo_pin, GPIO.LOW)
    p = GPIO.PWM(servo_pin, 50)
    p.start(0)


def servo_write(angle):
    if angle<0:
        angle = 0
    elif angle > 180:
        angle = 180
    p.ChangeDutyCycle(map(angle, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))


def loop():
    while True:
        for dc in range(0, 181, 1):
            servo_write(dc)
            time.sleep(0.001)
            time.sleep(0.5)
        for dc in range(180, -1, -1):
            servo_write(dc)
            time.sleep(0.001)
            time.sleep(0.5)


def destroy():
    p.stop()
    GPIO.cleanup()

    if __name__ == '__main__':
        print ('Program is starting...')
        setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()