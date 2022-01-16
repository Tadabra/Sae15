# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:07:41 2022

@author: noelp
"""

import re
import os
from TP1td import *

textics = lecture_fichier("ADE_RT1_Septembre2021_Decembre2021.ics")
evenementTab=re.split("\nBEGIN:VEVENT\n|\nEND:VEVENT\nBEGIN:VEVENT\n|\nEND:VEVENT",textics)
#print(len(descriptionTab))
#descriptionTab = [i for i in descriptionTab if i != '']
del evenementTab[0]
del evenementTab[len(evenementTab)-1]
#descriptionTab[len(descriptionTab)-1]
tabDesEvenements = []
for i in range (len(evenementTab)-1):
    tabDesEvenements.append(tpcsv(evenementTab[i]))