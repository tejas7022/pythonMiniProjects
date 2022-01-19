from tkinter import *

def compound_interest():
    principle = int(txt.get())

    rate = int(txt1.get())

    time = int(txt2.get())

    CI = principle * (pow((1 + rate / 100), time))

    txt3.insert(10, CI)
def clear():
    txt.delete(0,END)
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)

    txt.focus_set()
if __name__ == "__main__":

    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Compound Interest Calculator")

    # set the configuration of GUI window
    gui.geometry("400x250")

    lbl = Label(gui, text="Principle Amount(Rs):", bg='red')
    lbl.grid(column=1, row=3, padx=10, pady=10)

    txt = Entry(gui, width=40)
    txt.grid(column=2, row=3, padx=10, pady=10)

    lbl1 = Label(gui, text="Rate(%):", bg='red')
    lbl1.grid(column=1, row=4, padx=10, pady=10)

    txt1 = Entry(gui, width=40)
    txt1.grid(column=2, row=4, padx=10, pady=10)

    lbl2 = Label(gui, text="Time(Year):", bg='red')
    lbl2.grid(column=1, row=5, padx=10, pady=10)

    txt2 = Entry(gui, width=40)
    txt2.grid(column=2, row=5, padx=10, pady=10)

    btn = Button(gui, text="SUBMIT",bg='red',
                 fg="blue", command=compound_interest)
    # set Button grid
    btn.grid(column=2, row=6)

    lbl3 = Label(gui, text="Compund Intrest:", bg='red')
    lbl3.grid(column=1, row=7, padx=10, pady=10)

    txt3 = Entry(gui, width=40)
    txt3.grid(column=2, row=7, padx=10, pady=10)

    btn = Button(gui, text="CLEAR", bg='red',
                 fg="blue", command=clear)
    # set Button grid
    btn.grid(column=2, row=8)

    gui.mainloop()
