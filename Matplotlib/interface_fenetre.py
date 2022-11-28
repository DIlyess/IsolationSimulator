from tkinter import *

from matplotlib.pyplot import sca
from anim_diff_fenetre import*

fen = Tk()


def simulation():
    animation_diff(scale1.get(), rho, c, scale3.get(), scale4.get(), 10, 10, 10, scale8.get(),
                   scale10.get(), scale10.get(), scale11.get(), scale4.get(), scale13.get(), scale12.get())


canv = Canvas(fen, width=1920, height=1080, bg='ivory')
canv.pack()

scale1 = Scale(canv, from_=0.1, to_=5, resolution=0.1,
               label='lambda', orient=HORIZONTAL, length=200)
scale1.place(x=750, y=0)

scale2 = Scale(canv, from_=10, to_=10000, resolution=10, label='rho',
               orient=HORIZONTAL, length=200)
scale2.place(x=750, y=75)

scale3 = Scale(canv, from_=5, to_=50, resolution=1,
               label='épaisseur des murs en pixel', orient=HORIZONTAL, length=200)
scale3.place(x=0, y=0)

scale4 = Scale(canv, from_=20, to_=100, resolution=1,
               label='largeur en pixel', orient=HORIZONTAL, length=200)
scale4.place(x=0, y=75)

scale11 = Scale(canv, from_=20, to_=100, resolution=1,
                label='longeur en pixel', orient=HORIZONTAL, length=200)
scale11.place(x=0, y=150)

scale8 = Scale(canv, from_=-20, to_=100,
               label='température extérieur °C', orient=HORIZONTAL, length=200)
scale8.place(x=250, y=0)

scale10 = Scale(canv, from_=-20, to_=100,
                label='température intérieur en °C', orient=HORIZONTAL, length=200)
scale10.place(x=250, y=75)

scale13 = Scale(canv, from_=-20, to_=100,
                label='température chauffage en °C', orient=HORIZONTAL, length=200)
scale13.place(x=500, y=75)

scale12 = Scale(canv, from_=0, to_=1,
                label='chauffage oui/non', orient=HORIZONTAL, length=200)
scale12.place(x=500, y=0)

bouton = Button(canv, text="Lancer la simulation", command=simulation)
bouton.place(x=1000, y=0)


if __name__ == "__main__":
    fen.geometry('1920x1080')
    fen.mainloop()
