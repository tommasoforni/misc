import math

class particle:
    m = 1.
    x = 0.
    y = 0.
    z = 0.
    vx = 0.
    vy = 0.
    vz = 0.
    fx = 0.
    fy = 0.
    fz = 0.
    def __init__(self,mm,px,py,pz):
        self.m = mm
        self.x = px
        self.y = py
        self.z = pz

    def dump(self):
        print("p: ", self.x,self.y,self.z)
        print("v: ", self.vx,self.vy,self.vz)
        print("f: ", self.fx,self.fy,self.fz)

class simulation:
    def __init__(self):
        self.particles = []
        self.epsilon = 1.
        self.sigma = 1.
        self.alpha = 0.0167
        self.cut = 1.3
        self.ts = 0.000005
        self.current = 0
        self.total = 1000000
        self.pe = 0.

    def force(self,a, b):
        rm = math.sqrt( ((a.x + b.x )/2)**2 + ((a.y + b.y )/2)**2 + ((a.z + b.z )/2)**2 )
        delx = a.x - b.x
        dely = a.y - b.y
        delz = a.z - b.z
        rsq = (delx)**2 +(dely)**2 +(delz)**2 
        r2inv = 1./rsq
        r6inv = r2inv*r2inv*r2inv
        shrink = (self.sigma * (1-rm* self.alpha *self.current/self.total)) ** 6
        forza = 24. * self.epsilon * shrink * r6inv*( 2 * shrink * r6inv -1) *r2inv
        pe =  2* self.epsilon *shrink * r6inv *( shrink*r6inv-1)
        return [forza*delx, forza*dely, forza*delz,pe]
        
        

    def compute(self,d):
        self.pe = 0.
        for i,p in enumerate(self.particles):
            lista = self.particles[:]
            lista.pop(i)
            p.fx = 0.
            p.fy = 0.
            p.fz = 0.
            for j,pp in enumerate(lista):
                f = self.force(p,pp)
                p.fx += f[0]
                p.fy += f[1]
                p.fz += f[2]
                self.pe += f[3]

            if d == 1:
                print("particella ",i, "step ",self.current)
                p.dump()
        self.pe /= len(self.particles)
                

    def update(self):
         for i,p in enumerate(self.particles):
             p.x += p.vx * self.ts
             p.y += p.vy * self.ts
             p.z += p.vz * self.ts

             p.vx += p.fx / p.m * self.ts
             p.vy += p.fy / p.m * self.ts
             p.vz += p.fz / p.m * self.ts
            
         self.current +=1
        
        
    def energydump(self):
        #print("energie step", self.current)
        print('pe =',self.pe) 
        ke = 0.
        for i in self.particles:
            ke += 1/2*i.m*(i.vx*i.vx+i.vy*i.vy+i.vz*i.vz)
        #print("ke =",ke)
        #print("etot =", self.pe+ke)
        
        
    def run(self,dumps):
        while self.current < self.total+1:
            if self.current % dumps == 0:
                self.compute(0)
                self.energydump()
                self.update()
            else:
                self.compute(0)
                self.update()
            
            

sim = simulation()

a = particle(1,30,0,0)
b = particle(1,30,1.3,0)
c = particle(1,30,0,1.3)
sim.particles.append(a)
sim.particles.append(b)
sim.particles.append(c)

sim.run(50000)
