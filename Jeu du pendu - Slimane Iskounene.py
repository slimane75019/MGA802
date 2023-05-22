import random

def choisir_mot():
    with open("mots_pendu.txt", 'r') as f:
        mot = f.readlines()
    return random.choice(mot).strip()

def affichage_mot(mot_a_deviner, lettres_donnees):
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

    while tentatives > 0:
        lettre = input("Entrez une lettre : \n")

        if lettre in lettres_donnees:
            print("Vous avez déjà deviné cette lettre.")

        elif lettre in mot_a_deviner:
            lettres_donnees.append(lettre)
            mot_affiche = affichage_mot(mot_a_deviner, lettres_donnees)
            print(mot_affiche)

            if "_" not in mot_affiche:
                print("Félicitation ! Vous avez deviné le mot secret :", mot_a_deviner)
                return

        else:
            tentatives -= 1
            print("La lettre", lettre, "n'est pas dans le mot.")
            print("Tentatives restantes :", tentatives)

    print("Dommage ! Vous avez perdu ! Le mot secret était :", mot_a_deviner)

jeu_pendu()





