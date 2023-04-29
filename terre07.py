# -*- coding: utf-8 -*-

#Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.

#utilisation d'un compteur pr éviter d'utiliser len()

import sys

try:
    counter_char = 0
    sentence = sys.argv[1]

    for characters in sentence:
        counter_char += 1

    if sentence.isnumeric():
        print("erreur d'argument.")
    elif len(sys.argv) > 2:
        print("erreur d'argument.")
    else:
        print(counter_char) 
except IndexError:
    print("erreur.")





