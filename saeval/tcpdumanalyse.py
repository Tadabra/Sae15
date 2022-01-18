# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:52:26 2022

@author: Fantin le seul
"""
import os
import csv

def lecture_fichier(chemin: str):
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        tab=[]
        with open(chemin) as f:
            for line in enumerate(f):
                linetext = line[1]
                if linetext.startswith('\t')!=True:
                    tab.append(linetext) 
            return tab
        # with open(chemin, encoding="utf8") as fh:
        #     return fh.readlines()
            #return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None

# def supHexa(tableauText):
#     tableauText = [i for i in tableauText if i.startswith("\t") != True ]
#     return tableauText

tableau = lecture_fichier("Fichier_a_traiter.txt")
#tableauSansHexa = supHexa(tableau)

def traitement(tableau):
    tablPseudoCSV = []
    for i in range(len(tableau)-1):
        var = tableau[i].split(",")
        decoupeVar0 = var[0].split(" ")#decoupe 11:42:04.766694
        heure = decoupeVar0[0]
        protocole = decoupeVar0[1]# "IP"
        adresseSource = decoupeVar0[2]# decoupe 'BP-Linux8.ssh',
        adresseDestination = decoupeVar0[4]# decoupe  '192.168.190.130.50019:',
        if decoupeVar0[5] == "Flags":
            flags = decoupeVar0[6][1:-1]# enleve les crochets de '[P.]'
        
            decoupeVar1 = var[1].split(" ")# decoupe ' seq 108:144', en "seq" et "108:144"
            seq = decoupeVar1[2]#recupere seulement "108:144"
            
            decoupeVar2 = var[2].split(" ")# decoupe ' ack 1', en "ack" et "1"
            ack = decoupeVar2[2]#recupere "1"
            
            decoupeVar3 = var[3].split(" ")#decoupe  ' win 312', en "win" et "312"
            win = decoupeVar3[2]#recupere "312"
            
            rechercheOption0 = tableau[1].split("[")
            rechercheOption1 = rechercheOption0[2].split("]")
            option = rechercheOption1[0]
            
            rechercheLongueur = rechercheOption1[1].split(" ")
            longueur = rechercheLongueur[2][:-1]
            pseudoCSV=";".join([heure,protocole,adresseSource,adresseDestination,flags,seq,ack,win,option,longueur,""])
            tablPseudoCSV.append(pseudoCSV)
        else:     
            #reste = decoupeVar0[6]
            pseudoCSVIfNoFlags = ";".join([heure,protocole,adresseSource,adresseDestination,"vide","vide","vide","vide","vide","vide"])
            tablPseudoCSV.append(pseudoCSVIfNoFlags)
    return tablPseudoCSV

table = traitement(tableau)


with open('tableur1.csv','w',newline='') as f:  #Ouverture du fichier CSV en écriture
    ecrire=csv.writer(f)                        # préparation à l'écriture
    for i in table:                           # Pour chaque ligne du tableau...  
        ecrire.writerow(i)                # Mettre dans la variable ecrire cette nouvelle ligne




