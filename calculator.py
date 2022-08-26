from ctypes import alignment
from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(bg="black")

e = Entry(root, font=("22"),width=25, bg="black", fg="white", 
    borderwidth=0, justify=RIGHT)
    
e.grid(row=0,column=0, columnspan=2, padx=10, pady=10)

e.insert(0, 0)





root.mainloop()