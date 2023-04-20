# -*- coding: utf-8 -*-

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