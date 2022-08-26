from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Button Clicked!")
    myLabel.pack()

myButton = Button(root, text="Click!", command=myClick,
     bg="#FFD8A9",fg="#483838")
myButton.pack()

root.mainloop()
