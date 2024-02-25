import csv
import random

def charger_verbes_irreguliers(chemin_fichier):
    verbes_irreguliers = []
    with open(chemin_fichier, newline='', encoding='utf-8') as csvfile:
        lecteur = csv.reader(csvfile)
        for ligne in lecteur:
            verbes_irreguliers.append(tuple(ligne))
    return verbes_irreguliers

def interroger_utilisateur(verbes_irreguliers, nombre_de_verbes):
    score = 0
    random.shuffle(verbes_irreguliers)
    #print(verbes_irreguliers)
    
    nombre_de_verbes_interroges = 0
    verbes_a_revoir = []
    for en, fr in verbes_irreguliers:
        reponse_utilisateur = input(f"\r\nTraduisez le verbe '{fr}' en français : ")
        if reponse_utilisateur.lower() == en.lower():
            print("Correct !")
            score += 1
        else:
            print(f"Incorrect. La réponse correcte est : '{en}'")
            verbes_a_revoir.append(fr + ' --> ' + en)
        nombre_de_verbes_interroges += 1
        if nombre_de_verbes_interroges >= nombre_de_verbes: break
    
    print(f"\nScore final : {score}/{nombre_de_verbes_interroges}")
    if score < nombre_de_verbes_interroges:
        print("Verbes à revoir:")
        [print(verbe) for verbe in verbes_a_revoir]

if __name__ == "__main__":
    chemin_fichier_csv = "list_verbs.csv"  # Remplacez par le chemin réel de votre fichier CSV
    verbes_irreguliers = charger_verbes_irreguliers(chemin_fichier_csv)
    
    if verbes_irreguliers:
        nombre_de_verbes = int(input("Combien de verbes pour l'interrogation ?\r\n"))
        nombre_de_verbes = min(nombre_de_verbes, len(verbes_irreguliers))
        interroger_utilisateur(verbes_irreguliers, nombre_de_verbes)
    else:
        print("Erreur : Impossible de charger la liste des verbes irréguliers.")