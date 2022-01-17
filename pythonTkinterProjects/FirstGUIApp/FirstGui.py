# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Tkinter")
# Set geometry (widthxheight)
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item2 = Menu(menu)
item.add_command(label='New')
item.add_command(label='open')
item.add_command(label='settings')
menu.add_cascade(label='File', menu=item)
menu.add_cascade(label='EDIT', menu=item2)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text="This is the TKINTER enter YOUR NAME")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)


# function to display text when
# button is clicked
def clicked():
    va = txt.get()
    res = "YOUR NAME is ::" + va.upper()
    lbl.configure(text=res)


# button widget with red color text
# inside
btn = Button(root, text="Click me",
             fg="blue", command=clicked)
# set Button grid
btn.grid(column=2, row=0)

# all widgets will be here
# Execute Tkinter
root.mainloop()
