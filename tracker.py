import json
from pathlib import Path

def showOption():
    print("1. Ajouter une dépense")
    print("2. Voir toutes les dépenses")
    print("3. Voir les dépenses par categorie")
    print("4. Voir le total")
    print("5. Supprimer une dépense")
    print("6. Supprimer toutes les dépenses")
    print("7. Quitter")
    print("")

    while True:
        choice = input("Entrée un chiffre (1-7): ")
        print("")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 7:
                return choice
            print("La valeur doit etre comprise entre 1 et 7")
            print("")
        except ValueError:
            print("La valeur entrée doit etre un entier")
            print("")

def showCategorie():
    print("Choisissez une catégorie: ")
    print("")
    print("1. Alimentation")
    print("2. Transport")
    print("3. Logement")
    print("4. Loisirs")
    print("5. Abonnements")
    print("6. Autres")
    print("")
    categorie = ["Alimentation", "Transport", "Logement", "Loisirs", "Abonnements", "Autres"]
    while True:
        cat = input("Entrée le numéro de la catégorie: ")
        print("")
        try:
            cat = int(cat)
            if cat >= 1 and cat <= 6:
                return categorie[cat - 1]
            else:
                print("Il faut que le nombre soit compris entre 1 et 6")
                print("")
        except ValueError:
            print("La valeur doit etre un nombre")
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
    categorie = showCategorie()
    print("Vous avez ajoutez:\n")
    print(f"Nom: {name}")
    print(f"Montant: {price}")
    print(f"Categorie: {categorie}")
    print("")
    for dic in allDepense:
        if dic["name"] == name and dic["categorie"] == categorie:
            print(f"Il y avait deja {dic['montant']} pour {dic['name']} dans la categorie {categorie}")
            dic["montant"] += price
            print(f"Montant total pour {dic['name']} dans {categorie}: {dic['montant']}")
            print("")
            return
    allDepense.append({"name": name, "montant": price, "categorie": categorie})

def showExpense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense courante")
        print("")
        return
    print("Voici toutes vos dépenses:\n")
    for dic in allDepense:
        print(f"Nom: {dic['name']}")
        print(f"Montant: {dic['montant']}")
        print(f"Categorie: {dic['categorie']}")
        print("")

def showTotal(allDepense):
    total = 0.0
    for dic in allDepense:
        total += dic["montant"]
    print(f"Total: {total}")
    print("") 

def countName(allDepense, name):
    cnt = 0
    for dic in allDepense:
        if dic["name"] == name:
            cnt += 1
    return cnt

def supExpense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense a supprimé")
        print("")
        return
    dep = input("Entrée le nom de la dépense a supprimé: ")
    print("")
    cnt = countName(allDepense, dep)
    if cnt > 1:
        print("Il y a plusieurs depense à ce nom veuillez choisir une categorie")
        print("")
        cat = showCategorie()
        for dic in allDepense:
            if dic["name"] == dep and dic["categorie"] == cat:
                price = dic["montant"]
                allDepense.remove(dic)
                print(f"Vous avez supprimé {dep} d'un montant de {price} dans {cat}")
                print("")
                return
        print(f"La catégorie {cat} n'existe pas pour {dep}. Rien n'a été supprimé")
        print("")
    elif cnt == 1:
        for dic in allDepense:
            if dic["name"] == dep:
                price = dic["montant"]
                allDepense.remove(dic)
                print(f"Vous avez supprimé {dep} d'un montant de {price}")
                print("")
                return
    else:
        print("Il n'y a pas de dépense associé a ce nom")
        print("")
        return

def supAllDepense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense a supprimer")
        print("")
        return
    allDepense.clear()
    print("Vous avez supprimé toute vos dépense")
    print("")

def showExpenseByCategorie(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense")
        print("")
        return
    print("Quel categorie de depense voulez vous voir ?")
    print("")
    cat = showCategorie()
    flag = False
    for dic in allDepense:
        if dic["categorie"] == cat:
            print(f"Nom: {dic['name']}")
            print(f"Montant: {dic['montant']}")
            print(f"Categorie: {dic['categorie']}")
            print("")
            flag = True
    if flag:
        return
    else:
        print(f"Il n'y a aucune dépense pour {cat}")
        print("")
        return

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
        showExpenseByCategorie(allDepenseListe)
    elif value == 4:
        showTotal(allDepenseListe)
    elif value == 5:
        supExpense(allDepenseListe)
        saveData(allDepenseListe)
        
    elif value == 6:
        supAllDepense(allDepenseListe)
        saveData(allDepenseListe)
    else:
        break