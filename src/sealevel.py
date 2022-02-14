# sealevel.py
# This file contains the function related to the process of computing sea level rise.

import sys
import numpy as np

import src.display as dp
import src.data as dt
import src.func as fc

def seaLevel(dataset, scenario, year, focus, colorbar):
    map = dt.Islands

    if dataset == "SP":
        print("\n\nComputing for St-Pierre island")
        map = dt.StPierre
    elif dataset == "M":
        print("\n\nComputing for Miquelon island")
        map = dt.Miquelon
    elif dataset == "all":
        print("\n\nComputing for the whole St-Pierre-et-Miquelon islands")
        map = dt.Islands
    else: sys.exit("\n\nError! The choice of dataset is invalid.\nType python3 main.py -help to get assistance running this script\n\n")



    if year < 2000:
        sys.exit("\n\nError, this script is meant to be used for years after 2000\nType python3 main.py -help to get assistance running this script\n\n")



    if scenario == "all":
        print("Computing for all IPCC scenarios")
        maps = [np.copy(map) for i in range(9)]
        maps[1] = fc.applyScenario(maps[1], "26min")
        maps[2] = fc.applyScenario(maps[2], "26max")
        maps[3] = fc.applyScenario(maps[3], "45min")
        maps[4] = fc.applyScenario(maps[4], "45max")
        maps[5] = fc.applyScenario(maps[5], "60min")
        maps[6] = fc.applyScenario(maps[6], "60max")
        maps[7] = fc.applyScenario(maps[7], "85min")
        maps[8] = fc.applyScenario(maps[8], "85max")
        dp.displayAll(maps, focus, colorbar)

    elif scenario == "26min":
        print("Computing for the optimistic RCP 2.6 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "26max":
        print("Computing for the pessimistic RCP 2.6 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "45min":
        print("Computing for the optimistic RCP 4.5 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "45max":
        print("Computing for the pessimistic RCP 4.5 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "60min":
        print("Computing for the optimistic RCP 6.0 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "60max":
        print("Computing for the pessimistic RCP 6.0 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "85min":
        print("Computing for the optimistic RCP 8.5 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)
    elif scenario == "85max":
        print("Computing for the pessimistic RCP 8.5 scenario")
        map = fc.applyScenario(map, scenario, year)
        dp.display(map, focus, colorbar)

    elif scenario == "none":
        print("Applying no scenarios")
        dp.display(map, focus, colorbar)

    else: sys.exit("\n\nError! The choice of scenario is invalid.\nType python3 main.py -help to get assistance running this script\n\n")