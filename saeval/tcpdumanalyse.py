# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:52:26 2022

@author: Fantin le seul
"""
import os

def lecture_fichier(chemin: str):
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.readlines()
            #return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None

def supHexa(tableauText):
    tableauText = [i for i in tableauText if i.startswith("\t") != True ]
    return tableauText

tableau = lecture_fichier("Fichier_a_traiter.txt")
tableauSansHexa = supHexa(tableau)

var = tableauSansHexa[1].split(",")