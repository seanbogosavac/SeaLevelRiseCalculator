# display.py
# This file contains all functions related to the output of the program.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr


# Displays a single dataset
def display(dataset, focus, colorbar):
    print("Displaying results")
    X = np.copy(dataset)
    if focus:
        X[X<=0.0] = -15
        X[X>=50] = 50
    else:
        X[X<=0.0] = -200
    plt.figure(1,figsize=(10,8))
    plt.imshow(X,cmap="terrain")
    plt.axis("off")
    if colorbar: plt.colorbar()
    plt.show()


#Affichage de tous les scénarios à une année donnée
def displayAll(datasets, focus):
    print("Displaying results")
    for I in datasets:
        if focus:
            I[I<=0.0] = -15
            I[I>=50] = 50
        else:
            I[I<=0.0] = -200
    plt.figure(1,figsize=(10,8))
    plt.subplot(2,5,1)
    plt.imshow(datasets[1], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 2.6 (Otptimistic)")
    plt.subplot(2,5,6)
    plt.imshow(datasets[2], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 2.6 (Pessimistic)")
    plt.subplot(2,5,2)
    plt.imshow(datasets[3], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 4.5 (Otptimistic)")
    plt.subplot(2,5,7)
    plt.imshow(datasets[4], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 4.5 (Pessimistic)")
    plt.subplot(2,5,3)
    plt.imshow(datasets[5], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 6.0 (Otptimistic)")
    plt.subplot(2,5,8)
    plt.imshow(datasets[6], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 6.0 (Pessimistic)")
    plt.subplot(2,5,4)
    plt.imshow(datasets[7], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 8.5 (Otptimistic)")
    plt.subplot(2,5,9)
    plt.imshow(datasets[8], cmap="terrain")
    plt.axis("off")
    plt.title("RCP 8.5 (Pessimistic)")
    plt.subplot(2,5,5)
    plt.imshow(datasets[0], cmap="terrain")
    plt.axis("off")
    plt.title("Island as of 2015")
    plt.show()