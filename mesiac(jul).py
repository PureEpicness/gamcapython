import tkinter
import random
canvas=tkinter.Canvas(height=400,width=800,bg="white")
canvas.pack()

def mesiac(x,y,r,pozadie="white",farba="yellow"):
    
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x-0.5*r,y-r,x+1.5*r,y+r,fill=pozadie,outline=pozadie)
    
z=(random.randint(30,170))


def vlajka(x,y,farba="green"):
    canvas.create_oval(x,y,x+100,y+100,fill="brown")
    canvas.create_line(x+50,y,x+50,y-100)
    canvas.create_rectangle(x+50,y-160,x+150,y-100,fill=farba)
vlajka(50,180)

vlajka(800-150,180,"red")

def luna(x,y,r,pozadie,farba):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x-1.5*r,y-r,x+2.5*r,y+r,fill=pozadie,outline=pozadie)

def logo():
    mesiac()
    luna()

canvas.create_rectangle(1,200,800,400,fill="blue",outline="blue")

mesiac(340,z,30)
mesiac(340,400-z,30,"blue")
mesiac(150,50,20,"green","red")
