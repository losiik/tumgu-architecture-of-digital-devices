import matplotlib.pyplot as plt
import numpy as np

amplitude = 5
frequency = 5000
view_length = 0.001
step = 10.e-6

# Временной интервал от 0 до 0.001 секунды (1 мс) с шагом 1/10000 (частота)
x = np.arange(0, view_length, step)

# Создаем синусоиду с заданной частотой и амплитудой
y = amplitude * np.sin(2 * np.pi * frequency * x)

y2 = [0]
x2 = [0]

is_f = False
is_o = False
init = True

for i, elem in enumerate(y):
    if round(elem) == 4 and is_f is False:
        y2 += [0, 5]
        x2 += [x[i], x[i]]
        is_f = True
        is_o = False
        init = False
    if round(elem) == 2 and is_o is False and init is False:
        y2 += [5, 0]
        x2 += [x[i], x[i]]
        is_o = True
        is_f = False


plt.plot(x, y)
plt.axhline(y=4, color='red')
plt.axhline(y=1, color='green')
plt.plot(x2, y2)
plt.grid()

plt.show()
