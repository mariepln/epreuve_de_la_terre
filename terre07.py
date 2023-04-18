# -*- coding: utf-8 -*-

#utilisation d'un compteur pr éviter d'utiliser len()

import sys

try:
    counter_char = 0
    sentence = sys.argv[1]

    for characters in sentence:
        counter_char += 1

    if sentence.isnumeric():
        print("erreur.")
    elif len(sys.argv) > 2:
        print("erreur.")
    else:
        print(counter_char) 
except IndexError:
    print("erreur.")





