from tkinter import *
import ShapeCreator as SC
import time

scale = 200

fc=0

sx,sy = 1920,1080

offsetx,offsety=sx/2,sy/2

DotSize=3/2

EyePoint = [1,1,20]

EPToPlaneDist = 10

def drawPerspectiveGrid(canvas):
    
    XYZ=SC.CreateXYZ(EyePoint[2]-EPToPlaneDist)

    colors=['red','green','blue']

    i=0
    
    for relate in XYZ.relativity:
        
        D = EyePoint[2] - (XYZ.verts[relate[0]][2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2]/D
        x = (XYZ.verts[relate[0]][0] - EyePoint[0]) * attitude * (scale /((D*D)/1000))
        y = -(XYZ.verts[relate[0]][1] - EyePoint[1]) * attitude * (scale /((D*D)/1000))
        
        D = EyePoint[2] - (XYZ.verts[relate[1]][2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2]/D
        x1 = (XYZ.verts[relate[1]][0] - EyePoint[0]) * attitude * (scale /((D*D)/1000))
        y1 = -(XYZ.verts[relate[1]][1] - EyePoint[1]) * attitude * (scale /((D*D)/1000))
        
        canvas.create_line(x + offsetx,y + offsety,x1 + offsetx,y1 + offsety,fill=colors[i])
        i+=1
        
def drawPerspective(canvas,shape,verts):

    if(verts):
        for vert in shape.verts:
            
            D = EyePoint[2] - (vert[2]-(EyePoint[2]-EPToPlaneDist))
            attitude = EyePoint[2] / D
            x = (vert[0] - EyePoint[0]) * attitude * (scale /((D*D)/1000))
            y = (vert[1] - EyePoint[1]) * attitude * (scale /((D*D)/1000))
        
            canvas.create_line(x - DotSize + offsetx , y + offsety , x + DotSize + offsetx ,y + offsety ,width=DotSize*2,fill='#f000f0')
    
    for relate in shape.relativity:
        
        D = EyePoint[2] - (shape.verts[relate[0]][2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2]/D
        x = (shape.verts[relate[0]][0] - EyePoint[0]) * attitude * (scale /((D*D)/1000))
        y = -(shape.verts[relate[0]][1] - EyePoint[1]) * attitude * (scale /((D*D)/1000))
        
        D = EyePoint[2] - (shape.verts[relate[1]][2]-(EyePoint[2]-EPToPlaneDist))
        attitude = EyePoint[2]/D
        x1 = (shape.verts[relate[1]][0] - EyePoint[0]) * attitude * (scale /((D*D)/1000))
        y1 = -(shape.verts[relate[1]][1] - EyePoint[1]) * attitude * (scale /((D*D)/1000))
        
        canvas.create_line(x + offsetx,y + offsety,x1 + offsetx,y1 + offsety,fill='white')
def OnDestroy():
    print(fc)
    root.quit()
    root.destroy()
    
Octahedron= SC.CreateOctahedron()

Icosahedron = SC.CreateIcosahedron()

Cube = SC.CreateCube()

Plane = SC.CreatePlane()

Tetrahedron = SC.CreateTetrahedron()

Torus = SC.CreateTorus(10)

root=Tk()
root.geometry("{}x{}".format(sx,sy))
root.title("3DProject")
root.protocol ("WM_DELETE_WINDOW",OnDestroy)
sx=root.winfo_screenwidth()
sy=root.winfo_screenheight()
canvas = Canvas(root, width = sx,height = sy,bg="black")
canvas.pack()

Cicle=True
while Cicle:
    ft=time.time()
    Torus = SC.Rotate(Torus,60)
    sx=canvas.winfo_width()
    sy=canvas.winfo_height()
    canvas.width=sx
    canvas.height=sy
    offsetx,offsety=sx/2,sy/2
    while(time.time()-ft<0.02):
        fc+=1
    canvas.delete("all")
    drawPerspective(canvas,Torus,False)
    #drawPerspective(canvas,Cube,False)
    drawPerspectiveGrid(canvas)
    root.update()
