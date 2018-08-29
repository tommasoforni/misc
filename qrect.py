import numpy as np
from numpy import sin, cos, exp, pi, sqrt
import matplotlib.pyplot as plt
from scipy.integrate import dblquad
from mpl_toolkits.mplot3d import Axes3D

Lx = 5e-10
Ly = 7e-10
M = 9.1094e-31
e = 1.6022e-19
a = 10*e
h = 1.0545e-34
term = 7

def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm

def V(x,y):
    xm = (x - Lx/2.)/Lx
    ym = (y - Ly/2.)/Ly
    return 0.
    #return -a*exp(-xm*xm-ym*ym)

def makefun(i,j): #not really funny
    n = int(i/term)+1 #n e k sono Y
    m = i-n+1       #m e l sono X
    k = int(j/term)+1
    l = j-k+1
    return lambda y,x: sin(pi*m*x/Lx)*sin(pi*n*y/Ly) * (((h*pi*l/Lx)**2+(h*pi*k/Ly)**2)/(2*M) + V(x,y) )* sin(pi*k*y/Ly)*sin(pi*l*x/Lx) 

def ymin(x):
    return 0.
def ymax(x):
    return Ly

def element(i,j):
    integrand = makefun(i,j)
    return 4/(Lx*Ly) * dblquad(integrand,0.,Lx,ymin,ymax)[0]

terms = term*term
H = np.zeros((terms,terms))

for i in range(1,terms+1):
    for j in range(1,terms+1):
        H[i-1][j-1] =  element(i,j)

H = H/e
eig = np.linalg.eigh(H)
energies = np.ndarray.tolist(eig[0])
P = np.ndarray.tolist(np.transpose(eig[1]))
eig = [x for _,x in sorted(zip(energies,P))]
energies = np.sort(energies)
#print(energies)
#print(eig)
print(H)
x = np.arange(0,Lx,Lx/150.)
y = np.arange(0,Ly,Ly/150.)
z = np.zeros((len(x),len(y)))

v = np.zeros((len(x),len(y)))


def f(x,y,n):
    sinarray = np.zeros(terms)
    for i in range(1,term+1):
        for j in range(1,term+1):
            sinarray[(i-1)*term+j-1] = 2*sqrt(1/(Lx*Ly)) *sin(x*pi*j/Lx)*sin(y*pi*i/Ly) 
    return np.dot(sinarray,eig[n])

for i,xx in enumerate(x):
    for j,yy in enumerate(y):
        z[i,j] = f(xx,yy,7)
        v[i,j] = V(xx,yy)/e*2e3

X, Y = np.meshgrid(x,y)
hf = plt.figure()
ha = hf.add_subplot(211,projection='3d')
hb = hf.add_subplot(212,projection='3d')
ha.plot_surface(X,Y,z)
hb.plot_surface(X,Y,v)
plt.show()

        
