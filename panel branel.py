import tkinter
import random
canvas=tkinter.Canvas(height=800,width=800)
canvas.pack()

def panelak(x,y,v,s):
    p=x
    canvas.create_rectangle(x,y,x+s*20+10,y+v*20+10)
    for i in range(v):
        for i in range(s):
            canvas.create_rectangle(x+10,y+10,x+20,y+20)
            x=x+20
        x=p
        y=y+20

def mesto():
    for i in range(1,10):
        panelak(random.randint(1,600),random.randint(1,600),random.randint(1,10),random.randint(1,5))
        


mesto()
