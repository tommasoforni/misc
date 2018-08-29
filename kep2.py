import matplotlib.pyplot as plt
import numpy as np

G = 1.

class body:

    
    def __init__(self, m):
        self.mass = m
        self.X = []
        self.Y = []
        self.x = [0.0, 0.0]
        self.v = [0.0, 0.0]
        self.f = [0.0, 0.0]

    def ic(self, xx, y, vx, vy):
        self.x = [xx,y]
        self.v = [vx,vy]

    def dist(self,B):
        dx = self.x[0] - B.x[0]
        dy = self.x[1] - B.x[1]
        r = ( (self.x[0]-B.x[0])**2 + (self.x[1]-B.x[1])**2 ) **(0.5)
        return [dx,dy,r]

    def reset(self):
        self.f = [0.0,0.0]
    
    def addforce(self, B):
        d = self.dist(B)
        fof = - self.mass * B.mass * G / d[2]**3
        self.f[0] += fof * d[0]
        self.f[1] += fof * d[1]

class simulation:

    def __init__(self, timestep):
        self.dt = timestep
        self.bb = []
        self.t = 0.0
        self.current = 0
        
    def compute(self):
        for i,b in enumerate(self.bb):
            lista = self.bb[:]
            lista.pop(i)
            print(b.f)
            b.reset()
            for j,p in enumerate(lista):
                b.addforce(p)

    def update(self):
        self.compute()
        for b in self.bb:
            b.X.append(b.x[0])
            b.Y.append(b.x[1])

            b.x[0] += b.v[0] * self.dt
            b.x[1] += b.v[1] * self.dt    

            b.v[0] += b.f[0]/b.mass * self.dt
            b.v[1] += b.f[1]/b.mass * self.dt
       # print(self.current)    
        self.current += 1
        self.t += self.dt

    def run(self,T):
        while self.t<T:
            self.update()
    

    def plot(self):
        f, dat = plt.subplots(1)
        for b in self.bb:
            dat.plot( b.X, b.Y)
        plt.show()

sim = simulation(0.01)

s = 1.84
sole = body(1*s)
sole.ic(1,0,0,1)
terra = body(1*s)
terra.ic(-0.5,0.866,-0.866,-0.5)
luna = body(1*s)
luna.ic(-0.5,-0.866,0.866,-0.5)
sim.bb.append(sole)
sim.bb.append(terra)
sim.bb.append(luna)

sim.run(15)
sim.plot()


