# Billets et Pièces : recoinition

## Objectif du projet

L'objectif de ce projet est de concevoir un programme tel qu'en prenant une photo avec un Raspberry Pi de pièces (et de billets) étalées, 
celles-ci sont reconnues et le programme nous donne la somme d'argent totale ainsi que la liste des pièces.

## Résumé du projet

- Entrée : Pièces étalées
- Sortie : Argent total présent et liste des pièces reconnues par le programme
- Matériel : Raspberry Pi avec le module PiCamera

## Deux types de fonctionnements

### Fonctionnement *sans* le Raspberry Pi

Il faut utiliser la fonction *euro_detect.py* présente dans le dossier *euro-coin-detector-master*. 
Cette fonction permet au choix de charger une photo déjà existante ou d'ouvrir la caméra de l'ordinateur pour faire de la reconnaissance en direct

### Fonctionnement *avec* le Raspberry Pi

Il faut utiliser la fonction *photo.py* présente dans le dossier *Coin_recognition*. La prévisualisation de la caméra apparaît alors, avec une fenêtre
disposant de 2 boutons. Il suffit d'appuyer sur le bouton "Photo" pour lancer le programme et afficher les résultats dans la même fenêtre.