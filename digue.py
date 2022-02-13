#digue.py

import numpy as np
from numpy.polynomial import Polynomial
import math
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import os

##Initialisation
os.chdir("E:/Cours/Python")

##Polynomes
#Dilatation thermique (YJ [1 YJ = 11cm]):
dilTherm45 = Polynomial([0.0106288, 0.054236, 0.000706044])
#Fonte Glaciers (cm):
glac45max = Polynomial([-2.44382, 0.651685])

##Fonctions
#Année -> antcédant pour les polynomes
def anneeCoeff(y):
    if y>=2000:
        return int(0.25*y-499)
    else : return("Error")

#Calcul de la montéé pour une année donnée dans tous les scenario:
def calculMontee(annee):
    yGlace = anneeCoeff(annee + 4)
    yTherm = anneeCoeff(annee + 15)
    m45max = dilTherm45(yTherm) * 0.12 + 0.01 * glac45max(yGlace)
    return m45max

#Affichage d'un set de données
def affichage(Dataset):
    plt.figure(1,figsize=(10,8))
    plt.imshow(Dataset,cmap="terrain")
    plt.show()

def digue(seuil):
    #Chargement d'une carte plus détaillée
    Cote = np.loadtxt("data/RGEALTI_SPM_0545_5220_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
    Cote = Cote[700:900,300:650]
    Cote[0,0] = 250
    Cote[:,310:]=-99999.0
    Cote[160:,100:]=-99999.0
    Cote[143:160,290:310]=-99999.0
    Cote[155:160,280:290]=-99999.0

    #Création d'une côte supplémentaire (digue)
    X = np.copy(Cote)
    Digue = [[0,192],[0,193],[199,31],[150,198],[124,309],[125,309]]
    X[X<0] = -99999.0
    for x in range(1, 199):
        for y in range(20, 310):
            if X[x][y]<0 and (X[x+1][y]>0 or X[x][y+1]>0 or X[x-1][y]>0 or X[x][y-1]>0 or X[x+1][y+1]>0 or X[x+1][y-1]>0 or X[x-1][y+1]>0 or X[x-1][y-1]>0):
                X[x][y] = np.nan
                Digue.append([x,y])
    X[0,192], X[0,193], X[199,31], X[150,198], X[124,309], X[125,309]=np.nan, np.nan, np.nan, np.nan, np.nan, np.nan

    #Retirage des digues inutiles
    Carte = np.copy(X)
    E = calculMontee(2300)[3]
    print(compteDigue(X))
    for i in range(1,len(Digue)-8,10):
        Y = np.copy(Carte)
        Y[Digue[i][0]][Digue[i-1][1]] = Cote[Digue[i][0]][Digue[i][1]]
        Y[Digue[i+1][0]][Digue[i+1][1]] = Cote[Digue[i+1][0]][Digue[i+1][1]]
        Y[Digue[i+2][0]][Digue[i+2][1]] = Cote[Digue[i+2][0]][Digue[i+2][1]]
        Y[Digue[i+3][0]][Digue[i+3][1]] = Cote[Digue[i+3][0]][Digue[i+3][1]]
        Y[Digue[i+4][0]][Digue[i+4][1]] = Cote[Digue[i+4][0]][Digue[i+4][1]]
        Y[Digue[i+5][0]][Digue[i+5][1]] = Cote[Digue[i+5][0]][Digue[i+5][1]]
        Y[Digue[i+6][0]][Digue[i+6][1]] = Cote[Digue[i+6][0]][Digue[i+6][1]]
        Y[Digue[i+7][0]][Digue[i+7][1]] = Cote[Digue[i+7][0]][Digue[i+7][1]]
        Y[Digue[i+8][0]][Digue[i+8][1]] = Cote[Digue[i+8][0]][Digue[i+8][1]]
        Y[Digue[i+9][0]][Digue[i+9][1]] = Cote[Digue[i+9][0]][Digue[i+9][1]]
        utile = seuil
        for j in range(150):
            for x in range(1,len(Y)-1):
                for y in range(1,len(Y[0])-1):
                    if Y[x][y]!=-99999.0 and Y[x][y]<=E and (Y[x+1][y]<0 or Y[x][y+1]<0 or Y[x-1][y]<0 or Y[x][y-1]<0 or Y[x+1][y+1]<0 or Y[x+1][y-1]<0 or Y[x-1][y+1]<0 or Y[x-1][y-1]<0):
                        Y[x][y] = -99999.0
                        utile -= 1
        print(utile)
        if utile>0:
            X[Digue[i][0]][Digue[i-1][1]] = Cote[Digue[i][0]][Digue[i][1]]
            X[Digue[i+1][0]][Digue[i+1][1]] = Cote[Digue[i+1][0]][Digue[i+1][1]]
            X[Digue[i+2][0]][Digue[i+2][1]] = Cote[Digue[i+2][0]][Digue[i+2][1]]
            X[Digue[i+3][0]][Digue[i+3][1]] = Cote[Digue[i+3][0]][Digue[i+3][1]]
            X[Digue[i+4][0]][Digue[i+4][1]] = Cote[Digue[i+4][0]][Digue[i+4][1]]
            X[Digue[i+5][0]][Digue[i+5][1]] = Cote[Digue[i+5][0]][Digue[i+5][1]]
            X[Digue[i+6][0]][Digue[i+6][1]] = Cote[Digue[i+6][0]][Digue[i+6][1]]
            X[Digue[i+7][0]][Digue[i+7][1]] = Cote[Digue[i+7][0]][Digue[i+7][1]]
            X[Digue[i+8][0]][Digue[i+8][1]] = Cote[Digue[i+8][0]][Digue[i+8][1]]
            X[Digue[i+9][0]][Digue[i+9][1]] = Cote[Digue[i+9][0]][Digue[i+9][1]]
    print(compteDigue(X))
    return X

def applicationDigue(Carte):    #Application du scénario avec la digue
    Y = np.copy(X)
    E = calculMontee(2300)[3]
    for j in range(200):
        for x in range(1,len(Y)-1):
            for y in range(1,len(Y[0])-1):
                if Y[x][y]!=-99999.0 and Y[x][y]<=E and (Y[x+1][y]<0 or Y[x][y+1]<0 or Y[x-1][y]<0 or Y[x][y-1]<0) and (not(math.isnan(Y[x+1][y])) or not(math.isnan(Y[x][y+1])) or not(math.isnan(Y[x-1][y])) or not(math.isnan(Y[x][y-1]))):
                    Y[x][y] = -99999.0
    return Y

#Compte les cases servant de digue
def compteDigue(Dataset):
    x = 0
    for i in range(len(Dataset)):
        for j in range(len(Dataset[0])):
            if math.isnan(Dataset[i][j]):
                x+=1
    return(x)

X = digue(7816)
Y = applicationDigue(X)
affichage(X)