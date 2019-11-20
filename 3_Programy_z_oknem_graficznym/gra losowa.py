from tkinter import *
import random

t = Tk()
t.title("Wybierz przycisk")
t.geometry("300x350")

def wstaw_przyciski():
    ile_przyciskow = 8
    global przyciski
    przyciski = []
    dobry = random.randint(0,ile_przyciskow-1)
    for i in range (ile_przyciskow):
        if i == dobry:
            przyciski.append(Button(t, text = "kliknij mnie", command=trafiony))
        else:
            przyciski.append(Button(t, text = "kliknij mnie", command=pudlo))
    for i in przyciski:
        i.pack(fill=BOTH, expand=YES)