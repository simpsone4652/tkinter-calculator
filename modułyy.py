from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
def zamknij():
    okno = Tk()
    okno.destroy()
    exit()

def autor():
    okienko = Tk()
    okienko.title("Moje okienko")
    okienko.geometry('350x200')

def clicked():
    messagebox.showinfo('Autor programu', 'Szymon Napiórkowski')

def notatki():
    okno=Tk()
    okno.title("Moje notatki")
    notatki = scrolledtext.ScrolledText(okno, width=40, height=10)
    notatki.grid(column=0, row=0)  # wyświtlenie okienka
    notatki.insert(INSERT, 'Miejsce na obliczenia/notatki')



##1 ##IMPORTY
from tkinter import *
import tkinter as tk
import datetime as dt
from tkinter.ttk import *
from modułyy import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb


##2 ##UTWORZENIE OKNA APLIKACJI
class oknoo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)  # wywolanie konstruktora klasy tk.Tk
        self.title("Main")  # wewnetrzny dostep do wlasnosci okna
        self.okno.geometry("800x400")
        self.okno.resizable(width=False,height=False)
        self.okno.title("WSB Matematyka")
        self.okno.configure(background="white")



##4 ##PRZYCISKI (EVENTY MYSZY)
        Label(self,text="Bryły obrotowe ", bg="white",fg="midnight blue",font="none 14 bold").grid(row=1,column=0,sticky=W)
        Button(self,text=" Walec  ",command=bryla,bg="white",fg="midnight blue",font="none 12 bold").grid(row=3,column=0,sticky=W)
        Button(self,text=" Stożek",command=bryla1,bg="white",fg="midnight blue",font="none 12 bold").grid(row=4,column=0,sticky=W)
        Button(self, text=" Kula     ", command=kula, bg="white", fg="midnight blue", font="none 12 bold").grid(
            row=2, column=0, sticky=W)



        Label(self, text="Figury płaskie ", bg="white",fg="midnight blue",font="none 14 bold").grid(row=1,column=0,sticky=E)
        Button(self,text=" Trójkąty  ",command=bryla,bg="white",fg="midnight blue",font="none 12 bold").grid(row=3,column=0,sticky=E)
        Button(self,text="Czworokąty",command=bryla1,bg="white",fg="midnight blue",font="none 12 bold").grid(row=2,column=0,sticky=E)
        Button(self,text=" Wielokąty",command=kula,bg="white",fg="midnight blue",font="none 12 bold").grid(row=4,column=0,sticky=E)


        Button(self,text="Wyjście",width=13,command=zamknij,bg="white",fg="midnight blue",font="none 10 bold").grid(row=12 ,column=0,sticky=S)
        Button(self, text='Autor', command=clicked,bg="white",fg="midnight blue",font="none 10 bold").grid(column=0, row=9)
        Button(self,text="Notatki",command=notatki,bg="white",fg="midnight blue",font="none 10 bold").grid(column=0, row=11)

    def onButton(self):
        self.kula = kula(self)  # przekazanie okna jako rodzica

    def run(self):
        self.mainloop()


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
class kula(tk.Toplevel):
    def __init__(self,parent):
        tk.Toplevel.__init__(self, parent)  # wywolanie konstruktora klasy tk.Toplevel
        self.title("Child")  # wewnetrzny dostep do wlasnosci okna


    def onButton(self):
        self.kula = kula(self)  # przekazanie okna jako rodzica

        self = self.odo4
        self.odo4.title("Kula")
        self.odo4.geometry("800x400")
        self.odo4.resizable(width=False, height=False)
        self.odo4.title("WSB Matematyka")
        self.odo4.configure(background="white")

        Label(self, text="                                            KULA", bg="white", fg="midnight blue", font="none 18 bold").grid(row=0, column=0, sticky=N)
        Label(self, text="Kula powstaje przez obrót dowolnego koła wokół jego średnicy.", bg="white", fg="midnight blue", font="none 12 bold").grid(row=2, column=0, sticky=NW)
        Label(self, text="Powierzchnię kuli nazywamy sferą.", bg="white", fg="midnight blue", font="none 12 bold").grid(row=3, column=0, sticky=NW)
        Label(self, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=4, column=0, sticky=NW)
        Label(self, text="Wzór na pole kuli:", bg="white", fg="midnight blue", font="none 12 bold").grid(row=5, column=0, sticky=NW)
        Label(self, text="P=4πr2", bg="white", fg="midnight blue", font="none 12 bold").grid(row=6, column=0, sticky=SW)
        Label(self, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=7, column=0, sticky=NW)
        Label(self, text="Wzór na objętość kuli:", bg="white", fg='midnight blue', font="none 12 bold").grid(row=10, column=0, sticky=NW)
        Label(self, text="V=43πr3", bg="white", fg="midnight blue", font="none 12 bold").grid(row=12, column=0, sticky=NW)
        Label(self, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=13, column=0, sticky=NW)
        Label(self, text="", bg="white", fg="midnight blue", font="none 12 bold").grid(row=14, column=0, sticky=NW)
        Label(self, text="Obliczanie pola kuli:", bg="white", fg="midnight blue", font="none 13 bold").grid(column=0, row=14, sticky=NW)
        a = Entry(self,width = 8).grid(column=0, row=15,sticky=NW)
        def oblicz(self):
            wynik = "Wynik  " + a.get()

        przycisk = Button(self, text="Oblicz", command=clicked).grid(column=2, row=0)

        def pole1(self):
            return 4 * math.pi * a * a
            print("Pole powierzhni kuli wynosi: ", kula.pole1(a))

        def objetosc1(self):
            return 4 / 3 * math.pi * a ** 3
            print("Pole objętości kuli wynosi", kula.objetosc1(a))





glowne = oknoo()
glowne.master.title("Glowne") # zewnetrzny dostep do wlasnosci okna
glowne.run()

tk.Label(self.master, text="Bryły obrotowe ", bg="white", fg="midnight blue", font="none 14 bold").grid(row=1, column=0,
                                                                                                        sticky=W)

tk.Button(self.master, text=" Walec  ", bg="white", fg="midnight blue", font="none 12 bold").grid(row=3, column=0,
                                                                                                  sticky=NW)

tk.Button(self.master, text=" Stożek", bg="white", fg="midnight blue", font="none 12 bold").grid(row=4,
                                                                                                 column=0,
                                                                                                 sticky=W)
tk.Button(self.master, text=" Kula     ", bg="white", fg="midnight blue", font="none 12 bold").grid(
    row=2, column=0, sticky=W)

tk.Label(self.master, text="Figury płaskie ", bg="white", fg="midnight blue", font="none 14 bold").grid(row=1, column=0,
                                                                                                        sticky=E)
tk.Button(self.master, text=" Trójkąty  ", bg="white", fg="midnight blue", font="none 12 bold").grid(row=3,
                                                                                                     column=0,
                                                                                                     sticky=E)
tk.Button(self.master, text="Czworokąty", bg="white", fg="midnight blue", font="none 12 bold").grid(row=2,
                                                                                                    column=0,
                                                                                                    sticky=E)
tk.Button(self.master, text=" Wielokąty", bg="white", fg="midnight blue", font="none 12 bold").grid(row=4,
                                                                                                    column=0,
                                                                                                    sticky=E)

tk.Button(self.master, text="Wyjście", width=13, bg="white", fg="midnight blue",
          font="none 10 bold").grid(row=12, column=0, sticky=S)
tk.Button(self, text='Autor', bg="white", fg="midnight blue", font="none 10 bold").grid(column=0,
                                                                                        row=9)
tk.Button(self.master, text="Notatki", bg="white", fg="midnight blue", font="none 10 bold").grid(column=0, row=11)

