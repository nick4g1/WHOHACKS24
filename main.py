import tkinter as tk
import sys
import math
from input import *
from tkinter import *
from tkinter import filedialog
from image import convertImage
import os

#File IO
global x
x = readInto(sys.argv[1])
#v1 = IntVar()
#print(x)
global original_x
original_x = list(x)
after_id = None
#thomas was here
window = tk.Tk()
window.geometry("1366x768")
greeting = tk.Label(text="Algorithm Visualizer")
greeting.pack()
canvas = Canvas(window, width=1366,height=768,bg="teal")
canvas.pack()
#start methods for after_id
def start_bubble_sort(arr, canvas):
    global after_id
    after_id = window.after(100, bubble_sort, arr, canvas)
def start_selection_sort(arr, canvas):
    global after_id
    after_id = window.after(100, selection_sort, arr, canvas)
def start_reset(canvas):
    reset(canvas)
#sorts the key and value arrays
def bubble_sort(arr, canvas):
    reset(canvas)
    VisualizeArray(arr, canvas)
    size = len(arr)
    for num in range(size - 1):
        for i in range(0, size - num - 1):
            if arr[i].getKey() > arr[i + 1].getKey():
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                VisualizeArray(arr, canvas)
                window.update_idletasks()
                window.after(1)
#resets canvas
def reset(canvas):
    global after_id, original_x
    if after_id:
        window.after_cancel(after_id)
        after_id = None
    convertImage(fileF, scale.get())
    x = readInto(sys.argv[1])
    original_x = list(x)
    VisualizeArray(original_x,canvas)
#buttons
BubButton = Button(canvas, text="Bubble Sort", command=lambda: start_bubble_sort(original_x, canvas))
BubButton.place(x=50, y=50)
Reset = Button(canvas, text="Reset", command=lambda: start_reset(canvas))
Reset.place(x=280, y=50)

#uploading a file
def upload_file():
    global fileF
    fileF = filedialog.askopenfilename(title="Choose File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if fileF:
        fileF = os.path.basename(fileF)
        convertImage(fileF, scale.get())
        x = readInto(sys.argv[1])
        original_x = list(x)
uploadButton = tk.Button(canvas, text="Upload File", command=upload_file)
uploadButton.place(x=400, y=50)

scale = Scale( canvas, from_ = 1, to=1300, orient = HORIZONTAL )
scale.place(x=500, y=50)


# sorts key and val arrays with selection sort
def selection_sort(arr, canvas):
    reset(canvas)
    VisualizeArray(arr, canvas)
    size = len(arr)
    for num in range(size):
        min = num
        for i in range(num + 1, size):
            if arr[i].getKey() < arr[min].getKey():
                min = i
        arr[num], arr[min] = arr[min], arr[num]
        VisualizeArray(arr, canvas)
        window.update_idletasks()
        window.after(10)

#select button
SelButton = Button(canvas, text="Selection Sort", command=lambda: start_selection_sort(original_x, canvas))
SelButton.place(x=125, y=50)
def partition(arr, low, high, canvas):
    VisualizeArray(arr, canvas)
    pivot = arr[high].getKey()
    i = low - 1
    for j in range(low, high):
        if arr[j].getKey() <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            VisualizeArray(arr, canvas)
            window.update_idletasks()
            window.after(1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    VisualizeArray(arr, canvas)
    window.update_idletasks()
    window.after(1)
    return i + 1
 
 
def quick_sort(arr, low, high, canvas):
    reset(canvas)
    VisualizeArray(arr, canvas)
    if low < high:
        pi = partition(arr, low, high, canvas)
        quick_sort(arr, low, pi - 1, canvas)
        quick_sort(arr, pi + 1, high, canvas)
        
QuickButton = Button(canvas, text="Quick Sort", command=lambda:window.after(100,quick_sort,original_x, 0, len(original_x) - 1, canvas))
QuickButton.place(x=210, y=50)
   
#visualizes array as rectangles
def VisualizeArray(arr, canvas):
    canvas.delete("all")
    canvas.delete("all")
    size = len(arr)
    width = round(math.sqrt(size))
    for i in range(width):
        for j in range(width):
            index = i * width + j
            if index < size:
                color = hex(arr[index].getValue())
                color = color[2:].zfill(6)  # Pad with zeros if needed
                color = '#' + color
                canvas.create_rectangle(200 + (20 * j), 200 + (i * 20), 200 + 20 * (j + 1), 200 + (20 * (i + 1)), fill=color)
            window.update_idletasks

    #print(arr)
    #for val in arr:
     #   color = hex(val)
      #  color = color[2:]
       # color = format(val, '06x')
        #color = "#" + color
        #print(color)
        #rect = canvas.create_rectangle(0 + (widthcount),500 - (100),width(count+1),500, fill=color)
        #window.update_idletasks
        #count = count + 1

#VisualizeArray(x)   
window.mainloop()    




