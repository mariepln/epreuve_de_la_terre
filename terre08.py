# -*- coding: utf-8 -*-

#calculer la puissance : opérateur **

import sys

try:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
    result = number1 ** number2
    if number2 < 0:
        print("erreur")
    elif len(sys.argv) > 2:
        print("erreur")
    else:
        print(result)
except:
    print("erreur")