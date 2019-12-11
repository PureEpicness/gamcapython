import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()


r=5
for i in range(1000):
    x=randrange(X_MAX)
    y=randrange(Y_MAX)
    if (x<=X_MAX/2)and(y<=Y_MAX/2):
        farba="green"
    elif (x<=X_MAX/2)and(y>=Y_MAX/2):
        farba="yellow"
    elif (x>=X_MAX/2)and(y<=Y_MAX/2):
        farba="orange"
    elif (x>=X_MAX/2)and(y>=Y_MAX/2):
        farba="red"
    c.create_oval(x-r,y-r,x+r,y+r,fill=farba)
