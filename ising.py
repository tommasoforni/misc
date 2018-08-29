import numpy as np
from numpy.random import randint
from numpy.random import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class lattice:

    def __init__(self,d,j):
        self.latt = 2*randint(2,size=(d,d))-1
        self.sweeps = 0
        self.J = j
        self.dim = d
        
    def siteEnergy(self,n,m):
        return self.latt[n][m]*self.J*(self.latt[n][m-1+self.dim*int(m-1<0)]+self.latt[n-1+self.dim*int(n-1<0)][m]+self.latt[n+1-self.dim*int(n+1>=self.dim)][m]+self.latt[n][m+1-self.dim*int(m+1>=self.dim)])
    
    def sweep(self):
        temp = np.copy(self.latt)
        for i in range(self.dim):
            for j in range(self.dim):
                if random()<(self.siteEnergy(i,j)+4.)/8.:
                    temp[i][j] *= -1.
                
        self.latt = np.copy(temp)
        self.sweeps += 1
        self.ims=[]
        self.fig = plt.figure()

    def image(self):
        ani = animation.ArtistAnimation(self.fig,self.ims,interval=50,blit=True,repeat_delay=1000)
        ani.save('sas.mp4')

    def M(self):
        m = 0.
        for i in range(self.dim):
            for j in range(self.dim):
                m += self.latt[i][j]
        return m/(self.dim*self.dim)

    def run(self,steps,draw):
        self.ims = []
        while self.sweeps<steps:
            print(self.sweeps)
            print(self.M())
            if draw:
                im = plt.imshow(self.latt,animated=True)
                self.ims.append([im])
            self.sweep()

    
    
a = lattice(50,+0.9)
a.run(100,1)
a.image()
