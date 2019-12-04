import tkinter
from random import randrange,randint
X_MAX, Y_MAX=800,600
c=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="black")
c.pack()

r=50
dx=2
dy=2
x,y = randint(r,X_MAX-r),randint(r,Y_MAX-r)
def saver(x,y,r):
    c.create_rectangle(x-r,y-r,x+r,y+r,fill="orange")
    c.create_text(x,y, text="DVD",font="Arial 30",fill="white")
while True:
    c.delete("all")
    saver(x,y,r)
    x+=dx
    y+=dy
    if y>=Y_MAX-r or y<=r:
        dy*=-1
    if x<=r or x>=X_MAX-r:
        dx*=-1
    
    c.update()
    c.after(1)

tkinter.mainloop()


