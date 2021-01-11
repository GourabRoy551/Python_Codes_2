import tkinter
from tkinter import *

win = Tk()


def pr():
    print('hi')


win.geometry("400x400")
b = Button(win, text='button', command=pr)
b.place(x=100, y=200)

win.mainloop()
