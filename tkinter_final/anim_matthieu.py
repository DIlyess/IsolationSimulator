import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec


# ======================================= #
# fonction permetant de fusionner deux liste
def join(L1, L2):
    res = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            res.append((L1[i], L2[j]))
    return res


def animation_diff(lamb_mur, rho_mur, c_mur, lamb_air, rho_air, c_air, h_cc, epaisseur, hauteur, T_haut, T_bas, T_droite, T_gauche, T_int_mur, T_int_piece, x_piece, y_piece, chauffage=False):
    # C'est le coeff qui lie la derivée temporelle de T et le laplacien de T
    alpha_mur = lamb_mur/(rho_mur*c_mur)
    # Donne le pas pr la discretization selon x de la surface (Maillage)
    delta_x = 1
    # Donne le pas pr la discretization selon y de la surface (Maillage)
    delta_y = 1
    # Paramètres comme pour le mur mais avec les valeurs adaptées à l'air
    alpha_air = 10*lamb_air/(rho_air*c_air)
    alpha_cc = h_cc/(rho_air*c_air)
    delta_t = (delta_x * delta_y)/(alpha_air)

    # Nombre d'iteration temporelle
    max_iter_time = 750
    # Calcule le pas de temps pour l'affichage
    delta_t_1 = (delta_x * delta_y)/(4 * alpha_mur)
    delta_t_2 = delta_x*rho_air*c_air/(h_cc)
    delta_t = min(delta_t_1, delta_t_2)

    # Choix du pas de temps pour que la solution converge (documentation)
    gamma_mur = (alpha_mur * delta_t) / (delta_x*delta_y)
    gamma_air = (alpha_air * delta_t) / (delta_x ** 2)
    gamma_cc = (h_cc*delta_t)/(delta_x*rho_air*c_air)

    # Créer une liste de matrice de zéro où res[i] va renvoyer la matrice des température au temps i
    res_mur1 = np.zeros((max_iter_time, hauteur, epaisseur))
    res_mur1.fill(T_int_mur)  # Initialise la température du mur

    res_mur2 = np.zeros((max_iter_time, epaisseur, hauteur))
    res_mur2.fill(T_int_mur)  # Initialise la température du mur

    res_mur3 = np.zeros((max_iter_time, hauteur, epaisseur))
    res_mur3.fill(T_int_mur)  # Initialise la température du mur

    res_mur4 = np.zeros((max_iter_time, epaisseur, hauteur))
    res_mur4.fill(T_int_mur)  # Initialise la température du mur

    # Créer une liste de matrice de zéro où res[i] va renvoyer la matrice des température au temps i
    res_piece = np.empty((max_iter_time, y_piece, x_piece))

    # Initialise la température de la piece
    res_piece.fill(T_int_piece)

    # Mets dans toutes les matrices les conditions aux limites
    res_mur1[0, :, (epaisseur-1)] = (h_cc*delta_x*res_piece[0, :, 0] -
                                     lamb_mur*res_mur1[0, :, (epaisseur-2)])/(lamb_mur+h_cc*delta_x)
    res_mur1[0, :, :1] = T_gauche
    res_mur1[0, :1, :] = T_bas
    res_mur1[0, (hauteur-1):, :] = T_haut

    res_mur2[0, :, (hauteur-1):] = T_haut
    res_mur2[0, :, :1] = T_bas
    res_mur2[0, :1, :] = T_gauche
    res_mur2[0, (epaisseur-1):, :] = (h_cc*delta_x*res_piece[0, y_piece-1, :] -
                                      lamb_mur*res_mur2[0, epaisseur-2, :])/(lamb_mur+h_cc*delta_x)

    res_mur3[0, :, (epaisseur-1):] = T_gauche
    res_mur3[0, :, 0] = (h_cc*delta_x*res_piece[0, :, x_piece-1] -
                         lamb_mur*res_mur3[0, :, 2])/(lamb_mur+h_cc*delta_x)
    res_mur3[0, :1, :] = T_bas
    res_mur3[0, (hauteur-1):, :] = T_haut

    res_mur4[0, :, (hauteur-1):] = T_haut
    res_mur4[0, :, :1] = T_bas
    res_mur4[0, :1, :] = (h_cc*delta_x*res_piece[0, :1, :] -
                          lamb_mur*res_mur2[0, 2, :])/(lamb_mur+h_cc*delta_x)
    res_mur4[0, (epaisseur-1):, :] = T_gauche

    # Résolution avec la méthode des différences finies pour le mur

    # Résolution avec la méthode des différences finies pour la pièce sans chauffage

    def calculate_piece(u, u1, u2, u3, u4, chauffage):
        if chauffage == False:  # test pour savoir si la piece est chauffée
            for k in range(0, max_iter_time-1, 1):  # boucle du temps
                # boucles de calcule de la température au sein du mur
                for i in range(1, hauteur-1, delta_y):
                    for j in range(1, epaisseur-1, delta_x):
                        u1[k + 1, i, j] = gamma_mur * (u1[k][i+1][j] + u1[k][i-1][j] +
                                                       u1[k][i][j+1] + u1[k][i][j-1] - 4*u1[k][i][j]) + u1[k][i][j]
                        u2[k + 1, j, i] = gamma_mur * (u2[k][j+1][i] + u2[k][j-1][i] +
                                                       u2[k][j][i+1] + u2[k][j][i-1] - 4*u2[k][j][i]) + u2[k][j][i]
                        u3[k + 1, i, j] = gamma_mur * (u3[k][i+1][j] + u3[k][i-1][j] +
                                                       u3[k][i][j+1] + u3[k][i][j-1] - 4*u3[k][i][j]) + u3[k][i][j]
                        u4[k + 1, j, i] = gamma_mur * (u4[k][j+1][i] + u4[k][j-1][i] +
                                                       u4[k][j][i+1] + u4[k][j][i-1] - 4*u4[k][j][i]) + u4[k][j][i]

                # boucle de calcule de la température à l'intérieur de la piece
                for i in range(1, y_piece-1, delta_x):
                    for j in range(1, x_piece-1, delta_x):
                        u[k + 1, i, j] = gamma_air * (u[k][i+1][j] + u[k][i-1][j] +
                                                      u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
                # actualisation des nouvelles conditions limites
                # ici pour les murs
                res_mur1[k+1, :, epaisseur-1] = (h_cc*delta_x*res_piece[k, :, 0] +
                                                 lamb_mur*res_mur1[k, :, (epaisseur-2)])/(lamb_mur+h_cc*delta_x)
                res_mur1[k+1, 0, :] = res_mur1[k+1, 1, :]
                res_mur1[k+1, (hauteur-1):, :] = res_mur1[k+1, (hauteur-2), :]

                res_mur2[k+1, :, hauteur-1] = res_mur2[k+1, :, hauteur-2]
                res_mur2[k+1, :, 0] = res_mur2[k+1, :, 1]
                res_mur2[k+1, (epaisseur-1):, :] = (h_cc*delta_x*res_piece[k, y_piece-1, :] +
                                                    lamb_mur*res_mur2[k, epaisseur-2, :])/(lamb_mur+h_cc*delta_x)

                res_mur3[k+1, :, 0] = (h_cc*delta_x*res_piece[k, :, x_piece-1] +
                                       lamb_mur*res_mur3[k, :, 2])/(lamb_mur+h_cc*delta_x)
                res_mur3[k+1, :1, :] = res_mur3[k+1, 1, :]
                res_mur3[k+1, (hauteur-1):, :] = res_mur3[k+1, hauteur-2, :]

                res_mur4[k+1, :, hauteur-1] = res_mur4[k+1, :, hauteur-2]
                res_mur4[k+1, :, 0] = res_mur4[k+1, :, 1]
                res_mur4[k+1, :1, :] = (h_cc*delta_x*res_piece[k, :1, :] +
                                        lamb_mur*res_mur2[k, 2, :])/(lamb_mur+h_cc*delta_x)
                # ici pour la piece
                res_piece[k+1, y_piece-1, :] = res_piece[k, y_piece-1, :] + \
                    gamma_cc*(res_mur1[k+1, :, epaisseur-1] -
                              res_piece[k, (y_piece-1):, :])
                res_piece[k+1, :, 0] = res_piece[k, :, 0] + \
                    gamma_cc*(res_mur2[k+1, epaisseur-1, :]-res_piece[k, :, 0])
                res_piece[k+1, 0, :] = res_piece[k, 0, :] + \
                    gamma_cc*(res_mur3[k+1, :, 0]-res_piece[k, 0, :])
                res_piece[k+1, :, x_piece-1] = res_piece[k, :, x_piece-1] + \
                    gamma_cc*(res_mur4[k+1, 0, :]-res_piece[k, :, x_piece-1])
        else:  # si la piece est chauffée
            x_chauffage = []  # coordonées des chauffages
            y_chauffage = []
            coord_chauffage = []  # ensemble des points appartenant au chauffages
            coord_chauffage1 = []
            for h in range(len(chauffage)):
                x_chauffage.append(
                    [chauffage[h][0][0]-5+i for i in range(11)])
                y_chauffage.append(
                    [chauffage[h][0][1]-5+i for i in range(11)])
                coord_chauffage.append([ele for ele in join(
                    y_chauffage[h], x_chauffage[h]) if (ele[0]-chauffage[h][0][1])**2+(ele[1]-chauffage[h][0][0])**2 < 5*2])
                for [i, j] in coord_chauffage[h]:
                    u[:, i, j] = chauffage[h][1]
                    coord_chauffage1 += coord_chauffage[h]

            for k in range(0, max_iter_time-1, 1):
                for i in range(1, hauteur-1, delta_y):
                    for j in range(1, epaisseur-1, delta_x):
                        u1[k + 1, i, j] = gamma_mur * (u1[k][i+1][j] + u1[k][i-1][j] +
                                                       u1[k][i][j+1] + u1[k][i][j-1] - 4*u1[k][i][j]) + u1[k][i][j]
                        u2[k + 1, j, i] = gamma_mur * (u2[k][j+1][i] + u2[k][j-1][i] +
                                                       u2[k][j][i+1] + u2[k][j][i-1] - 4*u2[k][j][i]) + u2[k][j][i]
                        u3[k + 1, i, j] = gamma_mur * (u3[k][i+1][j] + u3[k][i-1][j] +
                                                       u3[k][i][j+1] + u3[k][i][j-1] - 4*u3[k][i][j]) + u3[k][i][j]
                        u4[k + 1, j, i] = gamma_mur * (u4[k][j+1][i] + u4[k][j-1][i] +
                                                       u4[k][j][i+1] + u4[k][j][i-1] - 4*u4[k][j][i]) + u4[k][j][i]

                for i in range(1, y_piece-1, delta_x):
                    for j in range(1, x_piece-1, delta_x):
                        if (i, j) not in coord_chauffage1:
                            u[k + 1, i, j] = gamma_air * (u[k][i+1][j] + u[k][i-1][j] +
                                                          u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

                res_mur1[k+1, :, epaisseur-1] = (h_cc*delta_x*res_piece[k, :, 0] +
                                                 lamb_mur*res_mur1[k, :, (epaisseur-2)])/(lamb_mur+h_cc*delta_x)
                res_mur1[k+1, 0, :] = res_mur1[k+1, 1, :]
                res_mur1[k+1, (hauteur-1):,
                         :] = res_mur1[k+1, (hauteur-2), :]

                res_mur2[k+1, :, hauteur-1] = res_mur2[k+1, :, hauteur-2]
                res_mur2[k+1, :, 0] = res_mur2[k+1, :, 1]
                res_mur2[k+1, (epaisseur-1):, :] = (h_cc*delta_x*res_piece[k, y_piece-1, :] +
                                                    lamb_mur*res_mur2[k, epaisseur-2, :])/(lamb_mur+h_cc*delta_x)

                res_mur3[k+1, :, 0] = (h_cc*delta_x*res_piece[k, :, x_piece-1] +
                                       lamb_mur*res_mur3[k, :, 2])/(lamb_mur+h_cc*delta_x)
                res_mur3[k+1, :1, :] = res_mur3[k+1, 1, :]
                res_mur3[k+1, (hauteur-1):,
                         :] = res_mur3[k+1, hauteur-2, :]

                res_mur4[k+1, :, hauteur-1] = res_mur4[k+1, :, hauteur-2]
                res_mur4[k+1, :, 0] = res_mur4[k+1, :, 1]
                res_mur4[k+1, :1, :] = (h_cc*delta_x*res_piece[k, :1, :] +
                                        lamb_mur*res_mur2[k, 2, :])/(lamb_mur+h_cc*delta_x)

                res_piece[k+1, y_piece-1, :] = res_piece[k, y_piece-1, :] + \
                    gamma_cc*(res_mur1[k+1, :, epaisseur-1] -
                              res_piece[k, (y_piece-1):, :])
                res_piece[k+1, :, 0] = res_piece[k, :, 0] + \
                    gamma_cc*(res_mur2[k+1, epaisseur -
                                       1, :]-res_piece[k, :, 0])
                res_piece[k+1, 0, :] = res_piece[k, 0, :] + \
                    gamma_cc*(res_mur3[k+1, :, 0]-res_piece[k, 0, :])
                res_piece[k+1, :, x_piece-1] = res_piece[k, :, x_piece-1] + \
                    gamma_cc*(res_mur4[k+1, 0, :] -
                              res_piece[k, :, x_piece-1])

        return u

    # modelechauffage=[[coord,T],....,[coord,T]]

    fig = plt.figure()
    gs = GridSpec(1, 2, figure=fig)

    ax_piece = fig.add_subplot(gs[0, 1])
    plt.xlabel("x")
    plt.ylabel("y")
    ax_piece.set_aspect('equal')

    ax_mur = fig.add_subplot(gs[0, 0])
    ax_mur.set_aspect('equal')

    def plotheatmap(piece_k, mur_k, k):
        # Actualise le temps
        #ax_piece.title(f"Temperature at t = {k*delta_t:.3f} unit time")
        # Plot la matrice
        ax_piece.pcolormesh(piece_k, cmap=plt.cm.jet, vmin=0, vmax=150)
        ax_mur.pcolormesh(mur_k, cmap=plt.cm.jet, vmin=0, vmax=150)
        # ax.colorbar()
        return fig

    # Do the calculation here
    res_piece = calculate_piece(
        res_piece, res_mur1, res_mur2, res_mur3, res_mur4, chauffage)

    def animate(k):
        plotheatmap(res_piece[k], res_mur2[k], k)

    anim = animation.FuncAnimation(
        fig, animate, interval=1, frames=max_iter_time, repeat=False)
    plt.show()

# ======================================================== #

# Test#

# ======================================================== #


# Matériau
lamb_mur = 0.8
rho_mur = 2400
c_mur = 1

lamb_air = 0.024
rho_air = 1.24
c_air = 1005
h_cc = 10

# Caractéristiques de la surface du mur
epaisseur = 10
hauteur = 50

# Caractéristiques de la surface de la piece
x_piece = 50
y_piece = 50


# Conditions aux limites
T_int_piece = 60
T_int_mur = 10
T_droite = 20
T_gauche = 0
T_haut = T_int_mur
T_bas = T_int_mur
#chauffage = False

# Chauffage
chauffage = [[[15, 15], 200], [[35, 35], 200]]

# #Exemple :
# animation_diff(lamb_mur, rho_mur, c_mur, lamb_air, rho_air, c_air, h_cc, epaisseur, hauteur, T_haut,
#                T_bas, T_droite, T_gauche, T_int_mur, T_int_piece, x_piece, y_piece, chauffage)
