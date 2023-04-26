# -*- coding: utf-8 -*-

import sys 

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])

    if n1 < n2 < n3 or n3 < n2 < n1:
        print(n2)
    elif n2 < n1 < n3 or n3 < n1 < n2: 
        print(n1)
    elif n1 < n3 < n2 or n2 < n3 < n1:
        print(n3) 
    else:
        print("Les 3 nombres doivent être différents")
except:
    print("erreur")
            

