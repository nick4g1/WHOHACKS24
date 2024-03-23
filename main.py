import tkinter as tk
import sys
from input import *
from tkinter import *


#File IO
x = readInto(sys.argv[1])

#x = [10,20,30,40,50]
#thomas was here
window = tk.Tk()
window.geometry("1366x768")
greeting = tk.Label(text="Algorithm Visualizer")
greeting.pack()
canvas = Canvas(window, width=1366,height=768,bg="teal")
canvas.pack()
def VisualizeArray(x):
    canvas.delete("all")
    width = 1366/len(x)
    count = 0;
    for element in x:
        rect = canvas.create_rectangle(0 + (width*count),500 - (3*element),width*(count+1),500, fill='black')
        count = count + 1
VisualizeArray(x)
window.mainloop()


