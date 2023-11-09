#Cree par Maximilien Cloutier
#Cree en 2023
#Code du TP3

import random


vies = 20
victoires = 0
winstreak = 0
defaites = 0



def regles():
    print("\nBienvenue dans le donjon. Vous allez devoir combattre des monstres de differents niveaux pour affronter le boss du donjon. \n"
          "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n"
          "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n"
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n"
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. \n"
          "\nVoici votre premier monstre")

def menu():
    print("Que voulez-vous faire? \n"
          "1. Combattre cet adversaire \n"
          "2. Contourner cet adversaire et aller ouvrir une autre porte \n"
          "3. Afficher les règles du jeu \n"
          "4. Quitter la partie \n")


def jeu():
    global vies
    global victoires
    global winstreak
    global defaites
    choix = 0
    while vies > 0 and choix != 4:
        force_ennemis = random.randint(1, 5)
        print("Le montre a une puissance de", force_ennemis)
        choix = input(menu())
        if choix == "1":
                attaque = random.randint(1, 6)
                print("Votre attaque a une puissance de", attaque)
                print("Le montre a une puissance de", force_ennemis)
                if attaque > force_ennemis:
                    victoires += 1
                    winstreak += 1
                    vies = vies + force_ennemis
                    print("Vous avez battu le montre, vous avez ganger", force_ennemis, "point(s) de vie")
                    print("Vies:", vies)
                    print("Victoires:", victoires)
                    print("Winstreak:", winstreak)
                    print("Défaites:", defaites)
                elif attaque <= force_ennemis:
                    vies = vies - force_ennemis
                    defaites += 1
                    winstreak = 0
                    print("Votre attaque est trop faible, vous perdez", force_ennemis, "point(s) de vie")
                    print("Vies:", vies)
                    print("Victoires:", victoires)
                    print("Winstreak:", winstreak)
                    print("Défaites:", defaites)

        elif choix == "2":
            print("Vous échaper le monstre, vous perdez 1 point de vie \n"
                  "Il vous reste", vies, "points de vie")
            vies = vies -1
            print("Vous trouvez un autre monstre")

        elif choix == "3":
            print(regles())

        elif choix == "4":
            print("Vous avez quitté le jeu")

        else:
            print("Votre choix n'est pas bon, vieullez ressayer \n")

    if vies <= 0:
        print(" \nVous n'avez plus de points de vie. \n"
              "Vous êtes mort. \nVeuillez recommencer la partie \n Merci d'avoir joué")

    if victoires == 1 or winstreak >= 5:
        print("Vous avez battu assez de mnostres. \n"
              "Le boss est beaucoup plus de vies que les monstres normaux.\n"
              "Il va falloir lui infliger 20 dégats pour le vaincre.\n"
              "Vous avez 3 bouclier, une potion de vie et une épée que vous avez trouvé dans la salle.\n"
              "Les boucliers vous peremttent de bloquer une ataque de boss.\n"
              "La potion de vie vous donne 5 ponits de vie. \n"
              "L'épée vous donne une chance de faire 2 degats de plus")
        vies_boss = 20
        attaque_boss = random.randint(1, 10)
        boucliers = 3
        potion_vie = 1
        choix2 = input("Vieullez choisir une action:\n"
                       "1- Attaquer le boss\n"
                       "2- Bloquer l'attaque du boss\n"
                       "3- Utiliser la potion de vie")
        if choix2 == "1":
            print("Vous attaquer le boss")
            attaque2 = random.randint(1, 6) +2
            print("Votre attaque a une puissance de", attaque2)
            print("Le boss perd", attaque2, "point(s) de vie")
            vies_boss = vies_boss - attaque2
        elif choix2 == "2":
            if boucliers == 0:
                print("Vous nàvez plus de bouclier.\n"
                      "Ovus bloquer rien.\n"
                      "Le boss vous attque.\n")
            boucliers -= 1
            print("Vous utiliser un bouclier.\n"
                  "Il vous reste", boucliers, "bouclier(s)")
        elif choix2 == "3":
            if potion_vie == 0:
                print("Vous buvez une potion vide.\n"
                      "Rien ne se passe.\n"
                      "Le boss vous attque.\n")
            else:
                print("Vous utiliser une potion de vie")
                vies = +5
                potion_vie = 0
        else:
            print("Vous ne faites rien.\n"
                  "le boss vous attque.\n")




regles()
jeu()
