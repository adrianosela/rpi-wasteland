import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

x = 0.25
times = 5
turn = 0

while (turn < times ):
    GPIO.output(5, GPIO.HIGH)
    
    time.sleep(x)

    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)

    time.sleep(x)
    
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

    time.sleep(x)

    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    
    time.sleep(x)
    
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)

    time.sleep(x)
    
    GPIO.output(26, GPIO.LOW)
    turn = turn +1 

GPIO.cleanup()


