import sys


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
        print("Uno")
    else:
        print("Select a valid option")
        startup()

startup()
