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
    
    GPIO.output(M3A, GPIO.HIGH)
    GPIO.output(M3B, GPIO.LOW)
    GPIO.output(M3, GPIO.HIGH)
    
    GPIO.output(M4A, GPIO.HIGH)
    GPIO.output(M4B, GPIO.LOW)
    GPIO.output(M4, GPIO.HIGH)

def pireverse():
    print "Reverse"
    GPIO.output(M1A, GPIO.LOW)
    GPIO.output(M1B, GPIO.HIGH)
    GPIO.output(M1, GPIO.HIGH)

    GPIO.output(M2A, GPIO.LOW)
    GPIO.output(M2B, GPIO.HIGH)
    GPIO.output(M2, GPIO.HIGH)
    
    GPIO.output(M3A, GPIO.HIGH)
    GPIO.output(M3B, GPIO.LOW)
    GPIO.output(M3, GPIO.HIGH)
    
    GPIO.output(M4A, GPIO.HIGH)
    GPIO.output(M4B, GPIO.LOW)
    GPIO.output(M4, GPIO.HIGH)

def pileft():
    print "Left"
    GPIO.output(M1A, GPIO.LOW)
    GPIO.output(M1B, GPIO.HIGH)
    GPIO.output(M1, GPIO.HIGH)

    GPIO.output(M2A, GPIO.LOW)
    GPIO.output(M2B, GPIO.HIGH)
    GPIO.output(M2, GPIO.HIGH)

def piright():
    print "Right"
    GPIO.output(M3A, GPIO.HIGH)
    GPIO.output(M3B, GPIO.LOW)
    GPIO.output(M3, GPIO.HIGH)
    
    GPIO.output(M4A, GPIO.HIGH)
    GPIO.output(M4B, GPIO.LOW)
    GPIO.output(M4, GPIO.HIGH)

GPIO.setmode(GPIO.BOARD)

#Motor1
M1 = 40
M1A = 36
M1B = 38
#Motor2
M2 = 37
M2A = 33
M2B = 35
#Motor3
M3 = 11
M3A = 13
M3B = 15
#Motor4
M4 = 22
M4A = 16
M4B = 18

#Motor1
GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)
#Motor2
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M2A, GPIO.OUT)
GPIO.setup(M2B, GPIO.OUT)
#Motor3
GPIO.setup(M3, GPIO.OUT)
GPIO.setup(M3A, GPIO.OUT)
GPIO.setup(M3B, GPIO.OUT)
#Motor4
GPIO.setup(M4, GPIO.OUT)
GPIO.setup(M4A, GPIO.OUT)
GPIO.setup(M4B, GPIO.OUT)

while(1):
    operation = raw_input()
    if operation == 'w':
        piforward()
    elif operation == 'a':
        pileft()
    elif operation == 's':
        pireverse()
    elif operation == 'd':
        piright()
    elif operation == 'q':
        break
    else:
        print "Nothing"

GPIO.cleanup()