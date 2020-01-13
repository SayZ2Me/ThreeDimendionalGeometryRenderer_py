from tkinter import *
import ShapeCreator as SC
import time

scale = 2

fc=0

sx,sy = 1920,1080

offsetx,offsety=sx-sx/10,sy-sy/10

EyePoint = [0,0,10]

EPToPlaneDist = 10

def drawPerspective(canvas,shape):
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

def draw_dot(canvas,x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r,outline="white")

def OnDestroy():
    root.quit()
    root.destroy()
    

def RunAnimation(canvas,root):
    line = SC.CreateLine(0,0,0)
    square = SC.CreatePlane()
    cube = SC.CreateCube()
    cube.verts[0][2]=0
    cube.verts[2][2]=0
    cube.verts[4][2]=0
    cube.verts[6][2]=0
    cube.verts[1][2]=0
    cube.verts[3][2]=0
    cube.verts[5][2]=0
    cube.verts[7][2]=0
    for i in range(2,100):
        ft=time.time()
        canvas.delete("all")
        drawPerspective(canvas,square)
        square.verts[0][1]+=0.01
        square.verts[1][1]-=0.01
        square.verts[2][1]-=0.01
        square.verts[3][1]+=0.01
        root.update()
        while(time.time()-ft<0.005):
            pass
    for i in range(100):
        ft=time.time()
        canvas.delete("all")
        drawPerspective(canvas,cube)
        cube.verts[0][2]-=0.01
        cube.verts[2][2]-=0.01
        cube.verts[4][2]-=0.01
        cube.verts[6][2]-=0.01
        cube.verts[1][2]+=0.01
        cube.verts[3][2]+=0.01
        cube.verts[5][2]+=0.01
        cube.verts[7][2]+=0.01
        root.update()
        while(time.time()-ft<0.005):
            pass
    for i in range(100):
        ft=time.time()
        canvas.delete("all")
        drawPerspective(canvas,cube)
        cube = SC.Rotate(cube,100)
        root.update()
        while(time.time()-ft<0.01):
            pass
    for i in range(100):
        ft=time.time()
        canvas.delete("all")
        drawPerspective(canvas,cube)
        cube.verts[0][1]/=1.1
        cube.verts[0][2]/=1.1
        cube.verts[1][1]/=1.1
        cube.verts[1][2]/=1.1
        cube.verts[2][1]/=1.1
        cube.verts[2][2]/=1.1
        cube.verts[3][1]/=1.1
        cube.verts[3][2]/=1.1
        root.update()
        while(time.time()-ft<0.02):
            pass
    for i in range(20):
        ft=time.time()
        canvas.delete("all")
        drawPerspective(canvas,cube)
        cube.verts[4][1]/=1.3
        cube.verts[4][2]/=1.3
        cube.verts[5][1]/=1.3
        cube.verts[5][2]/=1.3
        cube.verts[6][1]/=1.3
        cube.verts[6][2]/=1.3
        cube.verts[7][1]/=1.3
        cube.verts[7][2]/=1.3
        root.update()
        while(time.time()-ft<0.02):
            pass
        

root=Tk()
root.geometry("{}x{}".format(sx,sy))
root.title("Program")
root.protocol ("WM_DELETE_WINDOW",OnDestroy)
sx=root.winfo_screenwidth()
sy=root.winfo_screenheight()
canvas = Canvas(root, width = sx,height = sy,bg="black")
canvas.pack()
while True:
    RunAnimation(canvas,root)
