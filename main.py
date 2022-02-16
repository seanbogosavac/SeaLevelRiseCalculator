# main.py
#

import sys

import src.sealevel as sl


args = sys.argv

if len(args) > 1:
    focus = False
    colorbar = True
    dataset = ""
    year = 2000

    if args[1] == "-help" or args[1] == "--h" :
        print("\n\nSea Level Rise Calculator -- Help page\n")
        print("usage: python3 main.py [-sealevel | -dike] [dataset] [scenario] [arg] ...\n")
        print("Options and arguments:")
        print("-sealevel    (--sl): Computes a map of the specified island after the specified scenario")
        print("-dike        (--dk):")
        print("-focus        (--f): Flaten the highest altitude to enable a greater range of values for the lower altitudes")
        print("-nocolorbar  (--nc): Does not show the colorbar on the final map (!Enabled and can't disable when choosing all scenarios!)")
        print("-year         (--y): Using -year=xxxx shows the result of the simulation on year xxxx (!Must be after 2000!)\n")
        print("Datasets avaliables (!Only for -sealevel!):")
        print("- SP               : Uses the St-Pierre island dataset")
        print("- M                : Uses the Miquelon island dataset")
        print("- all              : Uses the whole St-Pierre-et-Miquelon island dataset\n")
        print("Scenarios avaliables:")
        print("- all              : Shows one map per scenario to facilitate comparison")
        print("- none             : Show the specified dataset without any modification")
        print("- 26min            : Uses the optimistic RCP 2.6 scenario")
        print("- 26max            : Uses the pessimistic RCP 2.6 scenario")
        print("- 45min            : Uses the optimistic RCP 4.5 scenario")
        print("- 45max            : Uses the pessimistic RCP 4.5 scenario")
        print("- 60min            : Uses the optimistic RCP 6.0 scenario")
        print("- 60max            : Uses the pessimistic RCP 6.0 scenario")
        print("- 85min            : Uses the optimistic RCP 8.5 scenario")
        print("- 85max            : Uses the pessimistic RCP 8.5 scenario")

    elif args[1] == "-sealevel" or args[1] == "--sl":
        dataset = args[2]
        scenario = args[3]
        for arg in args[4:]:
            if arg == "-focus" or arg == "--f": focus = True
            if arg == "-nocolorbar" or arg == "--nc": colorbar = False
            if "-year=" in arg or "--y=" in arg: year = int(arg.split('=')[1])
        sl.seaLevel(dataset, scenario, year, focus, colorbar)

    
    else: 
        sys.exit("\n\nError! First argument invalid\n\n")


else:
    sys.exit("\n\nError! No arguments specified\n Type python3 main.py -help to get assistance running this script\n\n")