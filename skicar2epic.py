import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()
r=5
def klik(event):
    x,y=event.x,event.y
    c.create_oval(x+r,y+r,x-r,y-r,fill="red")
    global xx,yy
    xx,yy=x,y
def pusti(event):
    x,y=event.x,event.y
    c.create_oval(x+r,y+r,x-r,y-r,fill="blue")
    c.create_line(xx,yy,x,y)

c.bind("<ButtonPress>",klik)
c.bind("<ButtonRelease>",pusti)
