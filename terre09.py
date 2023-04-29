# -*- coding: utf-8 -*-

#Créez un programme qui affiche la racine carrée d’un entier positif.

import sys

try:
    number = int(sys.argv[1])
    result = number ** (1/2) # (n^2=b) = (b^(2/4)=n)
    if number < 0:
        print("erreur")
    elif len(sys.argv) > 2:
        print("erreur")
    else:
        print(int(result))
except IndexError:
    print("erreur.")
except ValueError:
    print("erreur.")