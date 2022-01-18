from programme2 import *

tab = creationTableauEvenements("ADE_RT1_Septembre2021_Decembre2021.ics")
tabdetab=[]
for element in tab:
    tabdetab.append(element.split(';'))

def recherche(tabdetab,valeur):
    dicPara={'uid':0,'dateDebut':1,'heureDebut':2,'duree':3,'typeActivité':4,'activité':5,'salle':6,'prof':7,'groupe':8}
    champ = int(input("Entrez le champ de recherche : \nuid:0\ndateDebut:1\nheureDebut:2\nduree:3\ntypeActivité:4\nactivité:5\nsalle:6\nprof:7\ngroupe:8 :\n\nvotre champ ? :"))
    champAssociés = input("taper les numéros des champs desirés sans espaces : ")
    tabChampAssociés = [int(car) for car in champAssociés]
    # print(tabChampAssociés)
    tabresources=[]
    for i in range(len(tabdetab)):
        # print(tab[i][5])
        if tabdetab[i][champ]==valeur:
            tabseance=[]
            tabseance = [tabdetab[i][x] for x in tabChampAssociés]
            # tabseance.extend([tabdetab[i][1],tabdetab[i][3],tabdetab[i][4]])
            # print(tabseance)
            tabresources.append(tabseance)
    return tabresources

tabr0=recherche(tabdetab,'R107')#recherche R107 (Informatique),associées à votre groupe B1
# la date de la séance, la durée, le type de la séance
resultat0=[element for element in tabr0 if element[4]=='B1']
#  nombre TP du groupe B1 en septembre, en octobre, en novembre et en décembre

tabr=recherche(tabdetab,'B1')
resultat1=[element for element in tabr if '09' in element[0][3:-5]]
resultat2=[element for element in tabr if '10' in element[0][3:-5]]
resultat3=[element for element in tabr if '11' in element[0][3:-5]]
resultat4=[element for element in tabr if '12' in element[0][3:-5]]

t1=len(resultat1)
t2=len(resultat2)
t3=len(resultat3)
t4=len(resultat4)

import matplotlib.pyplot as plt
import numpy as np

# diagramme baton

fig = plt.figure()

x = ['septembre','octobre','novembre','decembre']
height = [t1,t2,t3,t4]
width = 1.0

plt.bar(x, height, width, color='b' )

plt.savefig('SimpleBar.png')
plt.show()



labels = 'septembre','octobre','novembre','decembre'
sizes = [t1,t2,t3,t4]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.savefig('PieChart01.png')
plt.show()