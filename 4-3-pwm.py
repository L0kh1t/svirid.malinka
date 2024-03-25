import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(dac, GPIO.OUT)

def binv(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def volt(X):
    return 3.3*X/255
try:
    while True: 
        a = input()
        if a == 'q':
            break
        a = int(a)
        if a > 255:
            print('много')
            break
        GPIO.output(dac, binv(a))
        print(volt(a))
except  ValueError:
    print('это не целое число')
except TypeError:
    print('это НЕ ЦЕЛОЕ ЧИСЛО!')
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()