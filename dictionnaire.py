etudiant = {
    "nom" : "nom",
    "age" : "18",
    "notes" : [12, 5, 16, 14]
}

print("Liste des notes : ", etudiant["notes"])
print("Nombre de notes : ", len(etudiant["notes"]))
print("moyenne des notes ", int(sum(etudiant) / len(etudiant["notes"])))