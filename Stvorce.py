import tkinter
import random
X_MAX, Y_MAX = 800, 600
c=tkinter.Canvas(width=X_MAX, height=Y_MAX)
c.pack()

r=random.randint(150,300)
def kachla(r,x,y,z):
    for i in range(z):
        c.create_rectangle(x-r*0.5,y-r*0.5,x+r*0.5,y+r*0.5)
        r-=10
        
for i in range(10):
    kachla(random.randint(150,300),random.randint(r,X_MAX-r),random.randint(r,Y_MAX-r),random.randint(5,10))
   
