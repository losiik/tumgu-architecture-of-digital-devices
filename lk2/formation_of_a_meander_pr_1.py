import matplotlib.pyplot as plt
import numpy as np

amplitude = 5
view_length = 1000
step1 = 100
step2 = 50

def get_x(step):
    return [0] + [i for i in range(step, view_length + 1, step) for _ in range(2)]

def get_y(x):
    return [amplitude if n % 4 == 0 or n % 4 == 1 else 0 for n in range(len(x))]
    
x1 = get_x(step1)
y1 = get_y(x1)

x2 = get_x(step2)
y2 = get_y(x2)

plt.subplot(211)
plt.plot(x1, y1, marker='o')
plt.grid()

plt.subplot(212)
plt.plot(x2, y2, marker='o')
plt.grid()

plt.show()
