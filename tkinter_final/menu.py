from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from random import *
from tkinter import *
import matplotlib
from anim import *
from anim_multipieces import *
from PIL import Image, ImageTk


# création d'un police de caractère par défaut
LARGE_FONT = ("Verdana", 12)


class house(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # appel des différentes fenêtres
        for F in (StartPage, Cursor_1piece, Cursor_2piece, Maison):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # fonction qui affiche la fenêtre appelée
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# Fenêtre d'acceuil


class StartPage(Frame):

    def __init__(self, parent, controller):
        # initialisation de la page
        Frame.__init__(self, parent)

        self.configure(bg='blue')

        # image = Image.open("tkinter_final/image.png")

        # render = ImageTk.PhotoImage(image)
        # img = Label(self, image=render)
        # img.image = render
        # img.pack(side=BOTTOM)

        label = Label(
            self, text="Bienvenue sur le projet du groupe ThermodynamiCS !", bg="cyan", fg="black", font=("Times New Roman", 30, "bold"))
        label.pack(fill=X)

        # bouton pour aller à la page du graph
        button1 = Button(self, text='Lancer la simulation physique pour une seule pièce',
                         command=lambda: controller.show_frame(Cursor_1piece), bg="cyan", fg="black", font=("Times New Roman", 10))
        button1.pack(pady=10)

        button2 = Button(self, text="Lancer la simulation physique pour deux pièces séparées d'un mur",
                         command=lambda: controller.show_frame(Cursor_2piece), bg="cyan", fg="black", font=("Times New Roman", 10))
        button2.pack(pady=10)

        button3 = Button(self, text='Lancer la simulation pour une maison entière',
                         command=lambda: controller.show_frame(Maison), bg="cyan", fg="black", font=("Times New Roman", 10))
        button3.pack(pady=10)

        # bouton pour quitter
        button4 = Button(self, text='Quitter',
                         command=quit, bg="cyan", fg="black", font=("Times New Roman", 10))
        button4.pack(pady=10)


# Fenêtre du graph


class Maison(Frame):

    def __init__(self, parent, controller):
        # initialisation de la page
        Frame.__init__(self, parent)

        self.configure(bg='blue')
        label = Label(self, text="Maison entière", bg="cyan",
                      fg="black", font=("Times New Roman", 30, "bold"))
        label.pack(pady=10, padx=10, fill=X)
        # bouton pour revenir à la page d'acceuil
        button1 = Button(self, text='Home',
                         command=lambda: controller.show_frame(StartPage))
        button1.pack(side=TOP)
        HomeList = ["MaisonC", "MaisonU", "MaisonL"]

        nom_maison = StringVar(self, 'Villa')
        nom_maison.set(HomeList[0])
        optMaison = OptionMenu(self, nom_maison, *HomeList)
        optMaison.config(width=20, font=(
            'Helvetica', 9), background='cyan')
        optMaison.pack(pady=10)

        Curseur_puissance = Scale(self, from_=-500, to_=500, resolution=10,
                                  label='Puisance Chauffage par pièce', orient=HORIZONTAL, length=200, background='cyan')
        Curseur_puissance.set(0)
        Curseur_puissance.pack()

        Curseur_Text = Scale(self, from_=-20, to_=40, resolution=1,
                             label='Température extérieure (°C)', orient=HORIZONTAL, length=200, background='cyan')
        Curseur_Text.set(20)
        Curseur_Text.pack()

        Curseur_epaisseur = Scale(self, from_=10, to_=100, resolution=10,
                                  label='Epaisseur des murs (cm)', orient=HORIZONTAL, length=200, background='cyan')
        Curseur_epaisseur.set(50)
        Curseur_epaisseur.pack()

        Curseur_Tint = Scale(self, from_=-10, to_=30, resolution=1,
                             label='Température intérieure initiale (°C) ', orient=HORIZONTAL, length=200, background='cyan')
        Curseur_Tint.set(20)
        Curseur_Tint.pack()

        def simu():
            def callback(*args):
                nom_maison.configure()
            nb_piece = len(globals()[nom_maison.get()])

            multi_piece(globals()[nom_maison.get()], Curseur_Text.get()+273, 50000, [Curseur_puissance.get()]
                        * nb_piece, int(Curseur_epaisseur.get()/10), [Curseur_Tint.get()+273]*nb_piece)

        bouton = Button(self, text="Lancer la simulation",
                        command=simu)
        bouton.pack(pady=10)

        # bouton pour quitter
        button2 = Button(self, text='Quitter',
                         command=quit)
        button2.pack()

        # création du canvas
        # canvas = FigureCanvasTkAgg(fig, self)
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=BOTTOM)


class Cursor_1piece(Frame):

    def __init__(self, parent, controller):
        # initialisation de la page
        Frame.__init__(self, parent)
        self.configure(bg='blue')
        label = Label(self, text="Simulation pour une pièce", bg="cyan",
                      fg="black", font=("Times New Roman", 30, "bold"))
        label.pack(pady=10, padx=10, fill=X)
        # bouton pour quitter
        button2 = Button(self, text='Quitter',
                         command=quit)
        button2.pack(side=BOTTOM)

        # bouton pour revenir à la page d'acceuil
        button1 = Button(self, text='Home',
                         command=lambda: controller.show_frame(StartPage))
        button1.pack(side=BOTTOM)

        # création du canvas
        # scale1 = Scale(self, from_=0.5, to_=10, resolution=0.5,
        #                label='lambda', orient=HORIZONTAL, length=200)
        # scale1.place(x=750, y=0)
        # scale1.set(1)

        # scale2 = Scale(self, from_=10, to_=10000, resolution=10, label='rho',
        #                orient=HORIZONTAL, length=200)
        # scale2.place(x=750, y=75)
        # scale2.set(2400)

        e_mur = Scale(self, from_=5, to_=50, resolution=1,
                      label='Epaisseur des murs (dm)', orient=HORIZONTAL, length=200, background='cyan')
        e_mur.place(x=100, y=100)
        e_mur.set(10)

        l_piece = Scale(self, from_=20, to_=100, resolution=1,
                        label='Largeur de la pièce (dm)', orient=HORIZONTAL, length=200, background='cyan')
        l_piece.place(x=100, y=175)
        l_piece.set(50)

        L_piece = Scale(self, from_=20, to_=100, resolution=1,
                        label='Longeur de la pièce(dm)', orient=HORIZONTAL, length=200, background='cyan')
        L_piece.place(x=100, y=250)
        L_piece.set(50)

        T_ext = Scale(self, from_=-20, to_=100,
                      label='Température extérieure (°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_ext.place(x=350, y=100)
        T_ext.set(0)

        T_int_piece = Scale(self, from_=-20, to_=100,
                            label='Température intérieure (°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_int_piece.place(x=350, y=175)
        T_int_piece.set(20)

        T_int_mur = Scale(self, from_=-20, to_=100,
                          label='Température intérieure du mur(°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_int_mur.place(x=350, y=325)
        T_int_mur.set(15)

        T_chauff = Scale(self, from_=-20, to_=100,
                         label='Température du chauffage (°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_chauff.place(x=350, y=250)
        T_chauff.set(40)

        var_hd = IntVar()
        hd = Checkbutton(
            self, text="Chauffage coin haut droit", variable=var_hd, background='cyan')
        hd.place(x=900, y=125)

        var_hg = IntVar()
        hg = Checkbutton(
            self, text="Chauffage coin haut gauche", variable=var_hg, background='cyan')
        hg.place(x=650, y=125)

        var_bg = IntVar()
        hg = Checkbutton(
            self, text="Chauffage coin bas gauche", variable=var_bg, background='cyan')
        hg.place(x=650, y=175)

        var_bd = IntVar()
        hg = Checkbutton(
            self, text="Chauffage coin bas droite", variable=var_bd, background='cyan')
        hg.place(x=900, y=175)

        var_fh = IntVar()
        fh = Checkbutton(
            self, text="Fenêtre nord", variable=var_fh, background='cyan')
        fh.place(x=800, y=250)

        var_fb = IntVar()
        fb = Checkbutton(
            self, text="Fenêtre sud", variable=var_fb, background='cyan')
        fb.place(x=800, y=350)

        var_fg = IntVar()
        fg = Checkbutton(
            self, text="Fenêtre ouest", variable=var_fg, background='cyan')
        fg.place(x=700, y=300)

        var_fd = IntVar()
        fd = Checkbutton(
            self, text="Fenêtre est", variable=var_fd, background='cyan')
        fd.place(x=900, y=300)

        def simulation():
            anim_1pc(0.8, 2400, 1, e_mur.get(), T_ext.get(),  T_int_mur.get(), T_int_piece.get(),
                     L_piece.get(), l_piece.get(), T_chauff.get(), var_bd.get(), var_bg.get(), var_hd.get(), var_hg.get(), var_fh.get(), var_fb.get(), var_fg.get(), var_fd.get())

        bouton = Button(self, text="Lancer la simulation",
                        command=simulation)
        bouton.pack(side=BOTTOM)


class Cursor_2piece(Frame):

    def __init__(self, parent, controller):
        # initialisation de la page
        Frame.__init__(self, parent)
        self.configure(bg='blue')
        label = Label(self, text="Simulation pour deux pièces", bg="cyan",
                      fg="black", font=("Times New Roman", 30, "bold"))
        label.pack(pady=10, padx=10, fill=X)
        # bouton pour quitter
        button2 = Button(self, text='Quitter',
                         command=quit)
        button2.pack(side=BOTTOM)

        # bouton pour revenir à la page d'acceuil
        button1 = Button(self, text='Home',
                         command=lambda: controller.show_frame(StartPage))
        button1.pack(side=BOTTOM)

        # création du canvas
        # scale1 = Scale(self, from_=0.5, to_=10, resolution=0.5,
        #                label='lambda', orient=HORIZONTAL, length=200)
        # scale1.place(x=750, y=0)
        # scale1.set(1)

        # scale2 = Scale(self, from_=10, to_=10000, resolution=10, label='rho',
        #                orient=HORIZONTAL, length=200)
        # scale2.place(x=750, y=75)
        # scale2.set(2400)

        e_mur = Scale(self, from_=5, to_=50, resolution=1,
                      label='Epaisseur des murs (dm)', orient=HORIZONTAL, length=200, background='cyan')
        e_mur.place(x=100, y=100)
        e_mur.set(10)

        l_piece = Scale(self, from_=20, to_=100, resolution=1,
                        label='Largeur de la pièce (dm)', orient=HORIZONTAL, length=200, background='cyan')
        l_piece.place(x=100, y=175)
        l_piece.set(50)

        L_piece = Scale(self, from_=20, to_=100, resolution=1,
                        label='Longeur de la pièce(dm)', orient=HORIZONTAL, length=200, background='cyan')
        L_piece.place(x=100, y=250)
        L_piece.set(50)

        T_ext = Scale(self, from_=-20, to_=100,
                      label='Température extérieur (°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_ext.place(x=350, y=100)
        T_ext.set(0)

        T_int_piece = Scale(self, from_=-20, to_=100,
                            label='Température intérieur (°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_int_piece.place(x=350, y=175)
        T_int_piece.set(10)

        T_chauff = Scale(self, from_=-20, to_=100,
                         label='Température du chauffage (°C)', orient=HORIZONTAL, length=200, background='cyan')
        T_chauff.place(x=350, y=250)
        T_chauff.set(40)

        var_hd = IntVar()
        hd = Checkbutton(
            self, text="Chauffage coin haut droit", variable=var_hd, background='cyan')
        hd.place(x=900, y=175)

        var_hg = IntVar()
        hg = Checkbutton(
            self, text="Chauffage coin haut gauche", variable=var_hg, background='cyan')
        hg.place(x=650, y=175)

        var_bg = IntVar()
        hg = Checkbutton(
            self, text="Chauffage coin bas gauche", variable=var_bg, background='cyan')
        hg.place(x=650, y=250)

        var_bd = IntVar()
        hg = Checkbutton(
            self, text="Chauffage coin bas droite", variable=var_bd, background='cyan')
        hg.place(x=900, y=250)

        def simulation():
            anim_2pcs(0.8, 2400, 1, e_mur.get(), l_piece.get(), 10, 10, T_int_piece.get(), T_ext.get(),
                      (T_ext.get()+T_int_piece.get())/2, T_int_piece.get(), L_piece.get(), l_piece.get(), T_chauff.get(), var_bd.get(), var_bg.get(), var_hd.get(), var_hg.get())

        bouton = Button(self, text="Lancer la simulation",
                        command=simulation)
        bouton.pack(side=BOTTOM)


# exécution du code
app = house()
# choix de la définition de l'application
app.geometry("1280x720")
# exécution de l'animation
app.mainloop()
