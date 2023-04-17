# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    print("Erreur: veuillez entrer argument valide")

for argument in sys.argv [1:]:
    if argument.isspace():
        print("Erreur: veuillez entrer argument valide")
    else:
        print(argument[::-1])






