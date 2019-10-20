from tkinter import *
import ShapeCreator as SC

scale = 30

sy,sx = 0,0

offsetx,offsety=sx/2,sy/2

mx,my=0,0.5

DotSize=3/2
    
def drawOrt(canvas,shape):
    for relate in shape.relativity:
        canvas.create_line((shape.verts[relate[0]][0]+shape.verts[relate[0]][2]*mx) + offsetx,-(shape.verts[relate[0]][1]+shape.verts[relate[0]][2]*my)  + sy - offsety,(shape.verts[relate[1]][0]+shape.verts[relate[1]][2]*mx)  + offsetx,-(shape.verts[relate[1]][1]+shape.verts[relate[1]][2]*my) + sy - offsety,fill='white')

def drawVertDotsInOrt(canvas,shape):
    for vert in shape.verts:
        canvas.create_line((vert[0] + vert[2] * mx)  + offsetx - DotSize,-(vert[1] + vert[2] * my)  + sy - offsety ,(vert[0] + vert[2] * mx)  + offsetx + DotSize,-(vert[1] + vert[2] * my)  + sy - offsety,width=DotSize*2,fill='lime')

def drawPerspective(canvas,shape):
    EyePoint = [0,3,15]

    EPToPlaneDist = 10
    
    """for vert in shape.verts:
        
        D = EyePoint[2] - (vert[2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2] / D
        x = (vert[0] - EyePoint[0]) * attitude * scale
        y = (vert[1] - EyePoint[1]) * attitude * scale
        
        canvas.create_line(x - DotSize + offsetx , y + offsety , x + DotSize + offsetx ,y + offsety ,width=DotSize*2,fill='lime')
    """
    for relate in shape.relativity:
        
        D = EyePoint[2] - (shape.verts[relate[0]][2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2]/D
        x = (shape.verts[relate[0]][0] - EyePoint[0]) * attitude * scale
        y = (shape.verts[relate[0]][1] - EyePoint[1]) * attitude * scale
        
        D = EyePoint[2] - (shape.verts[relate[1]][2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2]/D
        x1 = (shape.verts[relate[1]][0] - EyePoint[0]) * attitude * scale
        y1 = (shape.verts[relate[1]][1] - EyePoint[1]) * attitude * scale
        
        canvas.create_line(x+ offsetx,y+ offsety,x1+ offsetx,y1+ offsety,fill='white')
        
Octahedron= SC.CreateOctahedron()

Icosahedron = SC.CreateIcosahedron()

Cube = SC.CreateCube()

Plane = SC.CreatePlane()

Tetrahedron = SC.CreateTetrahedron()

Torus = SC.CreateTorus()

root=Tk()
root.geometry("1920x1080")
root.title("3DProject")
sx=root.winfo_screenwidth()
sy=root.winfo_screenheight()
canvas = Canvas(root, width = sx,height = sy,bg="black")
canvas.pack()

Cicle=True

while Cicle:
    sx=canvas.winfo_width()
    sy=canvas.winfo_height()
    canvas.width=sx
    canvas.height=sy
    canvas.delete("all")

    offsetx,offsety=sx/2,sy/2
    #drawOrt(canvas,Torus)
    drawPerspective(canvas,Torus)
    
    root.update()
