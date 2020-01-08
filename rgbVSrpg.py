import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX)
c.pack()

r,g,b=randint(0,255),randint(0,255),randint(0,255)
j=1
k=1
l=1
while True:
    farba=f'#{r:02x}{g:02x}{b:02x}'
    r-=j
    g-=k
    b-=l
    if r == 0 or r == 255:
        j =- j
    if g == 0 or g == 255:
        k =- k
    if b == 0 or b == 255:
        l =- l

    
    c.create_rectangle(0,0,X_MAX,Y_MAX,fill=farba)
    print (r,g,b)
    c.update()
    c.after(1)
