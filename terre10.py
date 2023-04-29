# -*- coding: utf-8 -*-

#Créez un programme qui affiche si un nombre est premier ou pas.
#Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.

import sys

try:
    number = int(sys.argv[1])
    number_prime = True


    for diviseur in range(2, number):
        result = number / diviseur
        if diviseur < number and result.is_integer():
            number_prime = False
            break


    if number < 0:
     print("erreur")
    elif number_prime:
        print("Oui,", number, "est un nombre premier.")
    else:
        print("Non,", number, "n'est pas un nombre premier.")
except:
    print("erreur") 