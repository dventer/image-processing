import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10,10,1000)
plt.figure(figsize=(4,15))

plt.plot(x, (0.05-x**2)**0.5, '-k')
plt.plot(x, -((0.05-x**2)**0.5), '-k')


#Tentukan persamaan matematika yang diinginkan

y = x -x -0
y1 = 2*x
y2 = 2*x + 5
y3 = 2*x - 5
y4 = -2*x
y5 = -2*x + 5
y6 = -2*x - 5

plt.plot(x, y, '-k')
plt.plot(x, y1, '-k', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-y', label='y5')
plt.plot(x, y6, '-m', label='y6')


plt.legend(loc='upper left')
plt.grid()
plt.show()
