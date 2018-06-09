#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Label
import os
import sys
import time

fenrir = Tk()
fenrir.title("Fenrir Ransomware")


Oups = Frame(fenrir, borderwidth=2, relief=GROOVE, bg="red")
Oups.pack(side=TOP, padx=30, pady=30)
Label(Oups, text="Woops ! Vos données ont été encryptées par Fenrir !", background="red", foreground="white", font="50").pack(padx=10, pady=10)


infos = Frame(fenrir, width=1000, height=500, bg='white')
infos.pack(side=TOP, padx=30, pady=30)
Label(infos, text="Comment puis-je récupérer mes données ?", font="30").pack(padx=10, pady=10)
Button(fenrir, text ='Payer en bitcoin').pack(side=RIGHT, padx=5, pady=5)

def callback():
    if askyesno('Supprimer les données', 'Êtes-vous sûr de vouloir supprimer vos données ?'):
        showwarning('Et bien adieu.', 'Tant pis...')
        showwarning('££ùp,!;', 'Vos données vont être supprimées dans quelques secondes.')
    else:
        showerror("Ah...", "Vous avez peur ? C'est ça ?")

Button(fenrir, text ='Supprimer vos données', command=callback).pack(side=RIGHT, padx=5, pady=5)

# Mettre la fenêtre au millieu de l'écran
fenrir.withdraw()
fenrir.update_idletasks()  # Update "requested size" from geometry manager

x = (fenrir.winfo_screenwidth() - fenrir.winfo_reqwidth()) / 2
y = (fenrir.winfo_screenheight() - fenrir.winfo_reqheight()) / 2
fenrir.geometry("+%d+%d" % (x, y))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position
fenrir.deiconify()
fenrir.mainloop()

fenrir.mainloop()
