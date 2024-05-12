import matplotlib.pyplot as plt
import numpy as np

data_array = np.loadtxt('data.txt', dtype=int)
settings = np.loadtxt('settings1.txt', dtype=float)
v = settings[0]
nu = settings[1]

data_array = np.array(data_array*v)
time_array = np.array([i/nu for i in range(len(data_array))])
maxt = "время заряда = " + f'{max(time_array):.2f}' + 'c'

fig, ax = plt.subplots(figsize=(20, 10), dpi=100)
ax.plot(time_array, data_array, 'r-o', markerfacecolor='b', mec='b', ms=8, markevery=4,  label='V(t)')
fig.suptitle('Процесс заряда конденсатора RC-цепочке', size=20)
ax.set(xlim=(0, int(max(time_array)+1)), ylim=(0, int(max(data_array)+1)))

plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')

ax.minorticks_on()
ax.grid(which='major', color='black', linewidth=1)
ax.grid(which='minor', color='black', linewidth=0.5, ls=':')
ax.legend(loc='upper right')

plt.figtext(0.62, 0.6, maxt, size=20)
fig.savefig('test.svg')
plt.show()
