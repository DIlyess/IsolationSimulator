from trace_maison import *
from Modele_simple import *
from matplotlib import animation
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def multi_piece(Maison, T_ext, durée, P_chauf, epa_mur_ext, T0):

    # Récupération des constantes en fonction des arguments #
    T_ext = [T_ext]*durée
    nb_piece, Surf, Murs, Mat_surf, Mat_epa, Mat_fen, Mat_lambda = constante(Maison, epa_mur_ext)

    # Résolution et création d'un tableau des températures #

    T, t = resolution_simple(T0, durée, nb_piece, Surf,
                             Murs, Mat_surf, Mat_epa, Mat_fen, Mat_lambda, T_ext, P_chauf)

    # Création et configuration de la fenêtre d'affichage #

    fig = plt.figure()
    plt.axis('equal')
    ax = tracer_maison_complete(Maison, fig)

    # Création de couleur en fonction de la température #

    colors = plt.cm.jet(np.linspace(0, 1, 100))

    # Création de listes d'objets plt (rectangles et textes) #

    patchs = []
    texte_T = []
    for k in range(nb_piece):
        patchs += [patches.Rectangle((Maison[k][2][6], Maison[k][2][7]), Maison[k][2]
                                     [4]-Maison[k][2][6], Maison[k][2][3]-Maison[k][2][5], fc='y', color='w')]
        texte_T += [ax.text((Maison[k][2][4]+Maison[k][2][6])/2-1, (Maison[k][2][3]+Maison[k]
                                                                  [2][5])/2-0.2, str(round(T[:][:, k][0]-273, 1))+'°C', fontsize=8)]
    texte_T += [ax.text(-2.5, 3.4, 'T ext='+str(round(T_ext[0]-273, 1)
                                                )+'°C', fontsize=8)]
    texte_T += [ax.text(-2.5, 2.1, 't=', fontsize=8)]
    for i in range(nb_piece):
        texte_T += [ax.text((Maison[i][2][4]+Maison[i][2][6])/2-0.75, (Maison[i][2][3]+Maison[i]
                                                                       [2][5])/2+0.5, Maison[i][4], fontsize=8)]

    # Fonction d'initialistion des objets affichés #

    def init():
        for k in range(len(patchs)):
            ax.add_patch(patchs[k])

        return patchs[0],

    # Fonction d'actualisation des objets affichés #

    def animate(i):
        for k in range(len(patchs)):
            patchs[k].set_color(colors[int(T[:][:, k][i]-223)])
            texte_T[k].set_text(str(round(T[:][:, k][i]-273, 1))+'°C')
        texte_T[len(patchs)].set_text('Text='+str(round(T_ext[i]-273, 1))+'°C')
        texte_T[len(patchs)+1].set_text('t='+str(int(i/3600))+'h' +
                                        str(int(i % 3600/60))+'min'+str(int(i % 3600 % 60))+'s')
        return patchs[0],

    # Animation grâce au module animation de matplotlib #

    anim = animation.FuncAnimation(fig, animate,
                                   init_func=init, frames=range(0, 50000, 20), interval=1)

    plt.show()


# #Exemple:
## Aide arguments:
##  Maison : liste de dimension nombre de pièce contenant des dicos correspondants aux pièces de la maison.
##  T_ext : scalaire correspondant à la température à l'extérieure de la maison en K.
##  durée : scalaire correspondant à la durée de la simulation en seconde.
##  P_chauf : liste de dimension nombre de pièce contenant des scalaires corresepondants aux puissances fournies par le chauffage de chaque pièce.
##  epa_mur_ext : scalaire correspondant à l'épaisseur des murs extérieurs en dcm.
##  T0 : liste de dimension nombre de pièce contenant des scalaires corresepondants aux températures initiales de chaque pièce en K.
# multi_piece(MaisonU,273,50000,[0]*15,5,[293]*15)


