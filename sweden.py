import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()

r=10
s=35
for i in range(10000):
    x=randrange(X_MAX)
    y=randrange(Y_MAX)

    if x<X_MAX/3 and y<Y_MAX/2-s or x<X_MAX/3 and \
       y>Y_MAX/2+s or x>X_MAX/3+2*s and y<Y_MAX/2-s or \
       x>X_MAX/3+2*s and y>Y_MAX/2+s:
        farba="blue"
    else:
        farba="yellow"
 
    c.create_oval(x+r,y+r,x-r,y-r,fill=farba)
