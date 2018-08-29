import matplotlib.pyplot as plt
import numpy as np

G = 6.67e-11

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
            b.reset()
            for j,p in enumerate(lista):
                b.addforce(p)

    def update(self):
        self.compute()
        for b in self.bb:
            b.X.append(b.x[0])
            b.Y.append(b.x[1])

            aX = b.f[0]/b.mass
            aY = b.f[1]/b.mass
            
            b.x[0] += b.v[0] * self.dt + aX/2 * self.dt * self.dt
            b.x[1] += b.v[1] * self.dt + aY/2 * self.dt * self.dt   

            self.compute()
            
            b.v[0] += (aX + b.f[0]/b.mass)/2 * self.dt
            b.v[1] += (aY + b.f[1]/b.mass)/2 * self.dt
            
        print(self.current)    
        self.current += 1
        self.t += self.dt

    def run(self,T):
        while self.t<T:
            self.update()
            
    def plot(self):
        f, dat = plt.subplots(1)
        #plt.axes().set_aspect('equal')
        for b in self.bb:
            dat.plot( b.X, b.Y)
        plt.show()

sim = simulation(1e3)

sole = body(2e30)
sole.ic(0,0,0,0)
terra = body(6e24)
terra.ic(1.47e11,0,0,3.03e4)
luna = body(7.35e22)
luna.ic(1.47e11,3.633e8,-1076,3.03e4)
venere = body(4.87e24)
venere.ic(1.07e11,0,0,3.53e4)
buconero = body(2e33)
buconero.ic(1e13,0,0,1e3)
sim.bb.append(sole)
sim.bb.append(terra)
sim.bb.append(luna)
sim.bb.append(venere)
#sim.bb.append(buconero)

sim.run(3e7)

sim.plot()


