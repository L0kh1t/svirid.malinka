import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#инициализируем
levels = 2**8
maxVoltage = 3.3
troyka = 13
leds = [2,3,4,17,27,22,10,9]
comp = 14
dac = [8,11,7,1,0,5,12,6]

#задаём все выходы/входы
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=1)

#функция перевода в двоичное число
def b(n):
    return [int(i) for i in bin(int(n))[2:].zfill(8)]

#функция снятия напряжения на конденсаторе
def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        voltage = value/levels*maxVoltage
        signal = b(value)
        GPIO.output(dac, signal)
        time.sleep(0.007)
        if GPIO.input(comp) == 1:
            value -= 2**i
    print(voltage)
    return value
    

try:
    times = []
    volt = []
    max = 207
    n = 0
    t1 = time.time()
    #ищем время и напряжение
    while n != max:
        t = time.time()
        times.append(t-t1)
        n = adc()
        volt.append(n)
        print(n)
        znach = b(n)
        GPIO.output(leds, znach)
    measured_data_str = [str(item) for item in volt]
    print(measured_data_str)
    
    #записываем всё в файлики
    with open('data.txt', 'w') as outfile:
        outfile.write("\n".join(measured_data_str))
    step = 3.3/2**8
    nu = len(volt)/(times[-1])
    toprint = [step, nu]
    measured_data_str = [str(item) for item in toprint]
    with open('settings1.txt', 'w') as outfile:
        outfile.write("\n".join(measured_data_str))
finally:
    #строим графики
    plt.plot(times, volt, color='r')
    plt.show()
    print('время измерения', times[-1])
    print('частота', times[-1]/len(volt))
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()
