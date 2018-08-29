import numpy as np
import matplotlib.pyplot as plt

w = 1e-9
M = 9.1094e-31
e = 1.6022e-19
h = 1.0545e-34
Emax = 20*e
V = Emax

x = np.arange(0.5*e,Emax-0.5*e,Emax/100.)
y = np.zeros(len(x))
yy = np.zeros(len(x))
yyy = np.zeros(len(x))

for i,xx in enumerate(x):
    y[i] = np.tan(np.sqrt(w*w*M*xx/(2*h*h)))
    yy[i] = np.sqrt((V-xx)/xx)
    yyy[i] = -np.sqrt(xx/(V-xx))

x = x/e
plt.plot(x,y)
plt.plot(x,yy)
plt.plot(x,yyy)
plt.show()
