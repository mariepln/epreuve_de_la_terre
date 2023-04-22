# -*- coding: utf-8 -*-

import sys

try:
    heure_argument = sys.argv[1]
    hh_arg, mm_arg = heure_argument.split(":")
    hh = int(hh_arg)
    mm = int(mm_arg)

    def format_12h_soir(nombre):
        heure12 = nombre - 12
        if heure12 < 1 or heure12 > 11:
            return None
        return heure12

    def format_12h_matin(nombre):
        if nombre < 1 or nombre > 12:
            return None
        return nombre

    def format_12h_minuit(nombre):
        if nombre == 0:
            return 12
        else:
            return None
    

    if mm > 59:
        print("les minutes de dépassent pas 59...")
    else:
        heure12 = format_12h_soir(hh)
        if heure12 is None:
            heure12 = format_12h_matin(hh)
            if heure12 is None:
                heure12 = format_12h_minuit(hh)
                if heure12 is None:
                    print("veuillez indiquer un bon format")
                else:
                    print("{}:{:02d}PM".format(heure12, mm)) # caractère de remplissage 0, largeur 2 caractères
            else:
                print("{}:{:02d}PM".format(heure12, mm))
        else:
            print("{}:{:02d}AM".format(heure12, mm))

except:
    print("erreur")





    



