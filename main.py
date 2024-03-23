import tkinter as tk
import sys
from input import *
from tkinter import *


#File IO
x = readInto(sys.argv[1])
copy = list(x)
#x = [10,20,30,40,50]
#thomas was here
window = tk.Tk()
window.geometry("1366x768")
greeting = tk.Label(text="Algorithm Visualizer")
greeting.pack()
canvas = Canvas(window, width=1366,height=768,bg="teal")
canvas.pack()
def bubble_sort(arr, canvas):
    VisualizeArray(arr, canvas)
    size = len(arr)
    for num in range(size - 1):
        for i in range(0, size - num - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                VisualizeArray(arr, canvas)
                window.update_idletasks()
                window.after(10)
    copy = list(x)
BubButton = Button(canvas, text="Bubble Sort", command=lambda:window.after(100,bubble_sort,copy, canvas))
BubButton.place(x=50, y=50)
Reset = Button(canvas, text="Reset", command=lambda:window.after(100,VisualizeArray,x, canvas))
Reset.place(x=125, y=50)


   
def VisualizeArray(arr, canvas):
    window.update_idletasks
    canvas.delete("all")
    width = 1366/len(arr)
    count = 0;
    for element in arr:
        rect = canvas.create_rectangle(0 + (width*count),500 - (3*element),width*(count+1),500, fill='black')
        count = count + 1

#VisualizeArray(x)   
window.mainloop()    




