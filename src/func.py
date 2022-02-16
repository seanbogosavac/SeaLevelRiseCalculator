# func.py
# This file contains all the functions the sealevel.py and dike.py script files are based on.

import src.data as dt


## Fuctions used in both contexts
# Since the polynomials are not meant to use a year, but an integer refering to the year, this function make the conversion:
def yearToCoeff(y):
    return int(0.25*y-499)
    

# Calculates, for a given year, the amount of sea level rise for all main RCPs:
def levelRise(scenario, year):
    glac = yearToCoeff(year + 4)
    ther = yearToCoeff(year + 15)
    if scenario == "26min":
        rise = dt.thermExp26(ther) * 0.10 + 0.01 * dt.glac26min(glac)
    elif scenario == "26max":
        rise = dt.thermExp26(ther) * 0.12 + 0.01 * dt.glac26max(glac)
    elif scenario == "45min":
        rise = dt.thermExp45(ther) * 0.10 + 0.01 * dt.glac45min(glac)
    elif scenario == "45max":
        rise = dt.thermExp45(ther) * 0.12 + 0.01 * dt.glac45max(glac)
    elif scenario == "60min":
        rise = dt.thermExp60(ther) * 0.10 + 0.01 * dt.glac60min(glac)
    elif scenario == "60max":
        rise = dt.thermExp60(ther) * 0.12 + 0.01 * dt.glac60max(glac)
    elif scenario == "85min":
        rise = dt.thermExp85(ther) * 0.10 + 0.01 * dt.glac85min(glac)
    elif scenario == "85max":
        rise = dt.thermExp85(ther) * 0.12 + 0.01 * dt.glac85max(glac)
    return rise


# Applies a specific IPCC scenario to a dataset
def applyScenario(dataset, scenario, year):
    print("Starting computing scenario")
    rise = levelRise(scenario, year)
    for j in range(200):
        for x in range(1,len(dataset)-1):
            for y in range(1,len(dataset[0])-1):
                if isFlooded(dataset, rise, x, y):
                    dataset[x][y] = -99999.0
    print("Done")
    return dataset



## Functions used to replace long if statements
# Returns True if the pixel on given coordinates is flooded
def isFlooded(dataset, rise, x, y):
    return dataset[x][y] != -99999.0 and dataset[x][y] <= rise and (dataset[x+1][y] < 0 or dataset[x][y+1] < 0 or dataset[x-1][y] < 0 or dataset[x][y-1] < 0 or dataset[x+1][y+1] < 0 or dataset[x+1][y-1] < 0 or dataset[x-1][y+1] < 0 or dataset[x-1][y-1] < 0)