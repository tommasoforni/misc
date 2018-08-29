import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("alt2.txt")
h = 100.

dX = data
dY = data

i = 1
while i<data.shape[0]-1:
    j = 1
    while j<data.shape[1]-1:
        dY[i][j] = (data[i+1][j] - data[i-1][j])/ (2*h)
        dX[i][j] = (data[i][j+1] - data[i][j-1])/ (2*h)
        j = j+1
    i = i+1

j = 1
while j<data.shape[1]-1:
    dX[0][j] = (data[0][j+1] - data[0][j-1])/ (2*h)
    dX[data.shape[0]-1][j] = (data[data.shape[0]-1][j+1] - data[data.shape[0]-1][j-1])/ (2*h)
    j = j+1
    
i = 1
while i<data.shape[0]-1:
    dY[i][0] = (data[i+1][0] - data[i-1][0])/ (2*h)
    dY[i][data.shape[1]-1] = (data[i+1][data.shape[1]-1] - data[i-1][data.shape[1]-1])/ (2*h)
    i = i+1

i = 0
j = 0
dX[i][j] = (data[i][j+1] - data[i][j] ) / h
dY[i][j] = (data[i+1][j] - data[i][j] ) / h

j = data.shape[1]-1
dX[i][j] = (data[i][j] - data[i][j-1] ) / h
dY[i][j] = (data[i+1][j] - data[i][j] ) / h

i = data.shape[0]-1
dX[i][j] = (data[i][j] - data[i][j-1] ) / h
dY[i][j] = (data[i][j] - data[i-1][j] ) / h

j = 0
dX[i][j] = (data[i][j+1] - data[i][j] ) / h
dY[i][j] = (data[i][j] - data[i-1][j] ) / h

angle = np.pi*1. #light angle
a = [np.cos(angle),np.sin(angle)] #light vector
I = ( a[0] * dX + a[1] * dY ) / ( dX**2 + dY**2 + 1)**0.5 #intensity array
    
plt.imshow(I,cmap='Greys_r')
plt.show()
