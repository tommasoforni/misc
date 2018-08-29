import numpy as np
from numpy import sin, cos, exp, pi, sqrt
import matplotlib.pyplot as plt
from scipy.integrate import quad

L = 5e-10
M = 9.1094e-31
e = 1.6022e-19
a = 10*e
h = 1.0545e-34

def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm

def V(x):
    return a*x/L

def makefun(m,n): #not really funny
    return lambda x: sin(pi*m*x/L) * ((h*pi*n/L)**2/(2*M) + V(x) ) *sin(pi*n*x/L) 

def element(m,n):
    integrand = makefun(m,n)
    return 2/L * quad(integrand,0,L)[0]

terms = 30
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
print(energies)
print(eig)

x = np.arange(0,L,L/150.)
y = np.zeros(len(x))
yy = np.zeros(len(x))
yyy = np.zeros(len(x))

v = np.zeros(len(x))


def f(x,i):
    sinarray = np.zeros(terms)
    for n in range(1,terms+1):
        sinarray[n-1] = sqrt(2/L) *sin(x*pi*n/L) 
    return np.dot(sinarray,eig[i])

for i,xx in enumerate(x):
    y[i] = f(xx,0)
    yy[i] = f(xx,1)
    yyy[i] = f(xx,2)
    v[i] = V(xx)/e*2e3

plt.plot(x,y,label=energies[0])
plt.plot(x,yy,label=energies[1])
plt.plot(x,yyy,label=energies[2])
plt.plot(x,v,label='V(x)')
plt.legend()
plt.show()


        
