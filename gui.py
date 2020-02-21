#!/usr/bin/python3.8

from tkinter import filedialog
from tkinter import *

def main():
    window=Tk()
    window.filename =  filedialog.askopenfilename(
        initialdir="/",
        title="Select excel file",
        filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    window.mainloop()

if __name__ == '__main__':
    main()
