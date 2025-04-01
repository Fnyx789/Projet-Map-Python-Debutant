import json
import os 
from random import *

# charger_partie()

# Variables
couleurs = ['Cœur', 'Carreau', 'Trefle', 'Pique']
valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

deck = [(v, c) for v in valeurs for c in couleurs]  # Création d'un jeu de 54 cartes
deck_shuffle = []
paquet_pose = []

nombre_tour = 0

carte_deck = 10
sauv_tour = 5

nombre_joueur = int(input("saisissez le nombre de joueur (entre 3 et 4 joueurs) \n"))
main_joueurs = {}

joueur_actuel = 0

verif = False

# Fonction

def melanger():
    """
    Fonction qui va permettre de mélanger aléatoirement le paquet de carte à l'aide de la bibliothèque random
    """
    global deck_shuffle
    deck_shuffle = deck.copy()
    shuffle(deck_shuffle)

def attribution_deck():
    """
    Variables:
    nv_main = nouvelle main
    main_joueurs = dictionnaire contenant les mains de tous les joueurs

    fonction qui va permettre la distribution des mains des joueurs, et supprimer les cartes distribués du paquet initiale
    """
    melanger()
    for k in range(nombre_joueur):
        nv_main = f"main_joueur_{k+1}"
        main_joueurs[nv_main] = []
        for i in range(carte_deck):
            main_joueurs[nv_main].append(deck_shuffle[i])
            for carte in main_joueurs[nv_main]:
                if carte in deck_shuffle:
                    deck_shuffle.remove(carte)

def afficher_carte():
    """
    Variables:
    main_joueurs[f"main_joueur_{joueur_actuel}" -> main du joueur actuel (stockée dans le dictionnaire)

    Fonction qui va permettre d'afficher la main du joueur actuel à chaque fois que c'est à lui de jouer
    """
    print(main_joueurs[f"main_joueur_{joueur_actuel}"])

def verif_win():
    """
    Variables:
    couleurs -> liste contenant toutes les couleurs du jeu
    main_joueurs[f"main_joueur_{joueur_actuel}" -> main du joueur actuel (stockée dans le dictionnaire)
    verif -> variable qui contient un booléen de si le jouer actuel à gagner.

    Fonction qui va vérifié si un joueur à gagner en ayant une unique couleur commune à toutes ses cartes
    """
    global verif
    for e in main_joueurs[f"main_joueur_{joueur_actuel}"]:
        for c in couleurs:
            if c not in e:
                break
        else:
            verif = True
        


def tour_joueur():
    """
    Variables:
    joueur_actuel -> joueur qui est actuellement en train de jouer
    main_joueurs[f"main_joueur_{joueur_actuel}" -> main du joueur actuel (stockée dans le dictionnaire)

    Fonction qui va déterminé à quel joueur il est le tour de jouer
    """
    global joueur_actuel
    if joueur_actuel == 0 or joueur_actuel >= nombre_joueur:
        joueur_actuel = 1
    else:
        joueur_actuel += 1
    print(f"tour du joueur {joueur_actuel}")
    print("Voici votre paquet:", main_joueurs[f"main_joueur_{joueur_actuel}"])

def choix_tirage():
    """
    Variables:
    c -> choix du joueur de si il veut tirer une carte du paquet ou la dernière carte déposée
    derniere carte -> derniere carte du paquet pose
    paquet_pose -> défosse
    main_joueurs[f"main_joueur_{joueur_actuel}" -> main du joueur actuel (stockée dans le dictionnaire)
    nombre_tour -> nombre de tour jouer
    deck_shuffle -> paquet mélangé de carte 
    dernière carte -> derniere carte déposé par le joueur précédent

    Fonction qui demande au joueur si il souhaite tirer une carte du paquet ou prendre la derniere carte posée
    De plus, celle ci sauvegarde la partie tout les sauv_tour
    """
    global derniere_carte

    tour_joueur()
    if not deck_shuffle:
        deck_shuffle.extend(paquet_pose)
        paquet_pose = []
        derniere_carte = None
    
    if nombre_tour % sauv_tour == 0:  # Sauvegarder toutes les 5 tours 
        sauvegarder_partie()
    derniere_carte = deck_shuffle[-1]
    c = int(input("Choisissez 1 pour tirer pour prendre une carte du paquet\n\tChoisissez 2 pour prendre la dernière carte posée\n" if nombre_tour > 0 else "Choisissez 1 pour tirer pour prendre une carte du paquet\n"))
    if c == 1 and deck_shuffle:
        main_joueurs[f"main_joueur_{joueur_actuel}"].append(derniere_carte)
        print("Carte reçu: \t", derniere_carte)
        deck_shuffle.pop()  
    elif c == 2 and paquet_pose:
        main_joueurs[f"main_joueur_{joueur_actuel}"].append(paquet_pose[-1])  
        paquet_pose.pop()  
        deck_shuffle.pop()
    else:
        print("Option impossible")
    
    verif_win()
    choix_depot()
    os.system("cls") 
    

def choix_depot():
    """
    Variables:
    jouer_actuel -> joueur à qui c'est le tour de jouer
    i -> indice de la carte à déposer dans la défosse
    main_joueurs[f"main_joueur_{joueur_actuel}" -> main du joueur actuel (stockée dans le dictionnaire)
    nombre_tour -> nombre de tour jouer
    paquet_pose -> défosse

    Fonction qui permet au joueur de déposer la carte de son choix
    """
    global nombre_tour
    if len(main_joueurs[f"main_joueur_{joueur_actuel}"]) == 11:
        print("Voici votre jeu \n \t ")
        afficher_carte()
        i = int(input("Donnez l'indice de la carte que vous voulez déposer: 0 étant la première carte et 10 la dernière de votre paquet de 11 cartes\n"))
        print("La dernière carte du paquet est", derniere_carte)
        paquet_pose.append(main_joueurs[f"main_joueur_{joueur_actuel}"][i])
        main_joueurs[f"main_joueur_{joueur_actuel}"].remove(main_joueurs[f"main_joueur_{joueur_actuel}"][i])
    nombre_tour += 1

def sauvegarder_partie():
    """
    Entrée: Données de la partie
    Sortie: Fichier JSON contenant toutes ces données de manière structurée
    """
    data = {
        "deck_shuffle": deck_shuffle,
        "paquet_pose": paquet_pose,
        "nombre_tour": nombre_tour,
        "carte_deck": carte_deck,
        "nombre_joueur": nombre_joueur,
        "main_joueurs": main_joueurs,
        "joueur_actuel": joueur_actuel,
        "verif": verif
    }
    with open("sauvegarde_partie.json", "w") as fichier:
        json.dump(data, fichier, indent = 4)


def charger_partie():
    """
    Entrée: Fichier JSON contenant toutes les données de la partie 
    Sortie: Partie en cours contenant toutes les données (decks...) de la partie précédement chargée
    """
    global deck_shuffle, paquet_pose, nombre_tour, carte_deck, nombre_joueur, main_joueurs, joueur_actuel, verif

    with open("sauvegarde_partie.json", "r") as fichier:
        data = json.load(fichier)

    deck_shuffle = data["deck_shuffle"]
    paquet_pose = data["paquet_pose"]
    nombre_tour = data["nombre_tour"]
    carte_deck = data["carte_deck"]
    nombre_joueur = data["nombre_joueur"]
    main_joueurs = data["main_joueurs"]
    joueur_actuel = data["joueur_actuel"]
    verif = data["verif"]

def partie_de_jeu():  
    print("Distribution des cartes")
    attribution_deck()

    while not verif :   # Boucle qui permet de jouer tant que personne n'a gagné
        choix_tirage()

    print("Le joueur", joueur_actuel, "a gagné!")   




# Main

partie_de_jeu()
