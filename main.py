#main.py

import numpy as np
from numpy.polynomial import Polynomial
import math
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import os

##Initialisation
os.chdir("C:/Users/bogos/quiCk aCCess/Cours/Python")

#Extraction des données
dataset1 = np.loadtxt("data/BDALTIV2_25M_SPM_0525_5200_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
dataset2 = np.loadtxt("data/BDALTIV2_25M_SPM_0525_5225_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
dataset3 = np.loadtxt("data/BDALTIV2_25M_SPM_0550_5200_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
dataset4 = np.loadtxt("data/BDALTIV2_25M_SPM_0550_5225_MNT_RGSPM06U21_STPM50.asc",skiprows=6)

#Création de l'array complet
Dataset = np.concatenate((np.concatenate((dataset2, dataset4), 1),np.concatenate((dataset1, dataset3), 1)), 0)
CroppedData = Dataset[:,700:]
Miqu = Dataset[200:450, 750:1000]
Miqu[0][0] = 250
StPr = Dataset[1500:2000, 1250:1750]
StPr[0][0] = 250

##Polynomes (x=1=>annee=2000 ; x+1=>annee+4):
#Dilatation thermique (YJ [1 YJ = 11cm]):
dilTherm26 = lambda x : 0.760659*math.log(0.214891*x)
dilTherm45 = Polynomial([0.0106288, 0.054236, 0.000706044])
dilTherm60 = Polynomial([-0.000592308, 0.0373631, 0.00141606])
dilTherm85 = Polynomial([-0.00310769, 0.0308501, 0.00290476])
#Fonte Glaciers (cm):
glac26max = Polynomial([-2.52809, 0.674157])
glac26min = Polynomial([-0.84270, 0.224719])
glac45max = Polynomial([-2.44382, 0.651685])
glac45min = Polynomial([-0.77500, 0.206742])
glac60max = Polynomial([-2.86517, 0.764045])
glac60min = Polynomial([-1.09551, 0.292135])
glac85max = Polynomial([-3.60674, 0.961798])
glac85min = Polynomial([-1.11236, 0.296629])

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
    m26min = dilTherm26(yTherm) * 0.10 + 0.01 * glac26min(yGlace)
    m26max = dilTherm26(yTherm) * 0.12 + 0.01 * glac26max(yGlace)
    m45min = dilTherm45(yTherm) * 0.10 + 0.01 * glac45min(yGlace)
    m45max = dilTherm45(yTherm) * 0.12 + 0.01 * glac45max(yGlace)
    m60min = dilTherm60(yTherm) * 0.10 + 0.01 * glac60min(yGlace)
    m60max = dilTherm60(yTherm) * 0.12 + 0.01 * glac60max(yGlace)
    m85min = dilTherm85(yTherm) * 0.10 + 0.01 * glac85min(yGlace)
    m85max = dilTherm85(yTherm) * 0.12 + 0.01 * glac85max(yGlace)
    X = [m26min, m26max, m45min, m45max, m60min, m60max, m85min, m85max]
    return X

#Application des divers scenario a une annee donnée
def applicationScenario(annee, Dataset):
    E = calculMontee(annee)
    S = [Dataset]
    for i in range(len(E)):
        X = np.copy(Dataset)
        for j in range(200):
            for x in range(1,len(X)-1):
                for y in range(1,len(X[0])-1):
                    if X[x][y]!=-99999.0 and X[x][y]<=E[i] and (X[x+1][y]<0 or X[x][y+1]<0 or X[x-1][y]<0 or X[x][y-1]<0 or X[x+1][y+1]<0 or X[x+1][y-1]<0 or X[x-1][y+1]<0 or X[x-1][y-1]<0):
                        X[x][y] = -99999.0
        S.append(X)
        print("Done")
    return S

#Affichage d'un set de données
def affichage(interet=False, Dataset=CroppedData, colorbar=True):
    X = np.copy(Dataset)
    if interet:
        X[X<=0.0] = -15
        X[X>=50] = 30
    else:
        X[X<=0.0] = -200
    plt.figure(1,figsize=(10,8))
    plt.imshow(X,cmap="terrain")
    plt.axis('off')
    if colorbar: plt.colorbar()
    plt.show()

#Affichage de tous les scénarios à une année donnée
def affichageScenarios(annee, Dataset=CroppedData, interet=False):
    Data = applicationScenario(annee, Dataset)
    for I in Data:
        if interet:
            I[I<=0.0] = -15
            I[I>=50] = 50
        else:
            I[I<=0.0] = -200
    plt.figure(1,figsize=(10,8))
    plt.subplot(2,5,1)
    plt.imshow(Data[1], cmap="terrain")
    plt.axis('off')
    plt.title('RCP2.6 (Optimiste)')
    plt.subplot(2,5,6)
    plt.imshow(Data[2], cmap="terrain")
    plt.axis('off')
    plt.title('RCP2.6 (Pessimiste)')
    plt.subplot(2,5,2)
    plt.imshow(Data[3], cmap="terrain")
    plt.axis('off')
    plt.title('RCP4.5 (Optimiste)')
    plt.subplot(2,5,7)
    plt.imshow(Data[4], cmap="terrain")
    plt.axis('off')
    plt.title('RCP4.5 (Pessimiste)')
    plt.subplot(2,5,3)
    plt.imshow(Data[5], cmap="terrain")
    plt.axis('off')
    plt.title('RCP6.0 (Optimiste)')
    plt.subplot(2,5,8)
    plt.imshow(Data[6], cmap="terrain")
    plt.axis('off')
    plt.title('RCP6.0 (Pessimiste)')
    plt.subplot(2,5,4)
    plt.imshow(Data[7], cmap="terrain")
    plt.axis('off')
    plt.title('RCP8.5 (Optimiste)')
    plt.subplot(2,5,9)
    plt.imshow(Data[8], cmap="terrain")
    plt.axis('off')
    plt.title('RCP8.5 (Pessimiste)')
    plt.subplot(2,5,5)
    plt.imshow(Data[0], cmap="terrain")
    plt.axis('off')
    plt.title('Vue acutelle')
    plt.show()