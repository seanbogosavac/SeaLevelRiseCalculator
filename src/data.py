# data.py
# This file includes all the data used in the program, from the polynomials to the array containing the altimeter maps.

import numpy as np
from numpy.polynomial import Polynomial
import math


## Extracting data:
# Moderately precise (25m/pixel) dataset used to compute sea level rise
dataset1 = np.loadtxt("data/BDALTIV2_25M_SPM_0525_5200_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
dataset2 = np.loadtxt("data/BDALTIV2_25M_SPM_0525_5225_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
dataset3 = np.loadtxt("data/BDALTIV2_25M_SPM_0550_5200_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
dataset4 = np.loadtxt("data/BDALTIV2_25M_SPM_0550_5225_MNT_RGSPM06U21_STPM50.asc",skiprows=6)
Dataset = np.concatenate((np.concatenate((dataset2, dataset4), 1),np.concatenate((dataset1, dataset3), 1)), 0)
# More precise (5m/pixel) dataset used to compute the dikes
dikeDataset = np.loadtxt("data/RGEALTI_SPM_0545_5220_MNT_RGSPM06U21_STPM50.asc",skiprows=6)


## Building useable datasets:
# Complete archipelago
Islands = Dataset[:,700:]
# Miquelon island
Miquelon = Dataset[200:450, 750:1000]
Miquelon[0][0] = 300
# St-Pierre island
StPierre = Dataset[1500:2000, 1250:1750]
StPierre[0][0] = 300
# Miquelon's southern coast (best choice for the dikes due to its low altitude)
Coast = dikeDataset[700:900,300:650]
Coast[0,0] = 250
Coast[:,310:]=-99999.0
Coast[160:,100:]=-99999.0
Coast[143:160,290:310]=-99999.0
Coast[155:160,280:290]=-99999.0


## Polynomials
# Thermal expansion:
thermExp26 = lambda x: 0.760659*math.log(0.214891*x)
thermExp45 = Polynomial([0.0106288, 0.054236, 0.000706044])
thermExp60 = Polynomial([-0.000592308, 0.0373631, 0.00141606])
thermExp85 = Polynomial([-0.00310769, 0.0308501, 0.00290476])
# Glaciers melting:
glac26max = Polynomial([-2.52809, 0.674157])
glac26min = Polynomial([-0.84270, 0.224719])
glac45max = Polynomial([-2.44382, 0.651685])
glac45min = Polynomial([-0.77500, 0.206742])
glac60max = Polynomial([-2.86517, 0.764045])
glac60min = Polynomial([-1.09551, 0.292135])
glac85max = Polynomial([-3.60674, 0.961798])
glac85min = Polynomial([-1.11236, 0.296629])