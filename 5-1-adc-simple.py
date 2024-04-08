import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
levels = 2**8
maxVoltage = 3.3
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def b(n):
    return [int(i) for i in bin(int(n))[2:].zfill(8)]

def adc():
    for value in range(256):

        signal = b(value)
        voltage = value/levels*maxVoltage
        GPIO.output(dac, signal)
        time.sleep(0.0007)
        if GPIO.input(comp) == 1:
            print('value', value, 'signal', signal, 'voltage', voltage)
            return value
            break
    
try:
    while True:
        n = adc()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

