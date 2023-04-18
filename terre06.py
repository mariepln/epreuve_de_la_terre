# -*- coding: utf-8 -*-

import sys

try:
    argument = sys.argv[1]
    if len(sys.argv) > 2 or argument.isnumeric():
        print("erreur.")
    else:
        print(argument[::-1])
except IndexError:
    print("erreur.")







