import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec
from modèle_maison2 import*
from trace_maison2 import*


import timeit

start = timeit.default_timer()

# ======================================= #


def join(L1, L2):
    res = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            res.append([L1[i], L2[j]])
    return res


def animation_diff(lamb, rho, c, e_mur, hauteur, T_haut, T_bas, T_droite, T_gauche, T_int_mur, T_int_piece, x_piece, y_piece, T_chauffage=30, chauffage=False):
    # C'est le coeff qui lie la derivée temporelle de T et le laplacien de T
    alpha_mur = lamb/(rho*c)
    # Donne le pas pr la discretization selon x de la surface (Maillage)
    delta_x = 1
    # Donne le pas pr la discretization selon y de la surface (Maillage)
    delta_y = 1
    # Nombre d'iteration temporelle
    max_iter_time = 750
    # Calcule le pas de temps pour l'affichage
    delta_t = (delta_x * delta_y)/(4 * alpha_mur)

    # Choix du pas de temps pour que la solution converge (documentation)
    gamma_mur = (alpha_mur * delta_t) / (delta_x*delta_y)

    # Créer une liste de matrice de zéro où res[i] va renvoyer la matrice des température au temps i
    res_mur = np.zeros((max_iter_time, hauteur, epaisseur))

    # Initialise la température du mur
    res_mur.fill(T_int_mur)

    # Mets dans toutes les matrices les conditions aux limites
    res_mur[:, :, (epaisseur-1):] = T_droite
    res_mur[:, :, :1] = T_gauche
    res_mur[:, :1, :] = T_bas
    res_mur[:, (hauteur-1):, :] = T_haut

    # Résolution avec la méthode des différences finies pour le mur
    def calculate_mur(u):
        for k in range(0, max_iter_time-1):
            for i in range(1, hauteur-1, delta_y):
                for j in range(1, epaisseur-1, delta_x):
                    u[k + 1, i, j] = gamma_mur * (u[k][i+1][j] + u[k][i-1][j] +
                                                  u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
            u[k+1, 0, :] = u[k+1, 1, :]
            u[k+1, hauteur-1, :] = u[k+1, hauteur-2, :]
            u[k+1, :, epaisseur-1] = u[k+1, :, epaisseur-2]

        return u

    # Calcule dans un premier temps de toutes les matrices de température pour le mur
    res_mur = calculate_mur(res_mur)

    # Récolte les températures au bord du mur côté pièce pour chaque temps k
    T_bord_mur = res_mur[:, hauteur//2, epaisseur//2]

    ###############################################################################

    # Paramètres comme pour le mur mais avec les valeurs adaptées à l'air
    alpha_air = 2
    delta_t = (delta_x * delta_y)/(4 * alpha_air)
    gamma_air = (alpha_air * delta_t) / (delta_x ** 2)

    # Créer une liste de matrice de zéro où res[i] va renvoyer la matrice des température au temps i
    res_piece = np.empty((max_iter_time, y_piece, 2*x_piece+e_mur))
    x_len = len(res_piece[0][0])
    y_len = len(res_piece[0])

    # Initialise la température du mur
    res_piece.fill(T_int_piece)

    # Fait en sorte que à chaque temps k, T_mur(extremité)=T_air(extremité) (à ameliorer car discontinuité)
    for k in range(max_iter_time):
        res_piece[k, (y_len-1):, :] = T_bord_mur[k]
        res_piece[k, :, :1] = T_bord_mur[k]
        res_piece[k, :1, :] = T_bord_mur[k]
        res_piece[k, :, (x_len-1):] = T_bord_mur[k]

    zone_mur = join([i for i in range(y_piece)], [
                    j for j in range(x_piece+1, x_piece+e_mur+1)])

    # Dans un premier temps on supposera que a température des murs intérieurs est constante et vaut T_int_piece
    for [i, j] in zone_mur:
        res_piece[:, i, j] = T_int_mur

    # Résolution avec la méthode des différences finies pour la pièce sans chauffage
    def calculate_piece(u):
        for k in range(0, max_iter_time-1, 1):
            for i in range(1, y_len-1, delta_y):
                for j in range(1, x_len-1, delta_x):
                    if [i, j] not in zone_mur:
                        u[k + 1, i, j] = gamma_air * (u[k][i+1][j] + u[k][i-1][j] +
                                                      u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
        return u

    def calculate_chauffage(u):
        x_chauffage = [x_piece//2-5+i for i in range(11)]
        y_chauffage = [y_piece//2-5+i for i in range(11)]
        coord_chauffage = [ele for ele in join(
            y_chauffage, x_chauffage) if (ele[0]-y_piece//2)**2+(ele[1]-x_piece//2)**2 < 5**2]
        for [i, j] in coord_chauffage:
            u[:, i, j] = T_chauffage
        for k in range(0, max_iter_time-1, 1):
            for i in range(1, y_len-1, delta_y):
                for j in range(1, x_len-1, delta_x):
                    if [i, j] not in coord_chauffage and [i, j] not in zone_mur:
                        u[k + 1, i, j] = gamma_air * (u[k][i+1][j] + u[k][i-1][j] +
                                                      u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

        return u

    fig = plt.figure()
    gs = GridSpec(1, 2, figure=fig)

    ax_piece = fig.add_subplot(gs[0, 1])
    tracer_maison(Maison2)
    plt.xlabel("x")
    plt.ylabel("y")
    ax_piece.set_aspect('equal')

    ax_mur = fig.add_subplot(gs[0, 0])
    ax_mur.set_aspect('equal')

    def plotheatmap(piece_k, mur_k, k):
        # Actualise le temps
        #ax_piece.title(f"Temperature at t = {k*delta_t:.3f} unit time")
        # Plot la matrice
        ax_piece.pcolormesh(piece_k, cmap=plt.cm.jet, vmin=0, vmax=40)
        ax_mur.pcolormesh(mur_k, cmap=plt.cm.jet, vmin=0, vmax=40)
        # fig.colorbar(mappable=ax=ax_piece)
        return fig

    # Do the calculation here
    if not chauffage:
        res_piece = calculate_piece(res_piece)
    else:
        res_piece = calculate_chauffage(res_piece)

    def animate(k):
        plotheatmap(res_piece[k], res_mur[k], k)

    anim = animation.FuncAnimation(
        fig, animate, interval=1, frames=max_iter_time, repeat=False)
    # anim.save("heat_equation_solution.gif")
    plt.show()

# ======================================================== #

# Test#

# ======================================================== #


# Matériau
lamb = 0.8
rho = 2400
c = 1

# Caractéristiques de la surface du mur
epaisseur = 10
hauteur = 50

# Caractéristiques de la surface de la piece
x_piece = 50
y_piece = 50


# Conditions aux limites
T_int_piece = 10
T_int_mur = 20
T_droite = 20
T_gauche = 0
T_haut = T_int_mur
T_bas = T_int_mur

# Chauffage
chauffage = True
T_chauffage = 50


animation_diff(lamb, rho, c, epaisseur, hauteur, T_haut,
               T_bas, T_droite, T_gauche, T_int_mur, T_int_piece, x_piece, y_piece, T_chauffage, chauffage)

stop = timeit.default_timer()

print('Time: ', stop - start)
