# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:07:41 2022

@author: noelp
"""

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


textics = lecture_fichier("ADE_RT1_Septembre2021_Decembre2021.ics")
descriptionTab=re.split("\nBEGIN:VEVENT\n|\nEND:VEVENT",textics)
print(len(descriptionTab))
descriptionTab = [i for i in descriptionTab if i != '']
del descriptionTab[0]
descriptionTab[len(descriptionTab)-1]


print(len(descriptionTab))