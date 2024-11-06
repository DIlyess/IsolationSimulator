# **Projet des Coding-Weeks 2021-2022 du groupe Kunseuh.**

Ce projet est le projet de simulation physique des Coding-Weeks 2022 de CentraleSupélec.

## **Le projet**

Le but de ce projet est d'établir la modélisation d'un sytsème thermodynamique grâce à une interface graphique dans laquelle l'on pourrait moduler les différents paramètres de notre système, tout en observant les changements que cela entraîne sur les variables du problèmes.

On se propose donc d'étudier l'évolution de la température au sein d'une maison, dont le volume peut varier, en fonction de divers paramètres tels que l'épaisseur des murs, la présence d'isolant, la température extérieure, ainsi que le système de chauffe propre à la maison. Le programme permettrait alors d'avoir une idée du coût en chauffage pour une période spécifique de l'année, ou bien de trouver le meilleur compromis entre isolant et chauffage.

## **Maquette du produit final**

Voici ce que le produit final pourra faire dans l'idéal:

- Pouvoir afficher d'une part le schéma de la maison vu de dessus avec dans chaque pièce une animation en temps réel qui précise la température dans chaque endroit de la pièce.
- Pouvoir la température d'un mur selectionné par l'utilisateur par un clic.
- Proposer le choix de l'épaisseur des murs ainsi que du matériau parmi une sélection de matériaux.
- Proposer le choix de placer, ou non, un chauffage dans une pièce (on pourra peut-être regler la température de ces chauffages)


![image](https://github.com/user-attachments/assets/9eab4d42-8e73-43ec-b696-1d0b08682097)

![image](https://github.com/user-attachments/assets/af973aec-fb67-48f1-93e5-b4e0e04be3a9)

![image](https://github.com/user-attachments/assets/ad4e9bd1-6a25-4e0a-8862-35d94750b225)


Tout ce qui précède constitue le Jalon 2 : phase d'analyse et de besoins.

## **Comment executer le programme**

Executer le fichier menu.py qui se trouve dans le dossier tkinter_final et laissez vous guider par l'interface utilisateur ! 

N'hésitez pas à mettre l'interface en plein écran afin de pouvoir voir tous les boutons.

Il se peut que la simulation tarde à apparaître, ceci est lié au long temps de calcul.

Pour les autres fichiers exécutables seuls du dossier tkinter_final :  
    - anim_multipeces.py : il suffit de décommenter les lignes 73 à 81 pour avoir un premier aperçu de l'animation et une aide concernant les arguments du code.  
    - anim_matthieu.py : il suffit de décommenter les lignes 282,283,284 pour avoir un premier aperçu de l'animation.  
    - trace_maison.py : il suffit de décommenter les lignes 56 à 59, pour avoir un aperçu du tracé d'une maison.  
    

## **Les membres du groupe Kunseuh :**

Ilyess Doragh

Tinaël Gelpe 

Antoine Greil

Antoine Faivre-Duboz

Matthieu Antoine

Julien Gombert

## **Pour suivre le déroulé du projet**

### **Objectif 1 : Une animation simple sous matplotlib**
- [**Fonctionnalité 1** : Calcul de la température dans la pièce au cours du temps](jalons_et_fct/fct_1.md)
- [**Fonctionnalité 2** : Affichage de l'animation sous matplotlib](jalons_et_fct/fct_2.md)


### **Objectif 2 : Rendre le projet plus réaliste et tenir compte des conditions aux limites en faisant le lien entre mur et pièce** 
- [**Fonctionnalité 3** : Calcul de l'évolution de la température dans le mur ](jalons_et_fct/fct_3.md)
- [**Fonctionnalité 4** : Mettre en lien la pièce et le mur et afficher la pièce](jalons_et_fct/fct_4.md)
- [**Fonctionnalité 5** : Créer une figure regroupant l'animation à la fois pour le mur et pour la pièce afin de mieux visualiser le phénomène](jalons_et_fct/fct_5.md)


### **Objectif 3 : Utilisation de tkinter pour proposer une première possibilité de paramétrage du problème**

- [**Fonctionnalité 6** : Créer un bouton qui permet d'afficher l'animation dans tkinter ](jalons_et_fct/fct_6.md)
- [**Fonctionnalité 7** :  Créer des curseurs qui permettent de parametrer la maison pour ensuite lancer l'animation](jalons_et_fct/fct_7.md)

### **Objectif 4 : Réaliser une simulation avec 2 pièces collées**

- [**Fonctionnalité 8** : Calcul ](jalons_et_fct/fct_8.md)


## **Dossier simulation maison**

- On y retrouve les differentes versions de la maison le modele trois étant le plus aboutit physiquement parlant mais ayant un temps d'execution trop grand le rendant inutilisable ici. Des exemple de simulations sont proposées sous formes de gif dans ce dossier.


