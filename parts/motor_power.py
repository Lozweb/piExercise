from time import sleep
import RPi.GPIO as GPIO

# Modifiez pour mettre les pins sur lesquels sont branchés les entrées de la L293D
MOTOR1_EN = 12
MOTOR1_A = 16
MOTOR1_B = 18


try:

    # Configure les pins
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    # AVANCE

    # Fais avancer le robot en faisant tourner les deux moteurs du même sens
    print("1en high 1a high 1b high")
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    # Continu d'avancer pendant une seconde
    sleep(1)

    # Stoppe et freine les moteurs pendant une seconde
    print("1en low 1a high 1b high")
    GPIO.output(MOTOR1_EN, GPIO.LOW)
    sleep(1)

    # TOURNE A GAUCHE

    # Fais tourner le robot à gauche  en faisant tourner les deux moteurs à sens opposé
    print("1en high 1a low 1b high")
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    sleep(0.5)

    # Stoppe et freine les moteurs pendant une seconde
    print("1en low 1a high 1b high")
    GPIO.output(MOTOR1_EN, GPIO.LOW)

    # On stoppe après une seconde
    sleep(1)

    GPIO.output(MOTOR1_EN, GPIO.LOW)

except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
    raise

GPIO.cleanup()