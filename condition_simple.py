continuer = "oui"

while continuer.lower() == "oui":
    nombre: int = int(input("Saisissez un nombre: "))

    if nombre > 0:
        print("Nombre positif")
    elif nombre < 0:
        print("Nombre negatif")
    else:
        print("Zero")
        
    continuer = input("Voulez-vous continuer ? (oui/non) : ")
    
print("Programme terminé")