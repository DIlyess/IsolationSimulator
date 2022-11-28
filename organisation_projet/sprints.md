# **Sprints du projet isolation d'un maison**

## **Consignes générales**

Pensez à commenter vos codes

Evitez au maximum les variables globales

Essayez de faire des codes avec uniquement des fonctions pour pouvoir créer des modules

Il faudrait autant que possible qu'on fasse nos propres codes

## **Sprint 1 : premier MVP sur matplotlib**

### Objectifs 

S'approprier les équations et le projet

Créer un premier MVP avec les graphes d'évolution de la chaleur et des varaibles argparse

Faire une animation d'un maison avec Matplotlib ??

### Répartition des taches (non définitif)

Ilyess : mise en place des animations matplotlib

Tinaël : création des variables argparse (et le reste parce que c'est pas très long)

Les autres : - écriture des codes de résolution numérique et création des graphes non animé

- chercher les données sur les coûts

## **Sprint 2 : deuxième MVP avec une interface**
 
### Objectifs

Utiliser Tkinter pour créer une interfarce intéractive

Réussir à mettre des graphes

### Répartitions des taches (non définitif)

Antoine FD : Se renseigner sur tkinter et le tracage de rectangle qui constitueront les pièces de la maison. L'utilisateur doit pouvoir tracer ses propres rectangles directement sur l'interface et on doit pouvoir récupérer les coordonnées de ce rectangle (Il me semble avoir vu une fonction tkinter get_cursor qui peut être utile)

Matthieu Antoine : S'occuper de savoir comment on va utiliser tkinter pour que l'utilisateur puisse poser une fenêtre ou un chauffage en un click sur son schéma qu'il aura tracé (les rectangles qui constituent les pièces). On devra en particulier avoir les coordonées du chauffage pour pouvoir adapter l'animation du réchauffement de l'air. Il faudra également imposer la condition que la fenêtre (donc le click de la souris) soit sur un mur, on verra après pr la condition que ce soit un mur extérieur.

Ilyess : Se debrouiller pour savoir comment placer une animation dans tkinter tout en choisissant son emplacement de sorte à ce que ca représente bien la bonne pièce.

Antoine Greil : 

Tinaël :

Julien :


## **Sprint 3 : MVP avec le module de thermo ??**

### Objectfis 

Ce sprint peut être réaliser avant le deuxième

Expérimentation du module de thermodynamique pour savoir si il est utile ou non

