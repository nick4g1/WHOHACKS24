import tkinter as tk
import sys

#File IO
input = open(sys.argv[1], "r", encoding="utf-8").read()


#thomas was here
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
window.mainloop()

