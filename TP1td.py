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


def find(date: str):
    tabDate = date.split("T")
    heureD = tabDate[1][:-3]
    annee = tabDate[0][:-4]
    mois = tabDate[0][4:-2]
    jour = tabDate[0][6:]
    date = "-".join([jour, mois, annee])
    return [date, heureD]
    
def heure(heure: str):
    table = [heure[:-2],heure[-2:]]
    return ":".join(table)




#if __name __ == "__main__" :
textics = lecture_fichier("evenementSAE_15.ics")
tabpropriete = ["UID:","DTSTART:","DTEND:","DESCRIPTION:","SUMMARY:","LOCATION:"] 
tab = []    
for propriete in tabpropriete :
    tab.append(select(textics, propriete))

dateDebut = find(tab[1])
dateFin = find(tab[2])
duree = str(int(dateFin[1])-int(dateDebut[1]))





