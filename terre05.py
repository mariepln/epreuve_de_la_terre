# -*- coding: utf-8 -*-

#Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

#créer variable pour chaque argument
#chaque argument doit ê un entier, 
#le résultat doit être entier, 
#renvoyer message d'erreur si division par 0 et si resultat < 1

import sys

for numbers in sys.argv[1:2]:
    try:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        calcul1 = number1 / number2
        calcul2 = number1 % number2 
        if number1 < number2:
            print("erreur.")
        else:  
            print('résultat:', int(calcul1))
            print("reste:", calcul2)
    except ZeroDivisionError: 
        print("Division par 0 impossible...")