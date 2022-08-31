# import tkinter as tk

# class window2:
#     def __init__(self, master1):
#         self.panel2 = tk.Frame(master1)
#         self.panel2.grid()
#         self.button2 = tk.Button(self.panel2, text = "Quit", command = self.panel2.quit)
#         self.button2.grid()
#         vcmd = (master1.register(self.validate),
#                 '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
#         self.text1 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)
#         self.text1.grid()
#         self.text1.focus()

#     def validate(self, action, index, value_if_allowed,
#                        prior_value, text, validation_type, trigger_type, widget_name):
#         if value_if_allowed:
#             try:
#                 float(value_if_allowed)
#                 return True
#             except ValueError:
#                 return False
#         else:
#             return False

# root1 = tk.Tk()
# window2(root1)
# root1.mainloop()
from select import select
from tkinter import *
from unittest import case
root = Tk()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

math = "addition"
# function to validate mark entry
def validate(action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.-+x/':
        sNum = (prior_value.split('+')[1] if '+' in prior_value  else  "") + text
        try:
            if text == '-' and index == '0':
                return True
            elif text == '-' and index != '0' and prior_value.count("-")<2:
                return True
            elif text in '+x/' and text not in prior_value:
                return True 
            elif isfloat(sNum):
                return True
            else:
                float(value_if_allowed)
                return True

            # elif (math == "addition" and text == '+' and isfloat(prior_value)):
            #     print(prior_value)
            #     return True
            # elif (text in '0123456789.' and isfloat(sNum) and text not in sNum ):
            #     return True
            # elif isfloat(value_if_allowed):
            #     return True
            # elif isfloat(sNum):
            #     return True
            # float(text)
            # return True


        except ValueError:
            return False
    else:
        return False

vcmd = (root.register(validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

#text box to enter marks
e=Entry(root,validate="key", validatecommand=vcmd)
e.pack()
e.focus()
root.mainloop()