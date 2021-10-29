# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 17:53:32 2021

@author: doria
"""
import numpy as np

def main():
    valueMatrixRange = getValueFromTxt()[0]
    matrice = initMatrix(valueMatrixRange)
    
    emplacement = getValueFromTxt()[1]
    initAspirateur(emplacement, matrice)
    
    #afficheMatrix(matrice)
    
    ordre = getValueFromTxt()[2]
    executeOrdre(ordre, matrice, emplacement, 0)
    print('\n Résultat final : ',emplacement[0], emplacement[1], emplacement[2])
    
#récupère les valeur du fichier texte
def getValueFromTxt():
    with open("texte.txt") as myfile:
        a = []
        for index, line in enumerate(myfile):
            a.append(line.strip().split(' '))
        return a

#initialise la matrice dynamiquement
def initMatrix(matrixRange):
    return np.zeros((int(matrixRange[0]),int(matrixRange[1])))

#affiche la matrice
def afficheMatrix(x):
    for b in range(0, len(x)):
        print(x[b])

#place l'aspirateur dynamiquement
def initAspirateur(emplacement, matrice):
    matrice[int(emplacement[0])][int(emplacement[1])] = 1
    print("\n direction initiale de l'aspirateur : ",emplacement[2],"\n")


#recursive qui boucle sur le nombre d'ordre
def executeOrdre(ordre, matrice, emplacement, nbOrdre):
    splitlist = list(str(ordre[0])[nbOrdre])
    col = int(emplacement[0])
    row = int(emplacement[1])
    direction = emplacement[2]
    
    print(' _____________________________')
    print('\n col:',col,' row:',row, ' direction:', direction)
    if(splitlist[0] == 'D'):
        direction = tourneDroite(emplacement)
    if(splitlist[0] == 'G'):
        direction = tourneGauche(emplacement)
    
    if(splitlist[0] == 'A'):
        matrice[col][row] = 0
        avancer(emplacement, len(matrice))
        col = emplacement[0]
        row = emplacement[1]
        matrice[col][row] = 1
        
    print()
    afficheMatrix(matrice)

    if(nbOrdre < len(list(str(ordre[0])))-1):
        executeOrdre(ordre, matrice, emplacement, nbOrdre+1)
        

#Oriente la direction à droite
def tourneDroite(emplacement):
    direction = emplacement[2]
    if(direction == 'N'):
        direction = 'E'
    elif(direction == 'E'):
        direction = 'S'
    elif(direction == 'S'):
        direction = 'W'
    else:
        direction = 'N'
    emplacement[2] = direction
    return direction

#Oriente la direction à gauche
def tourneGauche(emplacement):
    direction = emplacement[2]
    if(direction == 'N'):
        direction = 'W'
    elif(direction == 'W'):
        direction = 'S'
    elif(direction == 'S'):
        direction = 'E'
    else:
        direction = 'N'
    emplacement[2] = direction
    return direction

#Fait avancer l'aspirateur en fonction de ça direction. S'il avance dans le vide aucune action n'est effectuer.
def avancer(emplacement, lenMatrice):
    col = int(emplacement[0])
    row = int(emplacement[1])
    direction = emplacement[2]
    if(direction == 'N' and row != lenMatrice):
        row = row+1
    elif(direction == 'S' and row != 0):
        row = row-1
    elif(direction == 'E' and col != lenMatrice):
        col = col+1
    elif(col != 0):
        col = col-1
    emplacement[0] = col
    emplacement[1] = row


main()
