import math

class shape:
    def __init__(self):
        self.verts=[]
        self.relativity=[]
    def add(self,v):
        self.verts.append(v);
    def setRelativitys(self,rel):
        self.relativity.append(rel)

def CreatePlane():
    Plane = shape()
    
    Plane.add([1,0,1])
    Plane.add([1,0,-1])
    Plane.add([-1,0,-1])
    Plane.add([-1,0,1])

    Plane.setRelativitys([0,1])
    Plane.setRelativitys([1,2])
    Plane.setRelativitys([2,3])
    Plane.setRelativitys([3,0])
    
    return Plane

def CreateCube():
    Cube = shape()
    
    Cube.add([-10,-10,-10])
    Cube.add([-10,-10,10])
    Cube.add([-10,10,-10])
    Cube.add([-10,10,10])
    Cube.add([10,-10,-10])
    Cube.add([10,-10,10])
    Cube.add([10,10,-10])
    Cube.add([10,10,10])
    
    Cube.setRelativitys([0,1])
    Cube.setRelativitys([0,2])
    Cube.setRelativitys([0,4])
    Cube.setRelativitys([7,3])
    Cube.setRelativitys([7,5])
    Cube.setRelativitys([7,6])
    Cube.setRelativitys([1,3])
    Cube.setRelativitys([1,5])
    Cube.setRelativitys([2,3])
    Cube.setRelativitys([2,6])
    Cube.setRelativitys([4,5])
    Cube.setRelativitys([4,6])

    return Cube

def CreateOctahedron():
    Octahedron = shape()

    Octahedron.add([0,-1,0])
    Octahedron.add([-1,0,0])
    Octahedron.add([0,0,1])
    Octahedron.add([1,0,0])
    Octahedron.add([0,0,-1])
    Octahedron.add([0,1,0])

    Octahedron.setRelativitys([0,1])
    Octahedron.setRelativitys([0,2])
    Octahedron.setRelativitys([0,3])
    Octahedron.setRelativitys([0,4])
    Octahedron.setRelativitys([5,1])
    Octahedron.setRelativitys([5,2])
    Octahedron.setRelativitys([5,3])
    Octahedron.setRelativitys([5,4])
    Octahedron.setRelativitys([1,2])
    Octahedron.setRelativitys([2,3])
    Octahedron.setRelativitys([3,4])
    Octahedron.setRelativitys([4,1])

    return Octahedron

def CreateIcosahedron():
    Icosahedron = shape()
    
    Icosahedron.add([2,0,1])
    Icosahedron.add([-2,0,1])
    Icosahedron.add([2,0,-1])
    Icosahedron.add([-2,0,-1])
    
    Icosahedron.add([1,2,0])
    Icosahedron.add([1,-2,0])
    Icosahedron.add([-1,2,0])
    Icosahedron.add([-1,-2,0])
    
    Icosahedron.add([0,1,2])
    Icosahedron.add([0,1,-2])
    Icosahedron.add([0,-1,2])
    Icosahedron.add([0,-1,-2])
    
    Icosahedron.setRelativitys([0,4])    
    Icosahedron.setRelativitys([0,5])
    Icosahedron.setRelativitys([0,8])
    Icosahedron.setRelativitys([0,10])

    
    Icosahedron.setRelativitys([1,6])    
    Icosahedron.setRelativitys([1,7])   
    Icosahedron.setRelativitys([1,8])  
    Icosahedron.setRelativitys([1,10])
        
    Icosahedron.setRelativitys([2,4])
    Icosahedron.setRelativitys([2,5])
    Icosahedron.setRelativitys([2,11])
    Icosahedron.setRelativitys([2,9])
    
    Icosahedron.setRelativitys([3,6])
    Icosahedron.setRelativitys([3,7])
    Icosahedron.setRelativitys([3,11])
    Icosahedron.setRelativitys([3,9])

    
    Icosahedron.setRelativitys([4,8])
    Icosahedron.setRelativitys([6,8])

    Icosahedron.setRelativitys([4,9])
    Icosahedron.setRelativitys([6,9])

    Icosahedron.setRelativitys([5,10])
    Icosahedron.setRelativitys([7,10])

    Icosahedron.setRelativitys([5,11])
    Icosahedron.setRelativitys([7,11])

    Icosahedron.setRelativitys([0,2])
    Icosahedron.setRelativitys([1,3])
    
    Icosahedron.setRelativitys([4,6])
    Icosahedron.setRelativitys([5,7])
    
    Icosahedron.setRelativitys([8,10])
    Icosahedron.setRelativitys([9,11])
    
    return Icosahedron

def CreateTetrahedron():

    Tetrahedron = shape()

    Tetrahedron.add([-1,1,-1])
    Tetrahedron.add([1,1,1])
    Tetrahedron.add([-1,-1,1])
    Tetrahedron.add([1,-1,-1])

    Tetrahedron.setRelativitys([0,1])
    Tetrahedron.setRelativitys([1,2])
    Tetrahedron.setRelativitys([2,3])
    Tetrahedron.setRelativitys([3,0])
    Tetrahedron.setRelativitys([0,2])
    Tetrahedron.setRelativitys([1,3])

    return Tetrahedron

def CreateTorus():

    Torus = shape()

    TorBuf = shape()

    n=32
    
    alpha = math.pi / n * 2
    
    r = 2

    R = 5

    x,y,z=r,0,0

    for k in range(n):
        TorBuf.add([x * (math.cos(alpha*k)) - y * (math.sin(alpha*k)) + R,x * (math.sin(alpha*k)) + y * (math.cos(alpha*k)),z])
    
    for k in range(n):
        x1,y1,z1 = TorBuf.verts[k][0],TorBuf.verts[k][1],TorBuf.verts[k][2]
        for i in range(n):
            Torus.add([x1 * (math.cos(alpha*i)) - z1 * (math.sin(alpha*i)),y1,x1 * (math.sin(alpha*i)) + z1 * (math.cos(alpha*i))])
    for i in range(n):
        for k in range(n):
            Torus.setRelativitys([i + k*n,(i+1)%n + k*n])
            Torus.setRelativitys([ (0 + i + k * n)%(n*n), (0 + n + i + k * n)%(n*n)])
    
    return Torus
