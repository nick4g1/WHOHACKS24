import tkinter as tk
import sys
from input import *
from tkinter import *


#File IO
x = readInto(sys.argv[1])

#x = [10,20,30,40,50]
#thomas was here
window = tk.Tk()
canvas = Canvas(window, width=500,height=500)
canvas.pack()
def VisualizeArray(x):
    count = 0;
    for element in x:
        rect = canvas.create_rectangle(0 + (20*count),100 - element,20+(20*count),100, fill='black')
        count = count + 1
window.geometry("1000x600")
greeting = tk.Label(text="Algorithm Visualizer")
greeting.pack()
VisualizeArray(x)
window.mainloop()


