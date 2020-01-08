import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()
kreslit = False
farba="black"
w="1"
def ikony():
    c.create_rectangle(X_MAX-50,Y_MAX-50,X_MAX,Y_MAX,fill="black")
    c.create_rectangle(X_MAX-100,Y_MAX-50,X_MAX-50,Y_MAX,fill="red")
    c.create_rectangle(X_MAX-150,Y_MAX-50,X_MAX-100,Y_MAX,fill="green")
    c.create_rectangle(X_MAX-200,Y_MAX-50,X_MAX-150,Y_MAX,fill="blue")
    c.create_rectangle(0,Y_MAX-50,50,Y_MAX)
    c.create_rectangle(50,Y_MAX-50,100,Y_MAX)
    c.create_rectangle(100,Y_MAX-50,150,Y_MAX)
    c.create_oval(5,Y_MAX-45,45,Y_MAX-5)
    c.create_oval(60,Y_MAX-40,90,Y_MAX-10)
    c.create_oval(120,Y_MAX-30,130,Y_MAX-20)
    c.create_rectangle(X_MAX-50,2,X_MAX,50)
    c.create_text(X_MAX-25,25,text="oblivion")
def klik(event):
    global xx,yy
    xx,yy=event.x,event.y
    global kreslit
    kreslit=True
    global farba
    if X_MAX-100<xx<X_MAX-50 and Y_MAX-50<yy<Y_MAX:
        farba="red"
    if X_MAX-50<xx<X_MAX and Y_MAX-50<yy<Y_MAX:
        farba="black"
    if X_MAX-150<xx<X_MAX-100 and Y_MAX-50<yy<Y_MAX:
        farba="green"
    if X_MAX-200<xx<X_MAX-150 and Y_MAX-50<yy<Y_MAX:
        farba="blue"
    global w
    if 0<xx<50 and Y_MAX-50<yy<Y_MAX:
        w=10
    if 50<xx<100 and Y_MAX-50<yy<Y_MAX:
        w=5
    if 100<xx<150 and Y_MAX-50<yy<Y_MAX:
        w=1
    if X_MAX-50<xx<X_MAX and 0<yy<50:
        c.delete("all")
        ikony()
    
def pust(event):
    global kreslit
    kreslit=False

def kreslit(event):
    global xx,yy
    x,y=event.x,event.y
    if kreslit==True:
        c.create_line(xx,yy,x,y,fill=farba,width=w)
    xx,yy=x,y


ikony()
c.bind("<ButtonPress>",klik)
c.bind("<ButtonRelease>",pust)
c.bind("<Motion>",kreslit)

