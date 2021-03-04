from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import pandas as pd
import numpy as np
from pyodbc import ProgrammingError
import os

wnd=Tk()

wnd.geometry('370x100+450+300')

wnd.title('Login')

cpath=os.getcwd()
cpath=cpath+'\TMMAinfo.txt'

f= open(cpath)
lines=f.read().splitlines()

newlines=[]

for i in range(len(lines)):
    newlines.append(str(lines[i]))

global Pwd

Pwd=newlines[4].split("=")[1]

e = Entry(wnd,show='*',width=20,font=('Arial',16))
e.grid(row=0,column=1)

lb1=Label(wnd,text='Password: ',height=4).grid(row=0,column=0)

e.focus_set()

def callback():
    pwd=e.get()
    if pwd != Pwd:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='!Wrong Password!')
    else:
        wnd.destroy()
        import TMMA_program



btn=Button(wnd,text='log in',width=8,command=callback)
btn.grid(column=1,sticky='w')


wnd.mainloop()
