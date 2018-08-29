from PIL import Image,ImageDraw
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

im = Image.open("prova.jpg")

dimX = im.size[0]
dimY = im.size[1]

#Create Grid
n = 30./min(dimY,dimX)
N = int(n*dimX)
M = int(n*dimY)
x = np.arange(0,dimX,int(dimX/N))
y = np.arange(0,dimY,int(dimY/M))
maxX = max(x)
maxY = max(y)
grid = np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))])
grid2 = np.random.randint(-int(dimX/N),+int(dimX/N),(len(x)*len(y),2))
for i in range(0,len(x)*len(y)):
    if grid[i][0] == 0 or grid[i][0] == maxX:
        grid2[i][0] = 0
    if grid[i][1] == 0 or grid[i][1] == maxY:
        grid2[i][1] = 0
grid2 = grid + grid2

#Create Triangles
triangles = Delaunay(grid2)
points = grid2[triangles.simplices]
def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a
pointst = totuple(points)
#Draw
out = Image.new('RGB', (maxX,maxY),(255,255,255))
d = ImageDraw.Draw(out)

def areaSign(p1,p2,a,b):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    a = np.asarray(a)
    b = np.asarray(b)
    cp1 = np.cross(b-a,p1-a)
    cp2 = np.cross(b-a,p2-a)
    if np.dot(cp1,cp2)>=0:
        return True
    else:
        return False
    
def pointInTriangle(pt,t):
    b1 = areaSign(pt,t[0],t[1],t[2])
    b2 = areaSign(pt,t[1],t[0],t[2])
    b3 = areaSign(pt,t[2],t[0],t[1])
    return b1 and b2 and b3

def medianColor(t,image):
    #finds the median color in a triangle
    r, g, b = 0, 0, 0
    count = 0
    xmax = max(t[0][0],t[1][0],t[2][0])
    xmin = min(t[0][0],t[1][0],t[2][0])    
    ymax = max(t[0][1],t[1][1],t[2][1])
    ymin = min(t[0][1],t[1][1],t[2][1])
    for s in range(xmin,xmax):
        for ss in range(ymin,ymax):
            if pointInTriangle((s+0.5,ss+0.5),t):
                pixlr, pixlg, pixlb = image.getpixel((s, ss))
                r += pixlr
                g += pixlg
                b += pixlb
                count += 1
    return (int(r/count), int(g/count), int(b/count))

tcolors = np.zeros((len(triangles.simplices),3))
for i in range(len(pointst)):
    c = medianColor(pointst[i],im)
    d.polygon(pointst[i],fill=c)
    tcolors[i] = c
out.show()    
#Merge adjacent triangles with similar colors
D = 20**2
def colorDistance(c1,c2):
    return (c1[0]-c2[0])**2+(c1[1]-c2[1])**2+(c1[2]-c2[2])**2

passaggi = 5
for p in range(passaggi):
    for i in range(len(triangles.simplices)):
        for j in range(3):
            c1 = tcolors[i]
            c2 = tcolors[triangles.neighbors[i][j]]
            if colorDistance(c1,c2) < D:
                newcolor = (int((c1[0]+c2[0])/2),int((c1[1]+c2[1])/2),int((c1[2]+c2[2])/2))
                print(c1,c2,newcolor)
                d.polygon(pointst[i],fill=newcolor)
                d.polygon(pointst[triangles.neighbors[i][j]],fill=newcolor)
                tcolors[i] = newcolor
                tcolors[triangles.neighbors[i][j]] = newcolor

out.save("out", "PNG")
out.show()


