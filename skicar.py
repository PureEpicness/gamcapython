import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="black")
c.pack()

r=5
def pohyb(e):
    x,y=e.x,e.y
    c.create_oval(x+r,y+r,x-r,y-r,fill="pink")
    a=X_MAX-x
    b=Y_MAX-y
    c.create_oval(a+r,y+r,a-r,y-r,fill="pink")
    c.create_oval(x+r,b+r,x-r,b-r,fill="pink")
    c.create_oval(a+r,b+r,a-r,b-r,fill="pink")

c.bind("<Motion>",pohyb)
