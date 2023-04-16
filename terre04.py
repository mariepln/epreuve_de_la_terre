# -*- coding: utf-8 -*-

#vérifier qu'il y ai au moins 1 argument
#parcourir l'argument donné et vérifier que ce soit bien un entier positif
#renvoyer messages d'erreur si pas un entier positif

import sys


if len(sys.argv) == 1:
    print("Tu ne me la mettras pas à l’envers.")
else:
    for number in sys.argv[1:]:
        try:
            number = int(number)
            if number < 0:
                print("entrez un entier positif")
            elif number % 2 == 0:
                print("pair")
            elif number % 2 != 0:
                print("impair")
        except:     #je choisi de renvoyer ce message pour toute erreur (j'aurais pu notre ValueError) 
            print("Tu ne me la mettras pas à l’envers.")
    



   

