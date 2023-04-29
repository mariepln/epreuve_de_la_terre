# -*- coding: utf-8 -*-

#Créez un programme qui détermine si une liste d’entiers est triée ou pas.

import sys

if len(sys.argv) == 1 :
    print("Veuillez entrer une liste de nombres")
else:
    try:
        numbers = []
        for arg in sys.argv[1:]:
            numbers.append(int(arg))

        liste_triee = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                liste_triee = False
                break

        if liste_triee:
            print("Triée.")
        else:
            print("Pas triée.")
    except ValueError:
        print("Veuillez entrer des entiers")


