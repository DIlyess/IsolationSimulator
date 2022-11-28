
from materiaux import*


def def_mur(epa, mat, nb_fen, Xdeb, Xfin, Ydeb, Yfin, Orientation):
    mur = {'epaisseur': epa, 'materiaux': mat, 'nb_fenetre': nb_fen, 'Xdebut': Xdeb,
           'Xfin': Xfin, 'Ydebut': Ydeb, 'Yfin': Yfin, 'Orientation': Orientation}
    return(mur)

def def_piece(XHD,YHD,XHG,YHG,XBD,YBD,XBG,YBG,ext_sone,fen_sone,mat_int,mat_ext):
    mur_sud=def_mur(2+3*ext_sone[0],)


#### Modèles de maisons préenregistrés ####

### Simple pièce avec 1 fenêtre au sud ###


mur_sud1 = def_mur(10, constru['Parpaing'], 1, 0, 50, 0, 0, 'horizontale')
mur_nord1 = def_mur(10, constru['Parpaing'], 0, 0, 50, 50, 50, 'horizontale')
mur_est1 = def_mur(10, constru['Parpaing'], 0, 50, 50, 50, 0, 'verticale')
mur_ouest1 = def_mur(10, constru['Parpaing'], 0, 0, 0, 50, 0, 'verticale')
Maison1_fenetre = [mur_sud1, mur_nord1, mur_est1, mur_ouest1]

mur_sud1 = def_mur(10, constru['Parpaing'], 0, 0, 50, 0, 0, 'horizontale')
mur_nord1 = def_mur(10, constru['Parpaing'], 0, 0, 50, 50, 50, 'horizontale')
mur_est1 = def_mur(10, constru['Parpaing'], 0, 50, 50, 50, 0, 'verticale')
mur_ouest1 = def_mur(10, constru['Parpaing'], 0, 0, 0, 50, 0, 'verticale')
Maison1 = [mur_sud1, mur_nord1, mur_est1, mur_ouest1]


### Maison 4 pièces avec fenêtres ###

mur_sud2 = def_mur(5, constru['Parpaing'], 2, 2, 22, 2, 2, 'horizontale')
mur_nord2 = def_mur(5, constru['Parpaing'], 2, 2, 22, 22, 22, 'horizontale')
mur_est2 = def_mur(5, constru['Parpaing'], 2, 22, 22, 22, 2, 'verticale')
mur_ouest2 = def_mur(5, constru['Parpaing'], 2, 2, 2, 22, 2, 'verticale')
paroi_vert2 = def_mur(5, constru['Parpaing'], 0, 12, 12, 22, 2, 'verticale')
paroi_hor2 = def_mur(5, constru['Parpaing'], 0, 2, 22, 12, 12, 'horizontale')
Maison2 = [mur_ouest2, mur_est2, mur_nord2, mur_sud2, paroi_hor2, paroi_vert2]
