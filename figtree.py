import matplotlib.pyplot as plt
import numpy as np

r = np.arange(1.,4.,0.005)
x = [0.5]
x = x*600
x = np.asarray(x)
x = x.reshape(600,1)
r = r.reshape(600,1)

def map(r1,x1):
    x1 = r1 * x1 * (1-x1)
    return x1

it = 0
while it<1000:
    x = map(r,x)
    it = it+1

R = r
X = x
it = 0
while it<1000:
    x = map(r,x)
    R = np.concatenate((R,r),axis=0)
    X = np.concatenate((X,x),axis=0)
    it = it+1

plt.scatter(R,X,s=0.3,lw=0.1,marker="o")
plt.show()
    

