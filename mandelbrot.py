import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.,2.,0.001)
y = np.arange(-2.,2.,0.001)
man = np.zeros(shape=(len(x),len(y)))

def map(c,x1):
    x1 = x1*x1+c
    return x1

for i,x1 in enumerate(x):
    for k,y1 in enumerate(y):
        c = x1+y1*1.j
        it = 0
        z = 0+0.j
        while it<100 and abs(z)<2:
            z = map(c,z)
            it = it+1
            man[i][k]=it
            
plt.imshow(man)
plt.imsave('mandelbrot.png',man)
plt.show()
    

