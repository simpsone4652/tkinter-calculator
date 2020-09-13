from tkinter import *
import tkinter as tk
import datetime as dt
from tkinter.ttk import *
from modułyy import *
from bryły import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
import math

##=================WALEC===============
def bryla():
    okno2 = Tk()
    okno2.title("Walec")
    okno2.geometry("800x400")


    Label(okno2, text=
    'Walec powstaje w wyniku obrotu dowolnego prostokąta wokół prostej zawierającej jeden z jego boków.\n'
    'Powyższy walec powstał przez obrót prostokąta SBCE wokół prostej SE.\n'
    'Przekrojem osiowym walca jest prostokąt ABCD.\n'
    'Podstawą walca jest koło.\n'
    'Wzór na pole podstawy walca:\n'
    'Pp=πr2\n'
    'Wzór na pole powierzchni bocznej walca:\n'
    'Pb=2πrh\n'
    'Wzór na pole powierzchni całkowitej walca\n'
    'Pc=2Pp+Pb=2πr2+2πrh=2πr(r+h)\n'
    'Wzór na objętość walca:\n'
    'V=Pp⋅h=πr2h', bg="black", fg="white", font="none 11 bold").grid(row=2,column=0,sticky=W)





##===================STOŻEK===================





def bryla1():
    okno3 = Tk()
    okno3.title("Stożek")
    okno3.geometry("800x400")
    Label(okno3, text=
    'Stożek powstaje przez obrót trójkąta prostokątnego wokół jednej z przyprostokątnych.\n'
    'Przyprostokątna ta tworzy wysokość stożka, a druga przyprostokątna staje się promieniem podstawy.\n'
    'Przeciwprostokątna trójkąta prostokątnego staje się tworzącą stożka.\n'
    'Powyższy stożek powstał przez obrót trójkąta prostokątnego SBC wokół prostej SC.\n'
    'Przekrojem osiowym stożka jest trójkąt równoramienny ABC.\n'
    'Podstawą stożka jest koło.\n'
    'Wzór na pole podstawy stożka:\n'
    'Pp=πr2\n'
    'Wzór na pole powierzchni bocznej stożka:\n'
    'Pb=πrl\n'
    'Wzór na pole powierzchni całkowitej stożka:\n'
    'Pc=πr2+πrl=πr(r+l)\n'
    'Wzór na objętość stożka:\n'
    'V=13Pp⋅h=πr2h3\n', bg="black", fg="white", font="none 11 bold").grid(row=1, column=0, sticky=W)



##================KULA===============

def kula():
        okno4 = Tk()
        okno4.title("Kula")
        okno4.geometry("800x400")
        okno4.resizable(width=False, height=False)
        okno4.title("WSB Matematyka")
        okno4.configure(background="white")

        Label(okno4, text="                                            KULA", bg="white", fg="midnight blue",font="none 18 bold").grid(row=0, column=0, sticky=N)
        Label(okno4, text="Kula powstaje przez obrót dowolnego koła wokół jego średnicy.", bg="white",g="midnight blue", font="none 12 bold").grid(row=2, column=0, sticky=NW)
        Label(okno4, text="Powierzchnię kuli nazywamy sferą.", bg="white", fg="midnight blue",font="none 12 bold").grid(row=3, column=0, sticky=NW)
        Label(okno4, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=4, column=0, sticky=NW)
        Label(okno4, text="Wzór na pole kuli:", bg="white", fg="midnight blue", font="none 12 bold").grid(row=5,column=0,sticky=NW)
        Label(okno4, text="P=4πr2", bg="white", fg="midnight blue", font="none 12 bold").grid(row=6, column=0,sticky=SW)
        Label(okno4, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=7, column=0, sticky=NW)
        Label(okno4, text="Wzór na objętość kuli:", bg="white", fg="midnight blue", font="none 12 bold").grid(row=10,column=0,sticky=NW)
        Label(okno4, text="V=43πr3", bg="white", fg="midnight blue", font="none 12 bold").grid(row=12, column=0, sticky=NW)
        Label(okno4, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=13, column=0, sticky=NW)
        Label(okno4, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=14, column=0, sticky=NW)
        Label(okno4, text="Obliczanie pola kuli:", bg="white", fg="midnight blue", font="none 13 bold").grid(column=0,row=14,sticky=NW)


