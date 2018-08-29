import numpy as np
import matplotlib.pyplot as plt

def f(x,c):
    return 1-np.exp(-c*x)

h = 10e-6
c = np.arange(0,3,0.01)
x = np.zeros(len(c))
for i,cc in enumerate(c):
    y = np.random.random()
    yy = f(y,cc)
    while abs(yy-y)>h:
        y = yy
        yy = f(y,cc)
    x[i] = yy

plt.plot(c,x)
plt.show()
