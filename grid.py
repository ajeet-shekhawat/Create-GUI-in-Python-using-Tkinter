from tkinter import *
from turtle import bgcolor

root = Tk()
# root.configure(bg="black")
root['bg']="red"

#Creating a Lael Widget
myLabel1 = Label(root,text="Hello World!",bg="red")
myLabel2 = Label(root,text="My Name is Ajeet S Shekhawat",bg="red")

#Showing on screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()