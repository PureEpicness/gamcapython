import tkinter
import random
X_MAX,Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX, height=Y_MAX)
c.pack()

def vlak(p,x,y,d,farba):
    for i in range(p):
        c.create_line(x,y+3.5*d,x+d,y+3.5*d,width=5)
        c.create_rectangle(x+d,y,x+8*d,y+4*d,fill=farba)
        c.create_line(x+8*d,y+3.5*d,x+9*d,y+3.5*d,width=5)
        c.create_oval(x+2*d,y+3*d,x+4*d,y+5*d,fill="black")
        c.create_oval(x+5*d,y+3*d,x+7*d,y+5*d,fill="black")
        x+=9*d

vlak(4,20,50,20,"red")
vlak(2,20,250,20,"green")
vlak(3,20,450,20,"blue")

