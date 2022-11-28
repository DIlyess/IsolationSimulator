import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec

# ======================================= #


def join(L1, L2):
    res = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            res.append((L1[i], L2[j]))
    return res


def anim_1pc(lamb, rho, c, epaisseur, T_ext, T_int_mur, T_int_piece, x_piece, y_piece, T_chauffage, bd, bg, hd, hg, fh, fb, fg, fd):
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
    #gamma_mur = (alpha_mur * delta_t) / (delta_x*delta_y)
    gamma_mur = 0.15

    # Créer une liste de matrice de zéro où res[i] va renvoyer la matrice des température au temps i
    res_mur = np.zeros((max_iter_time, y_piece, epaisseur))

    # Initialise la température du mur
    res_mur.fill(T_int_mur)

    # Mets dans toutes les matrices les conditions aux limites
    res_mur[:, :, (epaisseur-1):] = T_int_mur
    res_mur[:, :, :1] = T_ext
    res_mur[:, :1, :] = T_int_mur
    res_mur[:, (y_piece-1):, :] = T_int_mur

    ###############################################################################

    # Paramètres comme pour le mur mais avec les valeurs adaptées à l'air
    alpha_air = 2
    delta_t = (delta_x * delta_y)/(4 * alpha_air)
    gamma_air = (alpha_air * delta_t) / (delta_x ** 2)

    # Créer une liste de matrice de zéro où res[i] va renvoyer la matrice des température au temps i
    res_piece = np.empty((max_iter_time, y_piece, x_piece))

    # Initialise la température du mur
    res_piece.fill(T_int_piece)

    if fh == 1:
        for k in range(max_iter_time):
            res_piece[k, (y_piece-1):, x_piece//2-5:x_piece//2+6] = T_ext

    if fb == 1:
        for k in range(max_iter_time):
            res_piece[k, 0, x_piece//2-5:x_piece//2+6] = T_ext

    if fd == 1:
        for k in range(max_iter_time):
            res_piece[k, y_piece//2-5:y_piece//2+6, (x_piece-1)] = T_ext

    if fg == 1:
        for k in range(max_iter_time):
            res_piece[k, y_piece//2-5:y_piece//2+6, 0] = T_ext

    # Résolution avec la méthode des différences finies pour la pièce sans chauffage

    def calculate_piece():
        for k in range(0, max_iter_time-1, 1):
            for i in range(1, y_piece-1, delta_x):
                for j in range(1, x_piece-1, delta_x):
                    res_piece[k + 1, i, j] = gamma_air * (res_piece[k][i+1][j] + res_piece[k][i-1][j] +
                                                          res_piece[k][i][j+1] + res_piece[k][i][j-1] - 4*res_piece[k][i][j]) + res_piece[k][i][j]
            for i in range(1, y_piece-1, delta_y):
                for j in range(1, epaisseur-1, delta_x):
                    res_mur[k + 1, i, j] = gamma_mur * (res_mur[k][i+1][j] + res_mur[k][i-1][j] +
                                                        res_mur[k][i][j+1] + res_mur[k][i][j-1] - 4*res_mur[k][i][j]) + res_mur[k][i][j]

            res_piece[k+1, (y_piece-1):, :] = (res_piece[k,
                                                         y_piece-2, :]+res_mur[k, :, epaisseur-2])/2
            res_piece[k+1, :, 0] = (res_piece[k, :, 1] +
                                    res_mur[k, :, epaisseur-2])/2
            res_piece[k+1, 0, :] = (res_piece[k, 1, :] +
                                    res_mur[k, :, epaisseur-2])/2
            res_piece[k+1, :, (x_piece-1)] = (res_piece[k,
                                                        :, x_piece-2]+res_mur[k, :, epaisseur-2])/2

            res_mur[k+1, :, (epaisseur-1):] = res_piece[k+1, :, 0]

    def calculate_chauffage():
        coord_chauffage = []
        if bd == 1:
            x_chauffage = [x_piece-10+i for i in range(11)]
            y_chauffage = [i for i in range(11)]
            coord_chauffage += ([ele for ele in join(
                y_chauffage, x_chauffage) if (ele[0]-5)**2+(ele[1]-(x_piece-5))**2 < 5**2])
        if bg == 1:
            x_chauffage = [i for i in range(11)]
            y_chauffage = [i for i in range(11)]
            coord_chauffage += ([ele for ele in join(
                y_chauffage, x_chauffage) if (ele[0]-5)**2+(ele[1]-5)**2 < 5**2])
        if hd == 1:
            x_chauffage = [x_piece-10+i for i in range(11)]
            y_chauffage = [y_piece-10+i for i in range(11)]
            coord_chauffage += ([ele for ele in join(
                y_chauffage, x_chauffage) if (ele[0]-(y_piece-5))**2+(ele[1]-(x_piece-5))**2 < 5**2])
        if hg == 1:
            x_chauffage = [i for i in range(11)]
            y_chauffage = [y_piece-10+i for i in range(11)]
            coord_chauffage += ([ele for ele in join(
                y_chauffage, x_chauffage) if (ele[0]-(y_piece-5))**2+(ele[1]-5)**2 < 5**2])
        for [i, j] in coord_chauffage:
            res_piece[:, i, j] = T_chauffage
        for k in range(0, max_iter_time-1, 1):
            for i in range(1, y_piece-1, delta_x):
                for j in range(1, x_piece-1, delta_x):
                    if (i, j) not in coord_chauffage:
                        res_piece[k + 1, i, j] = gamma_air * (res_piece[k][i+1][j] + res_piece[k][i-1][j] +
                                                              res_piece[k][i][j+1] + res_piece[k][i][j-1] - 4*res_piece[k][i][j]) + res_piece[k][i][j]
            for i in range(1, y_piece-1, delta_y):
                for j in range(1, epaisseur-1, delta_x):
                    res_mur[k + 1, i, j] = gamma_mur * (res_mur[k][i+1][j] + res_mur[k][i-1][j] +
                                                        res_mur[k][i][j+1] + res_mur[k][i][j-1] - 4*res_mur[k][i][j]) + res_mur[k][i][j]

        res_piece[k+1, (y_piece-1):, :] = (res_piece[k,
                                                     y_piece-2, :]+res_mur[k, :, epaisseur-2])/2
        res_piece[k+1, :, 0] = (res_piece[k, :, 1] +
                                res_mur[k, :, epaisseur-2])/2
        res_piece[k+1, 0, :] = (res_piece[k, 1, :] +
                                res_mur[k, :, epaisseur-2])/2
        res_piece[k+1, :, (x_piece-1)] = (res_piece[k,
                                                    :, x_piece-2]+res_mur[k, :, epaisseur-2])/2

        res_mur[k+1, :, (epaisseur-1):] = res_piece[k+1, :, (x_piece-1):]

    fig = plt.figure()
    gs = GridSpec(1, 2, figure=fig)
    ax_piece = fig.add_subplot(gs[0, 1])
    plt.xlabel("x")
    plt.ylabel("y")
    ax_piece.set_aspect('equal')

    ax_mur = fig.add_subplot(gs[0, 0])
    ax_mur.set_aspect('equal')

    plt.colorbar(ax_piece.pcolormesh(
        res_piece[0], cmap=plt.cm.jet, vmin=0, vmax=50), ax=ax_piece)

    def plotheatmap(piece_k, mur_k, k):
        # Actualise le temps
        ax_piece.set_title(
            f"Temperature dans la pièce \n à t = {k*delta_t:.3f} heures")
        ax_mur.set_title(
            f"Temperature dans le mur \n à t = {k*delta_t:.3f} heures")
        # Plot la matrice
        ax_piece.pcolormesh(piece_k, cmap=plt.cm.jet, vmin=0, vmax=40)
        ax_mur.pcolormesh(mur_k, cmap=plt.cm.jet, vmin=0, vmax=40)

        return fig

    # Do the calculation here
    if bg == 1 or hg == 1 or bd == 1 or hd == 1:
        calculate_chauffage()
    else:
        calculate_piece()

    def animate(k):
        plotheatmap(res_piece[k], res_mur[k], k)

    anim = animation.FuncAnimation(
        fig, animate, interval=1, frames=max_iter_time, repeat=True)
    # anim.save("heat_equation_solution.gif")
    plt.show()


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
T_int_piece = 20
T_int_mur = 10
T_ext = 0

# Chauffage
bd = 0
bg = 1
hd = 0
hg = 0
T_chauffage = 50

# Fenetre

fh = 0
fb = 0
fg = 0
fd = 0

anim_1pc(lamb, rho, c, epaisseur, T_ext, T_int_mur,
         T_int_piece, x_piece, y_piece, T_chauffage, bd, bg, hd, hg, fh, fb, fg, fd)
