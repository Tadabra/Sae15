import os
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:23:15 2022

@author: Fantin le seul
"""

def lecture_fichier(chemin: str) :#-> typing.Optional[str]
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None