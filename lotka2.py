import numpy as np
from numpy import array
import matplotlib.pyplot as plt

def rk4(f,a,b,y0,h):
    y = np.zeros((int((b-a)/h),len(y0)) )
    y[0] = y0
    for i in range(len(y)-1):
        k1 = f(i*h, y[i])
        k2 = f((i+0.5)*h,y[i]+0.5*k1*h)
        k3 = f((i+0.5)*h,y[i]+0.5*k2*h)
        k4 = f(i*h,y[i]+k3*h)
        y[i+1] = y[i] + h/6*(k1+2*k2+2*k3+k4)
    return y

g = 9.81
m = 1.
R = 0.08
rho = 1.22
C = 0.47
theta = np.pi/180.* 30.
V = 100.
y0 = [0,V*np.cos(theta),0,V*np.sin(theta)]

def drag(t,v):
    vx = v[1]
    vy = v[3]
    x = v[0]
    y = v[2]
    d = np.pi * R*R * rho * C/(2*m) *np.sqrt(vx*vx+vy*vy)
    vxp = -d*vx
    xp = vx
    vyp = -g -d*vy
    yp = vy
    return array([xp,vxp,yp,vyp])

h = 0.005
y1 = rk4(drag,0,10,y0,h)
m = 2.
y2 = rk4(drag,0,10,y0,h)
m = 5000.
y5 = rk4(drag,0,10,y0,h)
m = 1000.
y10 = rk4(drag,0,10,y0,h)

plt.scatter(y1.T[0],y1.T[2])
plt.scatter(y2.T[0],y2.T[2])
plt.scatter(y5.T[0],y5.T[2])
plt.scatter(y10.T[0],y10.T[2])
plt.legend()
plt.show()
