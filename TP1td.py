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




#if __name __ == "__main__" :
textics = lecture_fichier("evenementSAE_15.ics")
tabpropriete = ["UID:","DTSTART:","DTEND:","DESCRIPTION:","SUMMARY:","LOCATION:"] 
tab = []    
for propriete in tabpropriete :
    tab.append(select(textics, propriete))

description=tab[3]
descriptionTab=re.split("-| |,",description)    
#récupération des propriétés à afficher dans pseudo csv
uid=tab[0]
dateDebut = separerDateHeure(tab[1])[0]
heureDébut = separerDateHeure(tab[1])[1]
heureFin = separerDateHeure(tab[2])[1]
duree = str(int(heureFin)-int(heureDébut))
typeActivité = descriptionTab[1]
summary=tab[4]
salle=tab[5]
prof=descriptionTab[3]+" "+descriptionTab[4]
groupe=descriptionTab[2]

pseudoCSV=";".join([uid,dateDebut,formatageHeure(heureDébut),formatageHeure(duree),typeActivité,summary,salle,prof,groupe])





