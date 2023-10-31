import RPi.GPIO as GPIO
import time

relayPin = 11  # define the relayPin
buttonPin = 12  # define the buttonPin
debounceTime = 50


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin, GPIO.OUT)  # set relayPin to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN)  # set buttonPin to INTPUT mode


def loop():
    relay_state = False
    last_change_time = round(time.time() * 1000)
    button_state = GPIO.HIGH
    last_button_state = GPIO.HIGH
    reading = GPIO.HIGH
    while True:
        reading = GPIO.input(buttonPin)
        if reading != last_button_state:
            last_change_time = round(time.time() * 1000)
        if (round(time.time() * 1000) - last_change_time) > debounceTime:
            if reading != button_state:
                button_state = reading
                if button_state == GPIO.LOW:
                    print("Button is pressed!")
                    relay_state = not relay_state
                    if relay_state:
                        print("Turn on relay ...")
                    else:
                        print("Turn off relay ... ")
                else:
                    print("Button is released!")
        GPIO.output(relayPin, relay_state)
        last_button_state = reading  # lastButtonState store latest state


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':  # Program entrance
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

