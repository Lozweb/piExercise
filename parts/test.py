import servo_moteur as sm

if __name__ == '__main__':
    print('Program is starting...')
    sm.setup()
try:

    while True:

        angle = input("Entrez l'angle")
        sm.servo_write(int(angle))


except KeyboardInterrupt:
    sm.destroy()