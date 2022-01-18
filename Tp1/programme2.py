# -*- coding: utf-8 -*-

import re
import os
from TP1td import *

def creationTableauEvenements(fichierics:str):
    textics = lecture_fichier(fichierics)
    evenementTab=re.split("\nBEGIN:VEVENT\n|\nEND:VEVENT\nBEGIN:VEVENT\n|\nEND:VEVENT",textics)
    del evenementTab[0]#suppression begin:vcalendar
    #del evenementTab[len(evenementTab)-1]#suppression begin:vcalendar
    tabDesEvenements = []#creation tableau des evenements
    for i in range (len(evenementTab)-1):
        tabDesEvenements.append(tpcsv(evenementTab[i]))
    return tabDesEvenements

tab = creationTableauEvenements("ADE_RT1_Septembre2021_Decembre2021.ics")