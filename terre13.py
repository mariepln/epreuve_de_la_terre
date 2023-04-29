# -*- coding: utf-8 -*-

import sys 

try:
    
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])

    if len(sys.argv) > 4:
        print("veuillez entrer seulement 3 arguments")
    else:
        if n2 < n1 < n3 or n3 < n1 < n2: 
            print(n1)
        elif n1 < n2 < n3 or n3 < n2 < n1:
            print(n2)
        elif n1 < n3 < n2 or n2 < n3 < n1:
            print(n3) 
        else:
            print("Les 3 nombres doivent être différents")

except IndexError:
    print("Veuillez entrer le bon nombre d'arguments")
except ValueError:
    print("Veuillez entrer un nombre entier")

    


            

