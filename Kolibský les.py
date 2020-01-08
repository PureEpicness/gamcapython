import tkinter
import random
canvas=tkinter.Canvas(height=400,width=800)
canvas.pack()
def strom(x,y,r):
    canvas.create_rectangle(x-5,y,x+5,y+60,fill="brown")
    canvas.create_oval(x-r*0.5,y-r*0.5,x+r*0.5,y+r*0.5,fill="green")
def trava(x,y,p):
    for i in range(p):
        canvas.create_line(x,y,x-random.randint(5,20)+random.randint(5,20),y-random.randint(5,20),width=random.randint(1,3),fill="green")

for i in range(10):
    strom(random.randint(50,750),random.randint(50,340),random.randint(20,50))
for i in range(20):
    trava(random.randint(50,750),random.randint(50,340),random.randint(3,10))
