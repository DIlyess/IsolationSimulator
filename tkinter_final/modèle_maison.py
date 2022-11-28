from materiaux import*

### Création d'une fonction qui permet de créer des murs avec différents matériaux, position, orientation... ###
def def_mur(epa, mat, nb_fen, Xdeb, Xfin, Ydeb, Yfin, Orientation):
    mur = {'epaisseur': epa, 'materiaux': mat, 'nb_fenetre': nb_fen, 'Xdebut': Xdeb,
           'Xfin': Xfin, 'Ydebut': Ydeb, 'Yfin': Yfin, 'Orientation': Orientation}
    return(mur)


### Création d'une fonction qui permet de créer des pièces tout en récupérant des données importantes pour le tracé et l'animation ###
''' XHD, YHD, XHG, YHG, XBD, YBD, XBG, YBG sont les coordonnées des 4 coins de la pièce
ext_sone permet de renseigner les côtés de la pièce en contact avec l'extérieur dans l'ordre Sud-Ouest-Nord-Est (liste,1=contact)
fen_sone permet de renseigner le nombre de fenêtre sur chaque côté (liste S-O-N-E)
mat_sone permet de renseigner le matériau utilisé pour chaque côté (liste S-O-N-E)
'''
def def_piece(XHD, YHD, XHG, YHG, XBD, YBD, XBG, YBG, ext_sone, fen_sone, mat_sone, nom):
    mur_sud = def_mur(2+ext_sone[0]*3, mat_sone[0],
                      fen_sone[0], XBG, XBD, YBG, YBD, 'horizontale')
    mur_ouest = def_mur(2+ext_sone[1]*3, mat_sone[1],
                        fen_sone[1], XBG, XHG, YBG, YHG, 'verticale')
    mur_nord = def_mur(2+ext_sone[2]*3, mat_sone[2],
                       fen_sone[2], XHG, XHD, YHG, YHD, 'horizontale')
    mur_est = def_mur(2+ext_sone[3]*3, mat_sone[3],
                      fen_sone[3], XHD, XBD, YHD, YBD, 'verticale')
    Surf = (YHD-YBD)*(XBD-XBG)
    nb_fen_tot = fen_sone[0]+fen_sone[1]+fen_sone[2]+fen_sone[3]
    return [[mur_sud, mur_ouest, mur_nord, mur_est], Surf, [XHD, YHD, XHG, YHG, XBD, YBD, XBG, YBG], nb_fen_tot, nom]





#### Modèles de maisons préenregistrés ####

### Simple pièce avec 1 fenêtre au sud ###
mur_sud1 = def_mur(10, constru['Parpaing'], 1, 0, 50, 0, 0, 'horizontale')
mur_nord1 = def_mur(10, constru['Parpaing'], 0, 0, 50, 50, 50, 'horizontale')
mur_est1 = def_mur(10, constru['Parpaing'], 0, 50, 50, 50, 0, 'verticale')
mur_ouest1 = def_mur(10, constru['Parpaing'], 0, 0, 0, 50, 0, 'verticale')
Maison1_fenetre = [mur_sud1, mur_nord1, mur_est1, mur_ouest1]


### Maison 4 pièces avec fenêtres ###

mur_sud2 = def_mur(5, constru['Parpaing'], 2, 2, 22, 2, 2, 'horizontale')
mur_nord2 = def_mur(5, constru['Parpaing'], 2, 2, 22, 22, 22, 'horizontale')
mur_est2 = def_mur(5, constru['Parpaing'], 2, 22, 22, 22, 2, 'verticale')
mur_ouest2 = def_mur(5, constru['Parpaing'], 2, 2, 2, 22, 2, 'verticale')
paroi_vert2 = def_mur(5, constru['Parpaing'], 0, 12, 12, 22, 2, 'verticale')
paroi_hor2 = def_mur(5, constru['Parpaing'], 0, 2, 22, 12, 12, 'horizontale')
Maison2 = [mur_ouest2, mur_est2, mur_nord2, mur_sud2, paroi_hor2, paroi_vert2]


### Villa ###

Salon = def_piece(7, 14, 2, 14, 7, 2, 2, 2, [1, 1, 1, 0], [1, 2, 1, 0], [
                  constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Salon')
SdB = def_piece(10, 8, 7, 8, 10, 2, 7, 2, [1, 0, 0, 0], [1, 0, 0, 0], [
                constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'SdB')
Chambre1 = def_piece(13, 8, 10, 8, 13, 2, 10, 2, [1, 0, 0, 0], [1, 0, 0, 0], [
                     constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Chambre1')
Chambre2 = def_piece(17, 8, 13, 8, 17, 2, 13, 2, [1, 0, 0, 1], [1, 0, 0, 1], [
                     constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Chambre2')
Couloir = def_piece(17, 10, 7, 10, 17, 8, 7, 8, [0, 0, 0, 1], [0, 0, 0, 0], [
                    constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Couloir')
SaM = def_piece(13, 14, 7, 14, 13, 10, 7, 10, [0, 0, 0, 0], [0, 0, 0, 0], [
                constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'SaM')
Cuisine = def_piece(13, 18, 7, 18, 13, 14, 7, 14, [0, 1, 1, 1], [0, 1, 1, 1], [
                    constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Cuisine')
Entrée = def_piece(17, 14, 13, 14, 17, 10, 13, 10, [0, 0, 1, 1], [0, 0, 0, 0], [
                   constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Entrée')

MaisonC = [Salon, SdB, Chambre1, Chambre2, SaM, Cuisine, Entrée, Couloir]


### Maison en L ###

HallL = def_piece(11, 10, 7, 10, 11, 7, 7, 7, [0, 1, 0, 0], [0, 0, 0, 0], [
                  constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Hall')
SdBL = def_piece(15, 15, 13, 15, 15, 12, 13, 12, [0, 0, 1, 1], [0, 0, 0, 1], [
                 constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'SdB')
ChambreL = def_piece(15, 12, 11, 12, 15, 7, 11, 7, [0, 0, 0, 1], [0, 0, 0, 1], [
                     constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Chambre')
GarageL = def_piece(15, 7, 7, 7, 15, 2, 7, 2, [1, 1, 0, 1], [0, 0, 0, 0], [
                    constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Garage')
ChiottesL = def_piece(9, 12, 7, 12, 9, 10, 7, 10, [0, 0, 0, 0], [0, 0, 0, 0], [
                      constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'WC')
CuisineL = def_piece(11, 15, 7, 15, 11, 12, 7, 12, [0, 0, 1, 0], [0, 0, 1, 0], [
                     constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Cuisine')
SalonL = def_piece(7, 15, 2, 15, 7, 10, 2, 10, [1, 1, 1, 0], [1, 1, 1, 0], [
                   constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Salon')
CellierL = def_piece(13, 15, 11, 15, 13, 12, 11, 12, [0, 0, 1, 0], [0, 0, 0, 0], [
                     constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'Cellier')
couloirL = def_piece(11, 12, 9, 12, 11, 10, 9, 10, [0, 0, 0, 0], [0, 0, 0, 0], [
                     constru['Parpaing'], constru['Parpaing'], constru['Parpaing'], constru['Parpaing']], 'couloir')

MaisonL = [HallL, SdBL, ChambreL, GarageL,
           ChiottesL, CuisineL, SalonL, CellierL, couloirL]

### Villa U ###

SalonU=def_piece(16,15,7,15,16,9,7,9,[1,0,1,0],[1,0,1,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Salon')
SdBU1=def_piece(24,9,21,9,24,6,21,6,[0,0,0,1],[0,0,0,1],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'SdB1')
SdBU2=def_piece(5,10,2,10,5,7,2,7,[0,1,0,0],[0,1,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'SdB2')
WCU1=def_piece(24,15,21,15,24,13,21,13,[0,0,1,1],[0,0,0,1],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'WC1')
WCU2=def_piece(5,12,2,12,5,10,2,10,[0,1,0,0],[0,0,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'WC2')
ChambreU1=def_piece(24,6,19,6,24,2,19,2,[1,1,0,1],[1,1,0,1],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Chambre1')
ChambreU2=def_piece(7,7,2,7,7,2,2,2,[1,1,0,1],[1,2,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Chambre2')
ChambreU3=def_piece(24,13,21,13,24,9,21,9,[0,0,0,1],[0,0,0,1],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Chambre2')
CouloirU1=def_piece(21,15,19,15,21,9,19,9,[0,0,1,0],[0,0,1,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Hall1')
CouloirU2=def_piece(7,15,5,15,7,9,5,9,[0,0,1,0],[0,0,1,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Hall2')
CuisineU=def_piece(19,13,16,13,19,9,16,9,[1,0,0,0],[1,0,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Cuisine')
EntréeU=def_piece(19,15,16,15,19,13,16,13,[0,0,1,0],[0,0,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Entrée')
CellierU=def_piece(5,15,2,15,5,12,2,12,[0,1,1,0],[0,0,1,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'Cellier')
HallChambreU1=def_piece(21,9,19,9,21,6,19,6,[0,1,0,0],[0,0,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'')
HallChambreU2=def_piece(7,9,5,9,7,7,5,7,[0,0,0,1],[0,0,0,0],[constru['Parpaing'],constru['Parpaing'],constru['Parpaing'],constru['Parpaing']],'')

MaisonU=[SalonU,SdBU1,SdBU2,WCU1,WCU2,ChambreU1,ChambreU2,ChambreU3,CouloirU1,CouloirU2,CuisineU,EntréeU,CellierU,HallChambreU1,HallChambreU2]

