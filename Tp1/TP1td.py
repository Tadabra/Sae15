import re
import os
def lecture_fichier(chemin: str):
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        with open(chemin, encoding="utf8") as fh:
            #return fh.readlines()
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None


def select(textics: str, chaineSelect) :
    """
    Parameters
    ----------
    textics : C'est le string fournis par lecture_fichier.
    chaineSelect : C'est le string correspondant à la propriété du fichier ics.

    Returns
    -------
    return la propriété choisi.

    """
    texticsTab = textics.split("\n")
    for propriete in texticsTab :
        if chaineSelect in propriete:
            text = re.sub(chaineSelect,"",propriete)
            return text


def separerDateHeure(date: str):
    tabDateHeure = date.split("T")#séparation date et heure
    heure = tabDateHeure[1][:-3]#on tranche les données récupération heure
    annee = tabDateHeure[0][:-4]#récupération année
    mois = tabDateHeure[0][4:-2]#récupération mois
    jour = tabDateHeure[0][6:]#récupération jour
    date = "-".join([jour, mois, annee])#formatage date
    return [date, heure]
    
def formatageHeure(heure: str):
    table = [heure[:-2],heure[-2:]]
    return ":".join(table)


#textics = lecture_fichier("evenementSAE_15.ics")
def tpcsv(chaine_evenement: str):
    tabpropriete = ["UID:","DTSTART:","DTEND:","DESCRIPTION:","SUMMARY:","LOCATION:"]#tableau des données à récupérer 
    tab = []    
    for propriete in tabpropriete :# récupération des données
        tab.append(select(chaine_evenement, propriete))
    #les données facile à récupérer
    uid=tab[0]#uid
    summary=tab[4]#nom evenement
    salle=tab[5]#lien
    #les données facile trouver mais à formater
    dateDebut = separerDateHeure(tab[1])[0]#récupération de la date et formatage
    heureDébut = separerDateHeure(tab[1])[1]#récupération de l'heure et formatage
    heureFin = separerDateHeure(tab[2])[1]#récupération de l'heure de fin et formatage pour calculer la durée
    duree = str(int(heureFin)-int(heureDébut))#calcul de la durée
    
    #données à extraire de la description tab[3]
    description=tab[3]#on a "RT-TP B1, BOULEUX GUILLAUME"
    tabDescription = description.split(',')
    print
    tabGroupe = []
    tabProf = []
    for cas in tabDescription:
        print(cas)
        if cas.startswith('RT1-'):
            if cas[:6]=='RT1-TP':
                typeActivité = 'TP'
                tabGroupe.append(cas[6:])
            elif cas[:6]=='RT1-TD':
                typeActivité = 'TD'
                tabGroupe.append(cas[6:])
            elif cas[:6]=='RT1-CM':
                typeActivité = 'CM'
                tabGroupe.append(cas[6:])
            else:
                typeActivité = 'vide'
                tabProf.append(cas)
    # descriptionTab=re.split("-|,",description)# ici on coupe à - et , pour avoir "RT" "TP B1", "BOULEUX GUILLAUME"
    # if len(descriptionTab) == 3:
    #     tabActiviteGroupe = ""
    # else:
    #     tabActiviteGroupe=descriptionTab[1].split(" ")#ça correspond à  "TP" "B1"
    #récupération des propriétés à afficher dans pseudo csv

    # if len(descriptionTab) > 2:
    #      prof=descriptionTab[2]
    # else:
    #      prof=""
    prof= str(tabProf)
    groupe = str(tabGroupe)
    # if len(tabActiviteGroupe) == "":
    #     groupe = ""
    # else:
    #     groupe = tabActiviteGroupe[1]
    pseudoCSV=";".join([uid,dateDebut,formatageHeure(heureDébut),formatageHeure(duree),typeActivité,summary,salle,prof,groupe])
    return pseudoCSV





