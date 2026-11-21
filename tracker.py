import json
from pathlib import Path
from datetime import date, datetime

def showOption():
    print("1. Ajouter une dépense")
    print("2. Voir toutes les dépenses")
    print("3. Voir les dépenses par categorie")
    print("4. Voir les dépenses d'un mois")
    print("5. Voir le total")
    print("6. Supprimer une dépense")
    print("7. Supprimer toutes les dépenses")
    print("8. Quitter")
    print("")

    while True:
        choice = input("Entrée un chiffre (1-8): ")
        print("")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 8:
                return choice
            print("La valeur doit etre comprise entre 1 et 8")
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
    dateTime = date.today().strftime("%d/%m/%Y")
    print("Vous avez ajoutez:\n")
    print(f"Nom: {name}")
    print(f"Montant: {price}")
    print(f"Categorie: {categorie}")
    print(f"Date: {dateTime}")
    print("")
    allDepense.append({"name": name, "montant": price, "categorie": categorie, "date": dateTime})

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
        print(f"Date: {dic['date']}")
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

def showExpenseByName(allDepense, name):
    allDepenseByName = []
    i = 1
    for dic in allDepense:
        if dic['name'] == name:
            allDepenseByName.append(dic)
            print(f"{i}. {dic['name']} - {dic['categorie']} - {dic['montant']} - {dic['date']}")
            i += 1
    print("")
    while True:
        n = input("Entrée le numéro de la dépense à supprimé: ")
        print("")
        try:
            n = int(n)
            if n >= 1 and n < i:
                return allDepenseByName[n-1]
            print(f"La valeur doit etre comprise entre 1 et {i}")
            print("")
        except ValueError:
            print("La valeur doit etre un entier")
            print("")

def supExpense(allDepense):
    if len(allDepense) == 0:
        print("Il n'y a aucune dépense a supprimé")
        print("")
        return
    dep = input("Entrée le nom de la dépense a supprimé: ")
    print("")
    cnt = countName(allDepense, dep)
    if cnt > 1:
        print("Il y a plusieurs depense à ce nom veuillez choisir laquel supprimé")
        print("")
        depense = showExpenseByName(allDepense, dep)
        allDepense.remove(depense)
        print(f"{depense['name']} - {depense['categorie']} - {depense['montant']} - {depense['date']} à été supprimé")
        print("")
    elif cnt == 1:
        for dic in allDepense:
            if dic["name"] == dep:
                price = dic["montant"]
                allDepense.remove(dic)
                print(f"Vous avez supprimé {dep} d'un montant de {price} à la date du {dic['date']}")
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
            print(f"Date: {dic['date']}")
            print("")
            flag = True
    if flag:
        return
    else:
        print(f"Il n'y a aucune dépense pour {cat}")
        print("")
        return

def showExpenseByMonth(allDepense):
    month = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    while True:
        mois = input("Choisissez le mois que vous voulez affiché (1-12): ")
        print("")
        try:
            mois = int(mois)
            if mois >= 1 and mois <= 12:
                print(f"Vous avez choisit le mois de {month[mois-1]}")
                print("")
                flag = False
                for dic in allDepense:
                    if int(dic["date"].split("/")[1]) == mois:
                        print(f"Nom: {dic['name']}")
                        print(f"Montant: {dic['montant']}")
                        print(f"Categorie: {dic['categorie']}")
                        print(f"Date: {dic['date']}")
                        print("")
                        flag = True
                if flag:
                    return
                print(f"Il n'y a aucune dépense pour le mois de {month[mois-1]}")
                print("")
                return
            else:
                print("Le mois doit etre compris entre 1 et 12")
                print("")
        except ValueError:
            print("La valeur doit etre un entier")
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
        showExpenseByCategorie(allDepenseListe)
    elif value == 4:
        showExpenseByMonth(allDepenseListe)
    elif value == 5:
        showTotal(allDepenseListe)
    elif value == 6:
        supExpense(allDepenseListe)
        saveData(allDepenseListe)
    elif value == 7:
        supAllDepense(allDepenseListe)
        saveData(allDepenseListe)
    else:
        break