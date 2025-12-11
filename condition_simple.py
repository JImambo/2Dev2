def demander_nombre():
    while True:
        try:
            return float(input("Entrez un nombre : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

def demander_continuer():
    while True:
        reponse = input("Voulez-vous continuer ? (oui/non) : ").lower().strip()
        if reponse in ["oui", "o", "yes", "y"]:
            return True
        elif reponse in ["non", "n", "no"]:
            return False
        else:
            print("Réponse non reconnue. Merci de répondre par oui ou non.")

continuer = True

while continuer:
    nombre = demander_nombre()

    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("zéro")

    continuer = demander_continuer()

print("Programme terminé.")
