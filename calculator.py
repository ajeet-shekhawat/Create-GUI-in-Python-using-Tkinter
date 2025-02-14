from cgitb import text
from ctypes import alignment
from stat import FILE_ATTRIBUTE_NORMAL
import string
from tkinter import *
from webbrowser import get

root = Tk()
root.title("Calculator")
root.configure(bg="#262626")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def only_numbers(char):
    return isfloat(char)

validation = root.register(only_numbers)

# # entry field 0
e0 = Entry(root, font=('calibre',10, 'normal'),width=42, bg="#262626", fg="white", borderwidth=0, justify=RIGHT)
e0.grid(row=0,column=0, columnspan=4, padx=2, pady=3)
e0.insert(0,"")

# entry field 1
e = Entry(root, validate='key', validatecommand=(validation, '%S'),
        font=('calibre',20, 'bold'),width=20, bg="#262626", fg="white", borderwidth=0, justify=RIGHT)
e.grid(row=1,column=0, columnspan=4, padx=2, pady=3)
e.insert(0, 0)
e.focus()

# convert number into int or float
def numFloatInt(eVal):
    try:
        current = int(eVal)
    except:
        current = float(eVal)
    return current

# function to input numbers to entry box
def button_click(number):
    global math
    math=""
    current = e.get()
    e.delete(0, END)
    if current != '0':
        e.insert(0, str(current) + str(number))
    elif number == ".":
        e.insert(0, str(current) + str(number))
    else:
        e.insert(0,number)

# Function to clear values from entry box
def btnClearAll():
    e.delete(0,END)
    e0.delete(0,END)
    e.insert(0,0)

# Function to clear single values from entry box
def btnClear():
    e.delete(e.index("end")-1)

# Function for Positive and negative sign
def btnPosNeg():

    current = numFloatInt(e.get())
    
    if current > 0:
        e.insert(0,"-")
    elif current < 0:
        e.delete(0)

# Convert to percentage
def btnPer():
    eVal = numFloatInt(e.get())
    eVal = eVal / 100
    e.delete(0,END)
    e.insert(0,eVal)

def eString():
    estr = e0.get()
    if estr == "":
        return ""
    else:
        estr[:-1]

# Function for addition
def btnAdd():
    global f_num
    global math
    math = "addition"
    f_num = numFloatInt(e.get())
    # print(True if e0.get()=="" else False)
    # e0.insert(0, (str(f_num)+"+") if e0.get()=="" else (eString + "+" + str(f_num)+"+")) 
    e0.insert(0, str(f_num)+"+")
    # e.delete(0,END)

# Function for subtraction
def btnSub():
    global f_num
    global math
    math = "subtraction"
    f_num = numFloatInt(e.get())
    e0.insert(0,str(f_num)+"-")
    e.delete(0,END)

# Function for multiply
def btnMultiply():
    global f_num
    global math
    math = "multiplication"
    f_num = numFloatInt(e.get())
    e0.insert(0,str(f_num)+"x")
    e.delete(0,END)

# Function for divide
def btnDivide():
    global f_num
    global math
    math = "division"
    f_num = numFloatInt(e.get())
    e0.insert(0,str(f_num)+"/")
    e.delete(0,END)

# Function for Equal
def btnEqual():
    s_num = numFloatInt(e.get())
    e.delete(0, END)
    e0.delete(0,END)

    if math=="addition":
        e0.insert(0,str(f_num)+"+"+str(s_num)+"=")
        e.insert(0,f_num + s_num)
    
    if math=="subtraction":
        e0.insert(0,str(f_num)+"-"+str(s_num)+"=")
        e.insert(0,f_num - s_num)
    
    if math=="multiplication":
        e0.insert(0,str(f_num)+"x"+str(s_num)+"=")
        e.insert(0,f_num * s_num)

    if math=="division":
        e0.insert(0,str(f_num)+"/"+str(s_num)+"=")
        res = f_num / s_num
        if f_num % s_num == 0:
            e.insert(0,numFloatInt(res))
        else:
            e.insert(0,res)

# Button properties
fontbutton = ('MS PGothic',10, 'bold')
pdxBtn = 2
pdyBtn = 6
btnWidth = 8
bthHeight = 2
fgBtn = "white"
bgBtn = "#404040"
gbNumBtn = "#6B6B6B"

# Calculator Buttons
# Row 1 buttons
button_percent = Button(root, text="%", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnPer)
button_clear = Button(root, text="C", width=btnWidth, height=bthHeight, font=fontbutton,fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnClearAll)
button_delete = Button(root, text="del", width=btnWidth, height=bthHeight, font=fontbutton,fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnClear)
button_divide = Button(root, text="/", width=btnWidth, height=bthHeight, font=fontbutton,fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnDivide)

# Row 2 buttons
button_7 = Button(root, text="7", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(7))
button_8 = Button(root, text="8", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(8))
button_9 = Button(root, text="9", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(9))
button_multiply = Button(root, text="x", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnMultiply)

# Row 3 buttons
button_4 = Button(root, text="4", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(4))
button_5 = Button(root, text="5", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(5))
button_6 = Button(root, text="6", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(6))
button_subtract = Button(root, text="−", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnSub)

# Row 4 buttons 
button_1 = Button(root, text="1", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(1))
button_2 = Button(root, text="2", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(2))
button_3 = Button(root, text="3", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(3))
button_addition = Button(root, text="+", width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=bgBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnAdd)

# Row 5 buttons
button_posneg = Button(root, text="+/-",  width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnPosNeg)
button_0 = Button(root, text="0",  width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click(0))
button_decimal = Button(root, text=".",  width=btnWidth, height=bthHeight, font=fontbutton, fg=fgBtn, bg=gbNumBtn, padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=lambda:button_click("."))
button_equal = Button(root, text="=",  width=btnWidth, height=bthHeight, font=fontbutton, fg="#293462", bg="#FEDB39", padx=pdxBtn, pady=pdyBtn, borderwidth=0, command=btnEqual)

# Show Buttons on Screen
# Row 2 button
sbtnpadx = 2
sbtnpady = 2
button_percent.grid(row=2, column=0, padx=sbtnpadx, pady=sbtnpady)
button_clear.grid(row=2, column=1, padx=sbtnpadx, pady=sbtnpady)
button_delete.grid(row=2, column=2, padx=sbtnpadx, pady=sbtnpady)
button_divide.grid(row=2, column=3, padx=sbtnpadx, pady=sbtnpady)

# Row 3 button
button_7.grid(row=3, column=0, padx=sbtnpadx, pady=sbtnpady)
button_8.grid(row=3, column=1, padx=sbtnpadx, pady=sbtnpady)
button_9.grid(row=3, column=2, padx=sbtnpadx, pady=sbtnpady)
button_multiply.grid(row=3, column=3, padx=sbtnpadx, pady=sbtnpady)

# Row 4 button
button_4.grid(row=4, column=0, padx=sbtnpadx, pady=sbtnpady)
button_5.grid(row=4, column=1, padx=sbtnpadx, pady=sbtnpady)
button_6.grid(row=4, column=2, padx=sbtnpadx, pady=sbtnpady)
button_subtract.grid(row=4, column=3, padx=sbtnpadx, pady=sbtnpady)

# Row 5 button
button_1.grid(row=5, column=0, padx=sbtnpadx, pady=sbtnpady)
button_2.grid(row=5, column=1, padx=sbtnpadx, pady=sbtnpady)
button_3.grid(row=5, column=2, padx=sbtnpadx, pady=sbtnpady)
button_addition.grid(row=5, column=3, padx=sbtnpadx, pady=sbtnpady)

# Row 6 button
button_posneg.grid(row=6, column=0, padx=sbtnpadx, pady=sbtnpady)
button_0.grid(row=6, column=1, padx=sbtnpadx, pady=sbtnpady)
button_decimal.grid(row=6, column=2, padx=sbtnpadx, pady=sbtnpady)
button_equal.grid(row=6, column=3, padx=sbtnpadx, pady=sbtnpady)

root.mainloop()