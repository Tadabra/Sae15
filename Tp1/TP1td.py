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
    date = "/".join([jour, mois, annee])#formatage date
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
    if tab[5]=='':
        salle = 'vide'
    else:
        salle=tab[5]#lien
    #les données facile trouver mais à formater
    dateDebut = separerDateHeure(tab[1])[0]#récupération de la date et formatage
    heureDébut = separerDateHeure(tab[1])[1]#récupération de l'heure et formatage
    heureFin = separerDateHeure(tab[2])[1]#récupération de l'heure de fin et formatage pour calculer la durée
    duree = str(int(heureFin)-int(heureDébut))#calcul de la durée
    
    #données à extraire de la description tab[3]
    description=tab[3]#on a "RT-TP B1, BOULEUX GUILLAUME"
    tabDescription = description.split(',')
    tabGroupe = []
    tabProf = []
    for cas in tabDescription:
        # print(cas)
        if cas.startswith('RT1-') or cas.startswith('RT2-'):
            if cas[:6]=='RT1-TP' or cas[:6]=='RT2-TP':
                typeActivité = 'TP'
                tabGroupe.append(cas[7:])
            elif cas[:6]=='RT1-TD' or cas[:6]=='RT2-TD':
                typeActivité = 'TD'
                tabGroupe.append(cas[7:])
            elif cas[:6]=='RT1-CM' or cas[:6]=='RT2-CM':
                typeActivité = 'CM'
                tabGroupe.append(cas[7:])
            else:
                typeActivité = 'vide'
        else:tabProf.append(cas)
    if len(tabProf)==0:
        prof ="vide"
    else :
        prof="|".join(tabProf)
    if len(tabGroupe)==0:
        groupe="vide"
    else: 
        groupe = "|".join(tabGroupe)
    # print(prof,groupe)
    pseudoCSV=";".join([uid,dateDebut,formatageHeure(heureDébut),formatageHeure(duree),typeActivité,summary,salle,prof,groupe])
    return pseudoCSV





