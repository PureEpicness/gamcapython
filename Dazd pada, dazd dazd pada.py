import tkinter
import random
Y=400
X=600
c=tkinter.Canvas(width=X,height=Y,bg="white")
c.pack()


   
while True:
    c.delete("all")
    for i in range(100):
        x,y=random.randrange(X),random.randrange(Y)
        c.create_oval(x-5,y-5,x+5,y+5,fill="light blue")
    c.update()
    c.after(100)

