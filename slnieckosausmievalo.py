import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()

for i in range(500):
    x=randrange(X_MAX)
    y=randrange(Y_MAX)
    if (x<=X_MAX/2)and(y<=Y_MAX/2):
        farba="yellow"
    elif (x<=X_MAX/2)and(y>Y_MAX/2):
        farba="blue"
    elif (x>X_MAX/2)and(y<=Y_MAX/2):
        farba="red"
    elif (x>X_MAX/2)and(y>Y_MAX/2):
        farba="green"

    c.create_line(X_MAX/2,Y_MAX/2,x,y,fill=farba)
