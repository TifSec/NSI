# Initialisation de l'inventaire
inventaire = []

def ajouter_objet(objet):
    inventaire.append(objet) # Ajoute l'objet à l'inventaire
    print(f"{objet} a été ajouté à votre inventaire.")


def retirer_objet(objet):
    if objet in inventaire:
        inventaire.remove(objet) # Retire l'objet de l'inventaire
        print(f"{objet} a été retiré de votre inventaire.")
    else:
        print(f"{objet} n'est pas dans l'inventaire.")


def afficher_inventaire():
    if inventaire:
        print("Votre inventaire contient :")
        for objet in inventaire:
            print("- " + objet) # Affiche chaque objet
    else:
        print("Votre inventaire est vide.")


# Menu principal
while True:
    print("\nMenu :")
    print("1. Ajouter un objet")
    print("2. Retirer un objet")
    print("3. Afficher l'inventaire")
    print("4. Quitter")

    choix = input("Que voulez-vous faire ? (1/2/3/4) : ")

    if choix == "1":
        objet = input("Entrez le nom de l'objet à ajouter : ")
        ajouter_objet(objet)

    elif choix == "2":
        objet = input("Entrez le nom de l'objet à retirer : ")
        retirer_objet(objet)

    elif choix == "3":
        afficher_inventaire()

    elif choix == "4":
        print("Merci d'avoir joué !")
        break

    else:
        print("Choix invalide. Essayez encore.")

# Ok, j'aimerais que tu rajoute une option qui afficherais combien d'objets tu as dans ton inventaire
# Une option qui te demande le nom de l'objet et qui t'affiche combien tu en as (ex : epee -> 4)