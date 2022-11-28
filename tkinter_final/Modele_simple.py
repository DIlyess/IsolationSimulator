import numpy as np
from scipy.integrate import odeint
from modèle_maison import *
from materiaux import *
import matplotlib.pyplot as plt

# constantes :

# Caractéristiques de la maison


h_mur = 2.4
L_fen = 1.2
h_fen = 1.2
e_fen = 0.1
lambda_verre = 1

# Caractéristiques de l'air

rho = 1.2
c_tm = 1000


# Récupération des constantes à partir du modèle

def perimetre(piece):

    [XHD, YHD, XHG, YHG, XBD, YBD, XBG, YBG] = piece[2]
    return(2*(YHD-YBD+XHD-XHG))


def constante(Maison, epa_mur_ext):

    # constante globale #

    # initialisation
    nb_piece = len(Maison)
    Surf = [0]*nb_piece
    Murs = [0]*nb_piece

# On définit les surfaces et les murs de chaque pièce
    for i in range(nb_piece):
        Surf[i] = Maison[i][1]
        Murs[i] = Maison[i][0]

    # voisins #

# création de matrices Mi,j contenant les constantes reliant les pièces i et j
    # Surface du mur séparant les pièces i et j
    Mat_surf = np.zeros((nb_piece+1, nb_piece+1))
    # nombre de fenêtres entre les pièces i et j
    Mat_fen = np.zeros((nb_piece+1, nb_piece+1))
    # caractéristique mur entre les pièces i et j
    Mat_lambda = np.zeros((nb_piece+1, nb_piece+1))
    # épaisseur mur entre les pièces i et j
    Mat_epa = np.ones((nb_piece+1, nb_piece+1))

    for i in range(nb_piece):
        L_tot = 0
        nb_fen_int = 0
        [XHDi, YHDi, XHGi, YHGi, XBDi, YBDi, XBGi, YBGi] = Maison[i][2]
        for j in range(nb_piece):
            if j != i:
                # initialisation
                L_contact = 0
                direction_contact = 5
                # On fait un parcours croisé des pièces pour chercher les contacts entre les pièces i et j et les caractéristiques du contact
                [XHDj, YHDj, XHGj, YHGj, XBDj, YBDj, XBGj, YBGj] = Maison[j][2]
                if YHGi == YBGj:  # contact potentiel au nord
                    inter = [max(XHGi, XBGj), min(XHDi, XBDj)]
                    if inter[0] < inter[1]:   # si il y'a contact
                        L_contact = inter[1]-inter[0]
                        direction_contact = 2
                if XHGi == XHDj:  # contact potentiel à l'ouest
                    inter = [max(YBGi, YBDj), min(YHGi, YHDj)]
                    if inter[0] < inter[1]:
                        L_contact = inter[1]-inter[0]
                        direction_contact = 1
                if YBGi == YHGj:  # contact potentiel au sud
                    inter = [max(XBGi, XHGj), min(XBDi, XHDj)]
                    if inter[0] < inter[1]:
                        L_contact = inter[1]-inter[0]
                        direction_contact = 0
                if XHDi == XHGj:  # contact potentiel à l'est
                    inter = [max(YBDi, YBGj), min(YHDi, YHGj)]
                    if inter[0] < inter[1]:
                        L_contact = inter[1]-inter[0]
                        direction_contact = 3

                Mat_surf[i][j] = L_contact

                if L_contact != 0:

                    Mat_lambda[i][j] = Maison[i][0][direction_contact]['materiaux']['conductivité thermique']
                    Mat_epa[i][j] = Maison[i][0][direction_contact]['epaisseur']
                    Mat_fen[i][j] = Maison[i][0][direction_contact]['nb_fenetre']
        for j in range(nb_piece+1):
            L_tot += Mat_surf[i][j]
            nb_fen_int += Mat_fen[i][j]

        # Données contacts avec l'extérieur par différence
        Mat_surf[i][nb_piece] = perimetre(Maison[i])-L_tot
        Mat_fen[i][nb_piece] = Maison[i][3]-nb_fen_int
        Mat_epa[i][nb_piece] = epa_mur_ext
        Mat_lambda[i][nb_piece] = 0.9

    Mat_surf *= h_mur

    return(nb_piece, Surf, Murs, Mat_surf, Mat_epa, Mat_fen, Mat_lambda)


# modélisation de l'équa diff

def model(T, t, nb_piece, Surf, Murs, Mat_surf, Mat_epa, Mat_fen, Mat_lambda, T_ext, durée, P_chauf):
    dTdt = [0]*nb_piece
    for i in range(nb_piece):
        for j in range(nb_piece):
            if j != i:
                dTdt[i] += (T[j]-T[i])*((Mat_surf[i][j]-L_fen*h_fen*Mat_fen[i][j]) *
                                        Mat_lambda[i][j]/Mat_epa[i][j]+Mat_fen[i][j]*L_fen*h_fen*lambda_verre/e_fen)
        dTdt[i] = (dTdt[i]-(T[i]-T_ext[0])*h_mur*Mat_surf[i][nb_piece]*Mat_lambda[i]
                   [nb_piece]/Mat_epa[i][nb_piece]+P_chauf[i])/(rho*h_mur*Surf[i]*c_tm)

    return dTdt


# résolution

def resolution_simple(T0, durée, nb_piece, Surf, Murs, Mat_surf, Mat_epa, Mat_fen, Mat_lambda, T_ext, P_chauf):
    t = np.linspace(0, durée, durée)
    T = odeint(model, T0, t, args=(nb_piece, Surf, Murs,
               Mat_surf, Mat_epa, Mat_fen, Mat_lambda, T_ext, durée, P_chauf))
    return(T, t)
