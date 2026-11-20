import json
from pathlib import Path

def showOption():
    print("1. Ajouter une dépense")
    print("2. Voir toutes les dépenses")
    print("3. Voir le total")
    print("4. Supprimer une dépense")
    print("5. Supprimer toutes les dépenses")
    print("6. Quitter")
    print("")

    while True:
        choice = input("Entrée un chiffre (1-6): ")
        print("")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 6:
                return choice
            print("La valeur doit etre comprise entre 1 et 6")
            print("")
        except ValueError:
            print("La valeur entrée doit etre un entier")
            print("")

def addExpense(allDepense):
    name = input("Nom: ")
    print("")
    while True:
        price = input("Montant: ")
        print("")
        try:
            price = float(price)
            if price >= 0:
                break
            print("Veuillez entrée un montant positif")
            print("")
        except ValueError:
            print("La valeur doit etre un nombre ou un float")
            print("")
    print("Vous avez ajoutez:\n")
    print(f"Nom: {name}")
    print(f"Montant: {price}")
    print("")
    for dic in allDepense:
        if dic["name"] == name:
            print(f"Il y avait deja {dic['montant']} pour {dic['name']}")
            dic["montant"] += price
            print(f"Montant total pour {dic['name']}: {dic['montant']}")
            print("")
            return
    allDepense.append({"name": name, "montant": price})

def showExpense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense courante")
        print("")
        return
    print("Voici toutes vos dépenses:\n")
    for dic in allDepense:
        print(f"Nom: {dic['name']}")
        print(f"Montant: {dic['montant']}")
        print("")

def showTotal(allDepense):
    total = 0.0
    for dic in allDepense:
        total += dic["montant"]
    print(f"Total: {total}")
    print("") 

def supExpense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense a supprimé")
        print("")
        return
    dep = input("Entrée le nom de la dépense a supprimé: ")
    print("")
    for dic in allDepense:
        if dic["name"] == dep:
            price = dic["montant"]
            allDepense.remove(dic)
            print(f"Vous avez supprimé {dep} d'un montant de {price}")
            print("")
            return
    print("Il n'y a pas de dépense associé a ce nom")
    print("")

def supAllDepense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y avait aucune dépense a supprimer")
        print("")
        return
    allDepense.clear()
    print("Vous avez supprimé toute vos dépense")
    print("")

def saveData(allDepense):
    with open("données.json", "w", encoding="utf-8") as fichier:
        json.dump(allDepense, fichier, indent=4, ensure_ascii=False)

def recupData():
    file = Path("données.json")
    if not file.exists():
        return []
    try:
        with open("données.json", "r", encoding="utf-8") as fichier:
            data = json.load(fichier)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []
    
allDepenseListe = recupData()

while True:
    value = showOption()
    if value == 1:
        addExpense(allDepenseListe)
        saveData(allDepenseListe)
    elif value == 2:
        showExpense(allDepenseListe)
    elif value == 3:
        showTotal(allDepenseListe)
    elif value == 4:
        supExpense(allDepenseListe)
        saveData(allDepenseListe)
    elif value == 5:
        supAllDepense(allDepenseListe)
        saveData(allDepenseListe)
    else:
        break