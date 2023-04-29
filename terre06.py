# -*- coding: utf-8 -*-

#Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.

import sys

try:
    argument = sys.argv[1]
    if len(sys.argv) > 2 or argument.isnumeric():
        print("erreur.")
    else:
        print(argument[::-1])
except IndexError:
    print("erreur.")







