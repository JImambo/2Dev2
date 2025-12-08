
while True: 
    try:
        age_str = input(" Quel est votre age ? ")
        age: int = int(age_str)
        if age < 0 : 
            print("L'âge ne peut pas être negatif")
            continue
        break
        
    except ValueError:
        print("Veuillez saisir un nombre")
        
annee_naissance = 2025 - age
print("Tu es né(e) en", annee_naissance)
        