import matplotlib.pyplot as plt
from modèle_maison2 import *
#from variables import*


# def def_mur(epa,mat,nb_fen,Xdeb,Xfin,Ydeb,Yfin,Orientation):
#     mur={'epaisseur':epa,'materiaux':mat,'nb_fenetre':nb_fen,'Xdebut':Xdeb,'Xfin':Xfin,'Ydebut':Ydeb,'Yfin':Yfin,'Orientation':Orientation}
#     return(mur)


def tracer_mur(mur):
    plt.plot([mur['Xdebut'], mur['Xfin']], [mur['Ydebut'],
                                            mur['Yfin']], lw=mur['epaisseur'], color='k')
    if mur['nb_fenetre'] != 0:
        tracer_fenetre(mur)


def tracer_fenetre(mur):
    if mur['nb_fenetre'] == 1:
        if mur['Orientation'] == 'horizontale':
            plt.plot([(mur['Xdebut']+mur['Xfin'])/2-5, (mur['Xdebut']+mur['Xfin']) /
                      2+5], [mur['Ydebut'], mur['Yfin']], lw=mur['epaisseur'], color='w')
        else:
            plt.plot([mur['Xdebut'], mur['Xfin']], [(mur['Ydebut']+mur['Yfin'])/2 -
                                                    5, (mur['Ydebut']+mur['Yfin'])/2+5], lw=mur['epaisseur'], color='w')

    if mur['nb_fenetre'] == 2:
        if mur['Orientation'] == 'horizontale':
            plt.plot([(mur['Xdebut']+mur['Xfin'])/3-5, (mur['Xdebut']+mur['Xfin']) /
                      3+5], [mur['Ydebut'], mur['Yfin']], lw=mur['epaisseur'], color='w')
            plt.plot([(mur['Xdebut']+mur['Xfin'])*2/3-5, (mur['Xdebut']+mur['Xfin'])
                      * 2/3+5], [mur['Ydebut'], mur['Yfin']], lw=mur['epaisseur'], color='w')

        else:
            plt.plot([mur['Xdebut'], mur['Xfin']], [(mur['Ydebut']+mur['Yfin'])/3 -
                                                    1.5, (mur['Ydebut']+mur['Yfin'])/3+1.5], lw=mur['epaisseur'], color='w')
            plt.plot([mur['Xdebut'], mur['Xfin']], [(mur['Ydebut']+mur['Yfin'])*2/3 -
                                                    1.5, (mur['Ydebut']+mur['Yfin'])*2/3+1.5], lw=mur['epaisseur'], color='w')


def tracer_maison(maison):
    plt.gca().set_aspect(aspect='equal')  # égalise les échelles ###
    for mur in maison:
        tracer_mur(mur)
    


# def tracer_maison():
#     plt.gca().set_aspect(aspect = 'equal')         ### égalise les échelles ###
#     X_int = [0, args.L, args.L, 0, 0]
#     Y_int = [0, 0, args.l, args.l, 0]
#     plt.plot(X_int,Y_int, color='k')
#     X_ext = [-args.epa, args.L+args.epa, args.L+args.epa, -args.epa, -args.epa]
#     Y_ext = [-args.epa, -args.epa, args.l+args.epa, args.l+args.epa, -args.epa]
#     plt.plot(X_ext,Y_ext, color='k')
#     plt.show()


# tracer_maison()

# tracer_maison(Maison2)
# plt.show()