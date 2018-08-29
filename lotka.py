import numpy as np
import matplotlib.pyplot as plt

def rk4(f,g,a,b,x0,y0,h):
    y = np.zeros(int((b-a)/h))
    x = np.zeros(len(y))
    y[0] = y0
    x[0] = x0
    for i in range(len(y)-1):
        k1 = g(i*h, x[i], y[i])
        l1 = f(i*h, x[i], y[i])
        k2 = g( (i+0.5)*h, x[i]+0.5*l1*h, y[i]+0.5*k1*h)
        l2 = f( (i+0.5)*h, x[i]+0.5*l1*h, y[i]+0.5*k1*h)
        k3 = g( (i+0.5)*h, x[i]+0.5*l2*h, y[i]+0.5*k2*h)
        l3 = f( (i+0.5)*h, x[i]+0.5*l2*h, y[i]+0.5*k2*h)
        k4 = g(i*h, x[i]+l3*h, y[i]+k3*h)
        l4 = f(i*h, x[i]+l3*h, y[i]+k3*h)
        x[i+1] = x[i] + h/6*(l1+2*l2+2*l3+l4)
        y[i+1] = y[i] + h/6*(k1+2*k2+2*k3+k4)
    return [x,y]

a = 1
b = 0.5
c = 0.5
d = 2
x0 = 2
y0 = 2

def lotkaX(t,x,y):
    return a*x-b*x*y

def lotkaY(t,x,y):
    return c*x*y-d*y

h = 0.001
y = rk4(lotkaX,lotkaY,0,30,x0,y0,h)
t = np.arange(0,30.,h)
plt.plot(t,y[0])
plt.plot(t,y[1])
plt.show()
