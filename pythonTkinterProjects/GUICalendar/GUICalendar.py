from tkinter import *

import calendar

import datetime


def showCal():
    new_gui = Tk()

    new_gui.config(background="white")

    new_gui.title("CALENDER")

    new_gui.geometry("550x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    cal_year.grid(row=5, column=1, padx=20)

    new_gui.mainloop()


def showTime():
    new_gui = Tk()

    new_gui.config(background="white")

    new_gui.title("TIME")

    new_gui.geometry("250x140")

    e = datetime.datetime.now()

    current_time = e.strftime("%H:%M:%S")

    curr_time = Label(new_gui, text=current_time, font="Consolas 72 bold")

    curr_time.grid(row=5, column=1, padx=20)

    new_gui.mainloop()


def showDate():
    new_gui = Tk()

    new_gui.config(background="white")

    new_gui.title("DATE")

    new_gui.geometry("250x140")

    e = datetime.datetime.now()

    current_time = e.strftime("%d/%m/%Y")

    curr_time = Label(new_gui, text=current_time, font="Consolas 72 bold")

    curr_time.grid(row=5, column=1, padx=20)

    new_gui.mainloop()


if __name__ == '__main__':
    gui = Tk()

    gui.config(background="blue")

    gui.title("CALENDER")

    gui.geometry("700x600")

    cal = Label(gui, text="CALENDER", bg="light green", font=("times", 28, "bold"))

    year = Label(gui, text="Enter Year", bg="dark gray")

    time = Label(gui, text="CURRENT_TIME", bg="light green", font=("times", 28, "bold"))

    date = Label(gui, text="CURRENT_DATE", bg="light green", font=("times", 28, "bold"))

    year_field = Entry(gui)

    Show = Button(gui, text="Show Calendar", fg="Black",
                  bg="Red", command=showCal)

    Show_time = Button(gui, text="Show TIME", fg="Black",
                       bg="Red", command=showTime)

    Show_Date = Button(gui, text="Show DATE", fg="Black",
                       bg="Red", command=showDate)

    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    time.grid(row=1, column=2, padx=10, pady=10)

    Show_time.grid(row=4, column=2)

    date.grid(row=1, column=3, padx=10, pady=10)

    Show_Date.grid(row=4, column=3)

    Exit.grid(row=6, column=1)

    gui.mainloop()
