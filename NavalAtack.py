import tkinter
import random
Y=400
X=2*Y
canvas=tkinter.Canvas(width=X,height=Y,bg="white")
canvas.pack()


def mesiac(x,y,r,pozadie="white",farba="yellow"):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x-0.5*r,y-r,x+1.5*r,y+r,fill=pozadie,outline=pozadie)
def vlajka(x,y,farba="green"):
    canvas.create_oval(x,y,x+100,y+100,fill="brown")
    canvas.create_line(x+50,y,x+50,y-100)
    canvas.create_rectangle(x+50,y-160,x+150,y-100,fill=farba)
def luna(x,y,r,pozadie,farba):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x+0.5*r,y-r,x-1.5*r,y+r,fill=pozadie,outline=pozadie)
def logo(x,y,r,farba,pozadie="red"): 
    luna(x+r,y,r,pozadie,farba)
    mesiac(x+r*3.5,y,r,pozadie,farba)
def lod(x,y,v,farba,pozadie):
    canvas.create_polygon(x,y,x+v*2,y+v*3,x+v*7,y+v*3,x+v*9,y,x,y,fill="brown",outline="black")
    canvas.create_rectangle(x+v*4,y-v*7,x+v*5,y,fill="brown")
    canvas.create_polygon(x+v*4.5,y-v*7,x+v*4.5,y-v,x+v*7,y-v*2,fill="white",outline="black")
    logo(x+v*3,y+v*1.5,0.75*v,farba,pozadie)
x=300
y=200
z=100
for i in range(170):
    canvas.delete("all")
    vlajka(50,180)
    vlajka(650,180,"red")
    canvas.create_rectangle(1,Y/2,X,Y,fill="blue",outline="blue")
    mesiac(150,50,20,"green","red")
    logo(716.25,50,15,"light sky blue")
    lod(x,175,10,"light sky blue","brown")
    x+=3
    lod(y,215,15,"light sky blue","brown")
    y+=6
    lod(z,275,20,"light sky blue","brown")
    z+=10
    mesiac(560,370,30,"blue")
    mesiac(560,30,30)
    canvas.update()
    canvas.after(30)
