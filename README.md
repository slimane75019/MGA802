# Jeu du pendu

D'abord, mon programme va chercher aléatoirement un mot dans le fichier contenant pleins d'autres mots
Ensuite, il va créer une fonction que l'on va utiliser plus tard. Cette fonction va afficher des "_" et/ou des lettres dépendemment si l'utilisateur à trouvé une lettre du mot.
Le jeu du pendu peut alors commencer.
L'utilisateur a 6 chances. A chaque fois qu'il donne une lettre, il y a plusieurs possibilités:
-la lettre est dans le mot, elle va alors remplacer un des '_' dans sa position dans le mot
-la lettre n'est pas dans le mot. L'utilisateur perd alors une chance
-l'utilisateur n'a pas reussi à trouver toutes les lettres du mot au bout de 6 essais: c'est perdu
-l'utilisateur a reussi à trouver toutes les lettres du mot avant les 6 essais: c'est gagné
