# ProjetGraphesS2
Projet Graphes Semestre 2 BUT INFO 

# Membres du groupes : 

- Erwan ERNY S2A2
- Esteban DUBOIS S2A2

# Projet :

Création d'un graphe représentant les lignes de métro Tokyoïtes ainsi que les JR lines. Et création d'un système de parcours de graphe pour trouver le chemin le plus court entre deux stations.

# Caractéristique du projet

- Graphe non orientié, cela permet d'aller d'une station à une autre dans les deux sens possible
- Graphe non pondéré, le graphe ne prend pas en compte la distance en temps et en kilomètre entre deux gares

Théorie des graphes utilisée : Breadth-First Search (BFS).
L'algorithme part d'une station de départ et explore toutes les stations à 1 arrêt de distance puis à 2 arrêts de distance
et ce jusqu'à trouver le chemin le plus court pour aller jusqu'à la station cible

# Exemple d'utilisation

1) Utiliser le graphe généré au lancement du code ou le fichier texte avec la liste des stations
afin de trouver une station de départ et une station d'arrivée
<img width="1424" height="727" alt="image" src="https://github.com/user-attachments/assets/96106b6e-287a-478e-9fcd-1a0e10a86982" />

2) Renseigner la station d'arrivée et de départ dans le terminal                                                                                                 

<img width="258" height="60" alt="image" src="https://github.com/user-attachments/assets/5a1e08c0-3759-483d-b379-fa0a7e231a46" />

3) observer le chemin trouvé
   <img width="1664" height="992" alt="image" src="https://github.com/user-attachments/assets/8bf438fb-285b-4f72-8aa6-1879d8f73aa6" />

