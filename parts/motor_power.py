from time import sleep
import RPi.GPIO as GPIO

# Modifiez pour mettre les pins sur lesquels sont branchés les entrées de la L293D
Motor1E = 22
Motor1A = 18
Motor1B = 16


try:

    # Configure les pins
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)

    # AVANCE
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    print("forward")
    sleep(5)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    print("backward")
    sleep(5)

except KeyboardInterrupt:
    pass

except:
    GPIO.cleanup()
    raise

GPIO.cleanup()