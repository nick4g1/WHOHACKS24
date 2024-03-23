import tkinter as tk
import sys
from input import *
from tkinter import *


#File IO
global x
x = readInto(sys.argv[1])
#print(x)
global original_x, original_x_keys, original_x_values
original_x = dict(x)
original_x_keys = list(x.keys())
original_x_values = list(x.values())
global after_id
after_id = None
#thomas was here
window = tk.Tk()
window.geometry("1366x768")
greeting = tk.Label(text="Algorithm Visualizer")
greeting.pack()
canvas = Canvas(window, width=1366,height=768,bg="teal")
canvas.pack()
#start methods for after_id
def start_bubble_sort(keyArr, valArr, canvas):
    after_id = window.after(100, bubble_sort, keyArr, valArr, canvas)
def start_selection_sort(keyArr, valArr, canvas):
    after_id = window.after(100, selection_sort, keyArr, valArr, canvas)
def start_reset(canvas):
    reset(canvas)
#sorts the key and value arrays
def bubble_sort(keyArr, valArr, canvas):
    VisualizeArray(valArr, canvas)
    size = len(valArr)
    for num in range(size - 1):
        for i in range(0, size - num - 1):
            if keyArr[i] > keyArr[i + 1]:
                keyArr[i], keyArr[i + 1] = keyArr[i + 1], keyArr[i]
                valArr[i], valArr[i + 1] = valArr[i + 1], valArr[i]
                VisualizeArray(valArr, canvas)
                window.update_idletasks()
                window.after(1)
#resets canvas
def reset(canvas):
    if after_id:
        window.after_cancel(after_id)
    original_x_keys = list(x.keys())
    original_x_values = list(x.values())
    VisualizeArray(original_x_values,canvas)
#buttons
BubButton = Button(canvas, text="Bubble Sort", command=lambda: start_bubble_sort(original_x_keys, original_x_values, canvas))
BubButton.place(x=50, y=50)
Reset = Button(canvas, text="Reset", command=lambda:window.after(100,reset, canvas))
Reset.place(x=125, y=50)
# sorts key and val arrays with selection sort
def selection_sort(keyArr, valArr, canvas):
    VisualizeArray(valArr, canvas)
    size = len(valArr)
    for num in range(size):
        min = num
        for i in range(num + 1, size):
            if keyArr[i] < keyArr[min]:
                min = i
        keyArr[num], keyArr[min] = keyArr[min], keyArr[num]
        valArr[num], valArr[min] = valArr[min], valArr[num]
        VisualizeArray(valArr, canvas)
        window.update_idletasks()
        window.after(1)

#select button
SelButton = Button(canvas, text="Selection Sort", command=lambda: start_selection_sort(original_x_keys, original_x_values, canvas))
SelButton.place(x=170, y=50)
   
#visualizes array as rectangles
def VisualizeArray(arr, canvas):
    canvas.delete("all")
    width = 1366/len(arr)
    count = 0
    #print(arr)
    for val in arr:
        color = hex(val)
        color = color[2:8]
        color = "#" + color
        #print(color)
        rect = canvas.create_rectangle(0 + (width*count),500 - (100),width*(count+1),500, fill=color)
        window.update_idletasks
        count = count + 1

#VisualizeArray(x)   
window.mainloop()    




