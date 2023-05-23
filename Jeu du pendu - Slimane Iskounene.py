import random

def choisir_mot():                                     #Cette fonction sélectionne un mot au hasard dans la listes de mots fournie
    with open("mots_pendu.txt", 'r') as f:
        mot = f.readlines()
    return random.choice(mot).strip()

def affichage_mot(mot_a_deviner, lettres_donnees):    #A chaque essai, le mot sera affichée avec les lettres trouvées et/ou des '_'
    mot_affiche=''
    for lettre in mot_a_deviner:
        if lettre in lettres_donnees:
            mot_affiche+=lettre
        else:
            mot_affiche+='_'
    return mot_affiche

def jeu_pendu():
    mot_a_deviner = choisir_mot()
    lettres_donnees = []
    tentatives = 6

    print("Bienvenue au jeu du pendu !")
    print(affichage_mot(mot_a_deviner, lettres_donnees))

    while tentatives > 0:                                     #tant qu'il a encore des chances restantes, l'utilisateur peut donner une lettre
        lettre = input("Entrez une lettre : \n")

        if lettre in lettres_donnees:                         
            print("Vous avez déjà deviné cette lettre.")

        elif lettre in mot_a_deviner:                         #si la lettre donnée est dans le mot, elle sera ajouté au mot affiché et remplacera un des '_'
            lettres_donnees.append(lettre)
            print(affichage_mot(mot_a_deviner, lettres_donnees))

            if "_" not in mot_affiche:                         #si toutes les lettres ont été devinées, l'utilisateur a gagné
                print("Félicitation ! Vous avez deviné le mot secret :", mot_a_deviner)
                return

        else:                                                  #si la lettre n'est pas dans le mots, l'utilisateur perd une chance
            tentatives -= 1
            print("La lettre", lettre, "n'est pas dans le mot.")
            print("Tentatives restantes :", tentatives)

    print("Dommage ! Vous avez perdu ! Le mot secret était :", mot_a_deviner)

jeu_pendu()





