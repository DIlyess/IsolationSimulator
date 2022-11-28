import matplotlib.pyplot as plt
from modèle_maison import *


# Trace un mur à l'aide d'une ligne plt entre ses extrémités #

def tracer_mur(mur):
    plt.plot([mur['Xdebut'], mur['Xfin']], [mur['Ydebut'],
                                            mur['Yfin']], lw=mur['epaisseur'], color='k')
    if mur['nb_fenetre'] != 0:
        tracer_fenetre(mur)

# Trace une fenètre ou deux sur un mur donné en faisant apparaitre une ligne blanche 
# centrée sur le milieu du mur (1 fenêtre) ou sur les tiers du mur (2 fenêtres)

def tracer_fenetre(mur):
    if mur['nb_fenetre'] == 1:
        if mur['Orientation'] == 'horizontale':
            plt.plot([(mur['Xdebut']+mur['Xfin'])/2-0.6, (mur['Xdebut']+mur['Xfin']) /
                      2+0.6], [mur['Ydebut'], mur['Yfin']], lw=mur['epaisseur'], color='w')
        else:
            plt.plot([mur['Xdebut'], mur['Xfin']], [(mur['Ydebut']+mur['Yfin'])/2 -
                                                    0.6, (mur['Ydebut']+mur['Yfin'])/2+0.6], lw=mur['epaisseur'], color='w')

    if mur['nb_fenetre'] == 2:
        if mur['Orientation'] == 'horizontale':
            plt.plot([(mur['Xdebut']+mur['Xfin'])/3-0.6, (mur['Xdebut']+mur['Xfin']) /
                      3+0.6], [mur['Ydebut'], mur['Yfin']], lw=mur['epaisseur'], color='w')
            plt.plot([(mur['Xdebut']+mur['Xfin'])*2/3-0.6, (mur['Xdebut']+mur['Xfin'])
                      * 2/3+0.6], [mur['Ydebut'], mur['Yfin']], lw=mur['epaisseur'], color='w')

        else:
            plt.plot([mur['Xdebut'], mur['Xfin']], [(mur['Ydebut']+mur['Yfin'])/3 -
                                                    0.6, (mur['Ydebut']+mur['Yfin'])/3+0.6], lw=mur['epaisseur'], color='w')
            plt.plot([mur['Xdebut'], mur['Xfin']], [(mur['Ydebut']+mur['Yfin'])*2/3 -
                                                    0.6, (mur['Ydebut']+mur['Yfin'])*2/3+0.6], lw=mur['epaisseur'], color='w')

# Trace une maiosn définit comme une liste de mur #

def tracer_maison(maison):
    plt.gca().set_aspect(aspect='equal')  # égalise les échelles ###
    for mur in maison:
        tracer_mur(mur)
    
# Trace une maison définit comme une liste de pièce (plus pratique pour les simulations multipièces) #

def tracer_maison_complete(maison,fig):
    ax = fig.add_subplot(111)
    plt.gca().set_aspect(aspect='equal')  # égalise les échelles ###
    for piece in maison:
        for mur in piece[0] :
            tracer_mur(mur)
    return(ax)


# #Exemple :
# fig=plt.figure()
# tracer_maison_complete(MaisonU,fig)
# plt.show()
