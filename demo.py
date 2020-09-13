import tkinter as tk
from tkinter import *
import math
from tkinter import messagebox
from tkinter import scrolledtext


#----------------------------------------------------------------------

class Main():  #stworzenie klasy rodzica

    def __init__(self):
        self.master = tk.Tk() # bezposrednie tworzenie okna
        self.master.geometry("800x620")        #wielkosc okna
        self.master.resizable(width=True, height=True)     #ustawienia okna
        self.master.title("WSB Matematyka")                #tytuł
        self.master.configure(background="white smoke")   #tlo okna

        self.master.img1 = img1 = tk.PhotoImage(file="walec.png")      #IMPORT ZDJEC DO PRZYCISKÓW
        self.master.img2 = img2 = tk.PhotoImage(file="stozek.png")
        self.master.img3 = img3 = tk.PhotoImage(file="szescian.png")
        self.master.img4 = img4 = tk.PhotoImage(file="prostopadloscian.png")
        self.master.img5 = img5 = tk.PhotoImage(file="graniastoslup.png")
        self.master.img6 = img6 = tk.PhotoImage(file="ostroslup.png")
        self.master.img7 = img7 = tk.PhotoImage(file="kula.png")
        self.master.img8 = img8 = tk.PhotoImage(file="quit.png")
        self.master.img9 = img9 = tk.PhotoImage(file="kolo.png")
        self.master.img10 = img10 = tk.PhotoImage(file="kwadrat.png")
        self.master.img11 = img11 = tk.PhotoImage(file="prostokat.png")
        self.master.img12 = img12 = tk.PhotoImage(file="romb.png")
        self.master.img13 = img13 = tk.PhotoImage(file="rownoleglobok.png")
        self.master.img14 = img14 = tk.PhotoImage(file="trapez.png")
        self.master.img15 = img15 = tk.PhotoImage(file="trojkat.png")
        self.master.img16 = img16 = tk.PhotoImage(file="trojkatprostokatny.png")
        self.master.img17 = img17 = tk.PhotoImage(file="wielokat.png")
        self.master.img18 = img18 = tk.PhotoImage(file="notes1.png")





         #STWORZENIE GUZIKOW I LABELI MENU
        tk.Label(self.master, text="Pola i objętości", fg="DeepSkyBlue2", font="Times 12 bold").grid(row=0, column=0)
        tk.Button(self.master, text="Kula", image = img7 , command=self.onButton).grid(row=4,column=0,sticky=NW)
        tk.Button(self.master,text=" Walec  ",image=img1,command = self.onButton2).grid(row=4,column=1,sticky=NW)
        tk.Button(self.master, text=" Stożek",image=img2,command = self.onButton3).grid(row=4, column=2,sticky=NW)
        tk.Button(self.master, text=" Sześcian", image=img3).grid(row=4, column=3, sticky=NW)
        tk.Button(self.master, text=" Prostopadloscian", image=img4).grid(row=4, column=4, sticky=NW)
        tk.Button(self.master, text=" Graniastoslup", image=img5).grid(row=4, column=5,sticky=NW)
        tk.Button(self.master, text=" Ostroslup", image=img6).grid(row=4, column=6,sticky=NW)

        tk.Label(self.master,text="Pola figur", fg="DeepSkyBlue2", font="Times 12 bold").grid(row=6, column=0,sticky=NW)
        tk.Button(self.master, text=" Trójkąt  ",image=img15).grid(row=8,column=0,sticky=NW)
        tk.Button(self.master, text="Kwadrat",image=img10).grid(row=8,column=1,sticky=NW)
        tk.Button(self.master, text=" Wielokąt formeny",image=img17).grid(row=8,column=2,sticky=NW)
        tk.Button(self.master, text="Koło", image=img9).grid(row=8, column=3, sticky=NW)
        tk.Button(self.master, text="Prostokąt", image=img11).grid(row=8, column=4, sticky=NW)
        tk.Button(self.master, text="Romb", image=img12).grid(row=8, column=5, sticky=NW)
        tk.Button(self.master, text="Równoległobok", image=img13).grid(row=8, column=6, sticky=NW)
        tk.Button(self.master, text="Trapez", image=img14).grid(row=9, column=0, sticky=NW)
        tk.Button(self.master, text="Trojkat prostokatny", image=img16).grid(row=9, column=1, sticky=NW)
        tk.Label(self.master).grid(row=10,column=8,sticky=SE)
        tk.Label(self.master).grid(row=11, column=8, sticky=SE)
        tk.Label(self.master).grid(row=12, column=8, sticky=SE)
        tk.Label(self.master).grid(row=13, column=8, sticky=SE)
        tk.Label(self.master).grid(row=14, column=8, sticky=SE)
        tk.Label(self.master).grid(row=15, column=8, sticky=SE)
        tk.Label(self.master).grid(row=16, column=8, sticky=SE)
        notatki2 = tk.Button(self.master, text="Notatki", image=img18, command=self.notatki)
        notatki2.grid(row=16, column=8, sticky=SE)
        tk.Button(self.master,image=img8,command=self.zamknij).grid(row=19, column=8 ,sticky=SE)
        #tk.Button(self.master, text='Autor', command=self.clicked).grid(column=40,row=70,sticky=E)


    def zamknij(self):
        self.master = tk.Tk()    #funkcja do zamkniecia aplikacji
        self.master.destroy()
        exit()



    def clicked(self):
        self.master = messagebox.showinfo('Autor programu', 'Szymon Napiórkowski')   #funkcja do wyswietlania autora

    def notatki(self):
        self.master = tk.Tk()    #funkcja w 2 oknie wlacza notatki
        self.master.title("Moje notatki")
        self.master.notatki = scrolledtext.ScrolledText(self.master, width=40, height=10)
        self.master.notatki.grid(column=0, row=0)  # wyświtlenie okienka
        self.master.notatki.insert(INSERT, 'Miejsce na obliczenia/notatki')
        pass

    def onButton3(self):
        self.child = Child3(self.master)    #po kliknieciu odpowiedniego guzika przenosi nas do odpowiedniego okna
    def onButton2(self):
        self.child = Child2(self.master)
    def onButton(self):
        self.child = Child(self.master) # przekazanie okna jako rodzica

    def run(self):    #
        self.master.mainloop()

#----------------------------------------------------------------------











class Child():   #klasa dziecka KULA

    def __init__(self, parent):
            self.master = tk.Toplevel(parent)  # bezposrednie tworzenie okna
            self.master.title("Child")  # wewnetrzny dostep do wlasnosci okna
            # tk.Button(self.master, text="Otworz okno Child z okna Child", command=self.onButton).grid(column=0,row=15,sticky=NW)
            self.master.geometry("800x620")
            self.master.resizable(width=False, height=False)
            self.master.title("Kula")
            self.master.configure(background="white")
            self.master.img1 = img1 = tk.PhotoImage(file="kula2.png")
            self.master.img2 = img2 = tk.PhotoImage(file="wzory1.png")
            tk.Label(self.master, text="Kula jest określona promieniem lub średnicą, jest zbiorem punktów,"
                     , bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=1,column=0,sticky=SW)
            tk.Label(self.master, text="które są odległe od środka maksymalnie długością równą promieniowi."
                     , bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=2, column=0, sticky=SW)
            tk.Label(self.master, bg="white", fg="midnight blue", font="none 10 bold").grid(row=3,
                                                                                                          column=0,
                                                                                                          sticky=SW)
            tk.Label(self.master,text="WZORY", bg="white", fg="DeepSkyBlue2", font="none 10 bold").grid(row=5, column=0, sticky=SW)
            tk.Label(self.master, text="P=4πr2", bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=6,
                                                                                                           column=0,
                                                                                                           sticky=SW)
            tk.Label(self.master, text="V=4/3πr^3", bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=12,
                                                                                                            column=0,
                                                                                                            sticky=NW)
            tk.Label(self.master, text="d = 2 * r", bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=13, column=0,
                                                                                                     sticky=NW)


            tk.Label(self.master,image=img1, text="", bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=30, column=0,
                                                                                                   sticky=NW)
            tk.Label(self.master, image=img2, text="", bg="white", fg="DeepSkyBlue2", font="none 12 bold").grid(row=30,
                                                                                                               column=0,
                                                                                                               sticky=S)

            tk.Label(self.master, text=" ", bg="white", fg="DeepSkyBlue2",
                     font="none 13 bold").grid(column=0, row=14, sticky=NW)
            tk.Label(self.master,text="                                              KALKULATOR   ",bg="white",fg="DeepSkyBlue2", font="none 13 bold").grid(row=14)


            wynik2 = tk.Label(self.master, text="Pole : ", bg="white", fg="DeepSkyBlue2", font="none 13 bold")
            tk.Label(self.master, text="Podaj promień:  ", bg="white", fg="DeepSkyBlue2", font="none 13 bold").grid(column=0, row=17, sticky=NW)
            wynik2.grid(column=0, row=19, sticky=NW)
            #STWORZENIE OKNA ENTRY DO WPISYWANIA WARTOSCI
            number1 = tk.IntVar()
            tk.a = Entry(self.master, textvariable=number1, width=8)
            tk.a.grid(column=0, row=18, sticky=NW)
            a = float(tk.a.get())  #ZAMIENIENIE ZE STRINGA NA FLOAT ENTRY


            wynik3 = tk.Label(self.master, text="Objętość : ", bg="white", fg="DeepSkyBlue2", font="none 13 bold")
            wynik3.grid(column=0, row=20, sticky=NW)


            def oblicz2():   #wzor na pole kuli
                kulson2 = 4/3 * math.pi * float(tk.a.get())*float(tk.a.get())*float(tk.a.get())
                wynik4 = f"Objętość : {round(kulson2, 2)}"   #formatowanie stringow
                wynik3.configure(text=wynik4)  #wypisanie wyniku w odpowiednim miejscu


                kulson = 4 * math.pi * float(tk.a.get()) * float(tk.a.get())
                wynik = f"Pole : {round(kulson, 2)}"
                wynik2.configure(text=wynik)

            przycisk = Button(self.master, text="Oblicz", command=oblicz2, bg="white", fg="DeepSkyBlue2",
                              font="none 12 bold").grid(column=0, row=21, sticky=NW)  #przycisk oblicz
            def onButton(self):
                self.master = Child(self.master)  # przekazanie okna jako rodzica










class Child2():   #klasa dziecka WALEC

    def __init__(self, parent):
            self.master = tk.Toplevel(parent)  # bezposrednie tworzenie okna
            self.master.title("Child")  # wewnetrzny dostep do wlasnosci okna
            # tk.Button(self.master, text="Otworz okno Child z okna Child", command=self.onButton).grid(column=0,row=15,sticky=NW)
            self.master.geometry("800x620")
            self.master.resizable(width=False, height=False)
            self.master.title("Walec")
            self.master.configure(background="white")
            self.master.img1 = img1 = tk.PhotoImage(file="walec2.png")

            tk.Label(self.master, text="Walec obrotowy jest bryłą składającą się z dwóch równoległych podstaw i płaszcz. ", bg="white",    fg="midnight blue",font="none 11 bold").grid(row=1, column=0, sticky=NW)
            tk.Label(self.master, text="Płaszcz jest prostopadły do podstawy, a podstawa jest utworzona przez koło.", bg="white", fg="midnight blue", font="none 11 bold").grid(row=2, column=0,
                                                                                                      sticky=NW)
            tk.Label(self.master, text="Wzory", bg="white", fg="midnight blue", font="none 11 bold").grid(row=3, column=0,
                                                                                                      sticky=NW)
            tk.Label(self.master, text="Pp=πr2", bg="white", fg="midnight blue", font="none 10 bold").grid(row=4, column=0,
                                                                                                      sticky=NW)

            tk.Label(self.master, text="Pb=2πrh ", bg="white", fg="midnight blue", font="none 10 bold").grid(row=6, column=0,
                                                                                                      sticky=NW)

            tk.Label(self.master, text="Pc=2Pp+Pb=2πr2+2πrh=2πr(r+h) ", bg="white", fg="midnight blue", font="none 10 bold").grid(row=8, column=0,
                                                                                                      sticky=NW)

            tk.Label(self.master, text="V=Pp⋅h=πr2h ", bg="white", fg="midnight blue", font="none 10 bold").grid(row=10, column=0,
                                                                                                      sticky=NW)

            tk.Label(self.master, text="                                                                  KALKULATOR ", bg="white", fg="midnight blue",
                     font="none 13 bold").grid(column=0, row=14, sticky=NW)
            tk.Label(self.master,text="Podaj promień",bg="White", fg="midnight blue",
                     font="none 13 bold").grid(column=0, row=15, sticky=NW)
            tk.Label(self.master, text="Podaj wysokość", bg="White", fg="midnight blue",
                     font="none 13 bold").grid(column=1, row=15, sticky=NW)

            wynikpolep = tk.Label(self.master, text="Pole powierzhni podstawy : ", bg="white", fg="midnight blue", font="none 13 bold")
            wynikpolep.grid(column=0, row=19, sticky=NW)
            wynikpoleb = tk.Label(self.master, text="Pole powierzhni bocznej : ", bg="white", fg="midnight blue", font="none 13 bold")
            wynikpoleb.grid(column=0, row=20, sticky=NW)
            wynikpolec = tk.Label(self.master, text="Pole powierzhni całkowitej :", bg="white", fg="midnight blue", font="none 13 bold")
            wynikpolec.grid(column=0, row=21, sticky=NW)
            wynikobjet = tk.Label(self.master, text="Objętość :", bg="white", fg="midnight blue", font="none 13 bold")
            wynikobjet.grid(column=0, row=22, sticky=NW)
            tk.Label(self.master,image=img1).grid(column=0,row=23,sticky=E)


            number1 = tk.IntVar()
            number2 = tk.IntVar()
            tk.a = Entry(self.master, textvariable=number1, width=8)
            tk.a.grid(column=0, row=16, sticky=NW)
            a = float(tk.a.get())

            tk.b = Entry(self.master,textvariable=number2,width=8)
            tk.b.grid(column=1,row=16,sticky=NW)
            b = float(tk.b.get())


            def oblicz():
                polep = math.pi*float(tk.a.get())**2
                poleb = 2 * math.pi * float(tk.a.get()) * float(tk.b.get())
                polec = 2*polep+poleb
                objet = polec* float(tk.b.get())

                wynik1 = f"Pole powierzhni podstawy : {round(polep, 2)}"
                wynik2 = f"Pole powierzhni bocznej : {round(poleb, 2)}"
                wynik3 = f"Pole powierzhni całkowitej : {round(polec, 2)}"
                wynik4 = f"Objętość : {round(objet, 2)}"
                wynikpolep.configure(text=wynik1)
                wynikpoleb.configure(text=wynik2)
                wynikpolec.configure(text=wynik3)
                wynikobjet.configure(text=wynik4)


            przycisk = Button(self.master, text="Oblicz", command=oblicz, bg="white", fg="midnight blue",
                              font="none 12 bold").grid(column=0, row=18, sticky=NW)


class Child3():   #stożek

    def __init__(self, parent):
            self.master = tk.Toplevel(parent)
            self.master.title("Stożek")
            self.master.geometry("800x620")
            self.master.resizable(width=False, height=False)
            self.master.title("Walec")
            self.master.configure(background="white")
            tk.Label(self.master, text="    STOŻEK", bg="white",
                     fg="midnight blue",
                     font="none 18 bold").grid(row=0, column=0, sticky=N)
            tk.Label(self.master, text="Stożek powstaje przez obrót trójkąta prostokątnego wokół jednej z przyprostokątnych.  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=1, column=0, sticky=NW)

            tk.Label(self.master, text="Przyprostokątna ta tworzy wysokość stożka, a druga przyprostokątna staje się promieniem podstawy. ", bg="white", fg="midnight blue",
             font="none 11 bold").grid(row=2, column=0, sticky=NW)
            tk.Label(self.master, text="Przeciwprostokątna trójkąta prostokątnego staje się tworzącą stożka. ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=3, column=0, sticky=NW)
            tk.Label(self.master, text="Przekrojem osiowym stożka jest trójkąt równoramienny ABC.  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=4, column=0, sticky=NW)
            tk.Label(self.master, text="Podstawą stożka jest koło.  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=5, column=0, sticky=NW)
            tk.Label(self.master, text="Wzór na pole podstawy stożka:  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=6, column=0, sticky=NW)
            tk.Label(self.master, text="Pp=πr2  ", bg="white",
                     fg="midnight blue", font="none 10 bold").grid(row=7, column=0, sticky=NW)
            tk.Label(self.master, text="Wzór na pole powierzchni bocznej stożka:  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=8, column=0, sticky=NW)
            tk.Label(self.master, text="Pb=πrl  ", bg="white",
                     fg="midnight blue", font="none 10 bold").grid(row=9, column=0, sticky=NW)
            tk.Label(self.master, text="Wzór na pole powierzchni całkowitej stożka:  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=10, column=0, sticky=NW)
            tk.Label(self.master, text="Pc=πr2+πrl=πr(r+l)  ", bg="white",
                     fg="midnight blue", font="none 10 bold").grid(row=11, column=0, sticky=NW)
            tk.Label(self.master, text="Wzór na objętość stożka:  ", bg="white",
                     fg="midnight blue", font="none 11 bold").grid(row=12, column=0, sticky=NW)
            tk.Label(self.master, text="V=13Pp⋅h=πr2h3  ", bg="white",
                     fg="midnight blue", font="none 10 bold").grid(row=13, column=0, sticky=NW)

            tk.Label(self.master, text="Obliczenia: ", bg="white", fg="midnight blue",
                     font="none 13 bold").grid(column=0, row=14, sticky=NW)
            tk.Label(self.master, text="Podaj promień", bg="White", fg="midnight blue",
                     font="none 13 bold").grid(column=0, row=15, sticky=NW)
            tk.Label(self.master, text="Podaj wysokość", bg="White", fg="midnight blue",
                     font="none 13 bold").grid(column=0, row=15, sticky=S)

            wynikpolep = tk.Label(self.master, text=" ", bg="white", fg="midnight blue", font="none 13 bold")
            wynikpolep.grid(column=0, row=19, sticky=NW)
            wynikpoleb = tk.Label(self.master, text=" ", bg="white", fg="midnight blue", font="none 13 bold")
            wynikpoleb.grid(column=0, row=20, sticky=NW)
            wynikpolec = tk.Label(self.master, text=" ", bg="white", fg="midnight blue", font="none 13 bold")
            wynikpolec.grid(column=0, row=21, sticky=NW)
            wynikobjet = tk.Label(self.master, text="", bg="white", fg="midnight blue", font="none 13 bold")
            wynikobjet.grid(column=0, row=22, sticky=NW)

            number1 = tk.IntVar()
            number2 = tk.IntVar()
            tk.a = Entry(self.master, textvariable=number1, width=8)
            tk.a.grid(column=0, row=16, sticky=NW)
            a = float(tk.a.get())

            tk.b = Entry(self.master, textvariable=number2, width=8)
            tk.b.grid(column=0, row=16, sticky=S)
            b = float(tk.b.get())
            def oblicz():
                l = math.sqrt(float(tk.a.get()) * float(tk.a.get()) + float(tk.b.get()) * float(tk.b.get()))
                polep = math.pi * float(tk.a.get()) * float(tk.a.get())
                poleb = math.pi * float(tk.a.get()) * l
                polec = polep + poleb
                objet =  1/3 *  math.pi * math.pow( float(tk.a.get()),2) *  float(tk.b.get())

                wynik1 = f"Pole powierzhni podstawy stożka wynosi: {round(polep, 2)}"
                wynik2 = f"Pole powierzhni bocznej stożka wynosi: {round(poleb, 2)}"
                wynik3 = f"Pole powierzhni całkowitej stożka wynosi: {round(polec, 2)}"
                wynik4 = f"Objętość stożka wynosi: {round(objet, 2)}"
                wynikpolep.configure(text=wynik1)
                wynikpoleb.configure(text=wynik2)
                wynikpolec.configure(text=wynik3)
                wynikobjet.configure(text=wynik4)

            przycisk = Button(self.master, text="Oblicz", command=oblicz, bg="white", fg="midnight blue",
                              font="none 12 bold").grid(column=0, row=18, sticky=NW)


#----------------------------------------------------------------------

glowne = Main()
glowne.master.title("Kalkulator matematyczny") # zewnetrzny dostep do wlasnosci okna
glowne.run()