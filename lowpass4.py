import numpy as np
import matplotlib.pyplot as plt

def rk4(f,a,b,y0,h):
    y = np.zeros(int((b-a)/h))
    y[0] = y0
    for i in range(len(y)-1):
        k1 = f(i*h, y[i])
        k2 = f((i+0.5)*h,y[i]+0.5*k1*h)
        k3 = f((i+0.5)*h,y[i]+0.5*k2*h)
        k4 = f(i*h,y[i]+k3*h)
        y[i+1] = y[i] + h/6*(k1+2*k2+2*k3+k4)
    return y

rc = 0.1

def Vin(t):
    if int(2*t)%2 == 0:
        return 1.
    else:
        return -1.

def lowpass(t,y):
    return 1/rc*(Vin(t) - y)

h = 0.001
y = rk4(lowpass,0,10,0,h)
t = np.arange(0,10.,h)
plt.plot(t,y)
plt.show()
