import tkinter

canvas=tkinter.Canvas(width="800",height="600",bg="green")
canvas.pack()
import random

def domcek(x,y,r=50):

    canvas.create_rectangle(x,y,x+r,y+r)
    canvas.create_polygon(x,y,x+r,y,x+0.5*r,y-0.5*r)

for i in range(1,3):
    domcek(400,300)
    
