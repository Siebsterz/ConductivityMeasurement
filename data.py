from tkinter import *

from tkinter import messagebox

top = Tk()


def getVoltage():
    text = E.get()
    print(text)
    if text.isdigit():
        print("No number")
    else:
        print("kaka")

B = Button(top, text ="Hello", command = getVoltage)
E = Entry()
B.pack()
E.pack()
top.mainloop()