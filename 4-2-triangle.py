import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

a = int(input())
a = a/255
try:
    while True:
        for i in range(255):
            GPIO.output(dac, dec2bin(i))
            time.sleep(a)
        for i in range(255, -1, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(a)
            

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup() 