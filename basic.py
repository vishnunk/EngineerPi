import RPi.GPIO as GPIO
from time import sleep

def piforward():
    print "Moving forward"
    GPIO.output(M1A, GPIO.HIGH)
    GPIO.output(M1B, GPIO.LOW)
    GPIO.output(M1, GPIO.HIGH)

    GPIO.output(M2A, GPIO.HIGH)
    GPIO.output(M2B, GPIO.LOW)
    GPIO.output(M2, GPIO.HIGH)

def pireverse():
    print "Reverse"
    GPIO.output(M1A, GPIO.LOW)
    GPIO.output(M1B, GPIO.HIGH)
    GPIO.output(M1, GPIO.HIGH)

    GPIO.output(M2A, GPIO.LOW)
    GPIO.output(M2B, GPIO.HIGH)
    GPIO.output(M2, GPIO.HIGH)


GPIO.setmode(GPIO.BOARD)

M1A = 36
M1B = 38
M1 = 40
M2A = 33
M2B = 35
M2 = 37

GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)
GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2A, GPIO.OUT)
GPIO.setup(M2B, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)

while(1):
    operation = raw_input()
    if operation == 'w':
        piforward()
    elif operation == 's':
        pireverse()
    elif operation == 'q':
        break
    else:
        print "Nothing"

GPIO.cleanup()
