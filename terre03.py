# -*- coding: utf-8 -*-

#alphabet à partir d'une lettre donnée en argument ligne commande 
#on reprend ex00 et ex02

import sys 

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in sys.argv[1:]:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_alphabet = alphabet[position:]
        print(new_alphabet)
    else:
        print("Veuillez choisir une lettre de l'alphabet en minuscule")
