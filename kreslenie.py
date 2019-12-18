import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()
kreslit = False
def klik(event):
    global xx,yy
    xx,yy=event.x,event.y
    global kreslit
    kreslit=True

def pust(event):
    global kreslit
    kreslit=False

def kreslit(event):
    global xx,yy
    x,y=event.x,event.y
    if kreslit==True:
        c.create_line(xx,yy,x,y,fill="black")
    xx,yy=x,y

c.create_rectangle(X_MAX-50,Y_MAX-50,X_MAX,Y_MAX,fill="green")


c.bind("<ButtonPress>",klik)
c.bind("<ButtonRelease>",pust)
c.bind("<Motion>",kreslit)

