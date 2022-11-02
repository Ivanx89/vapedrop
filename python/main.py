import sys
from tabulate import tabulate

def gcalc():
    print("\n----------------------------")
    print("General Calculator")
    print("----------------------------")


    #Ingredients:
    name    = input("Name of the flavor: ")
    totalml = int(input("Total ammount to make in mL [50/100]: "))
    nic     = float(input("Nicotine concentration in mg/mL [1.6/3]: "))
    flavor  = int(input("Flavor concentration in %: "))
    print(f"\nTo make {totalml}mL of {name} at {flavor}, you will have to mix:")

    flavorml  = totalml/flavor
    base      = totalml-flavorml
    nicokit10 = 0
    nicokit20 = 0

    #Per 100Ml of liquid:
    if totalml == 100:
        if nic == 1.6:
            nicokit10 = 2
            base = base - 20
        elif nic == 3:
            nicokit20 = 2
            base = base - 20
    elif totalml == 50:
        if nic == 1.6:
            nicokit10 = 1
            base = base - 10
        elif nic == 3.0:
            nicokit20 = 1
            base = base - 10
    else:
        print("Ha habido un error.")

    print(float(nicokit20))
    recipe = [[base, flavorml, nicokit20, nicokit10]]

    # create header
    head = ["Concentrate(mL)", "Base(mL)", "Nicokit 10(u)", "Nicokit 20(u)"]

    print(tabulate(recipe, headers=head, tablefmt="grid"))



def startup():

    #STARTUP
    print('''   
              \ \    / /\   |  __ \|  ____|  __ \|  __ \ / __ \|  __ \ 
               \ \  / /  \  | |__) | |__  | |  | | |__) | |  | | |__) |
                \ \/ / /\ \ |  ___/|  __| | |  | |  _  /| |  | |  ___/ 
                 \  / ____ \| |    | |____| |__| | | \ \| |__| | |     
                  \/_/    \_\_|    |______|_____/|_|  \_\\____/|_| \n''')
    print("----------------------------")
    print("[1] General Calculator")
    print("[2] Inventory Calculator")
    print("[3] Quit")
    print("----------------------------")

    election = input("Select you choice: \n -> ")
    
    if election == "3":
        print("Bye!")
        sys.exit()
    elif election == "2":
        print("Dos")
    elif election == "1":
        gcalc()
    else:
        print("Select a valid option")
        startup()

startup()


