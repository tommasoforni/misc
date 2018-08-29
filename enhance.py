import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft2,irfft2

sigma=25.
def spread(x,y):
    return np.exp(-(x*x+y*y)/(2*sigma*sigma))

image = np.loadtxt("blur.txt")
plt.subplot(121)
plt.imshow(image,cmap='Greys_r')
f = np.zeros(image.shape)

for y in range(0,image.shape[0]):
    if y>image.shape[0]//2:
        yy = image.shape[0]-y
    else:
        yy = y
    for x in range(0,image.shape[1]):
        if x>image.shape[1]//2:
            xx = image.shape[1]-x
        else:
            xx = x
        f[y][x] = spread(xx,yy)
image = rfft2(image)
f = rfft2(f)#*image.shape[0]#*image.shape[1]

epsilon = 1e-5
for y in range(0,image.shape[0]):
     for x in range(0,image.shape[1]):
         if f[y][x] > epsilon:
             image[y][x] = image[y][x]/f[y][x]

image = irfft2(image)
plt.subplot(122)
plt.imshow(image,cmap='Greys_r')
plt.show()
