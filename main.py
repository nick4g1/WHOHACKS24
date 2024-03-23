import tkinter as tk
import sys
from input import *


#File IO
readInto(sys.argv[1])


#thomas was here
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
window.mainloop()

