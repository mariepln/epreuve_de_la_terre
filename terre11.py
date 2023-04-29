# -*- coding: utf-8 -*-

#24 o 12

import sys

try:
    heure_argument = sys.argv[1]
    hh_arg, mm_arg = heure_argument.split(":")
    hh = int(hh_arg)
    mm = int(mm_arg)

    def format_12h_soir(hh):
        heure12 = hh - 12
        if 13 <= hh <= 23 :
            return heure12
        return None

    def format_12h_matin(hh):
        if 1 <= hh <= 11:
            return hh
        return None
    
    def format_12h_midi(hh):
        if hh == 12:
            return hh
        return None

    def format_12h_minuit(hh):
        if hh == 00:
            return 12
        return None
    

    if mm > 59:
        print("les minutes de dépassent pas 59...")
    else:
        if format_12h_soir(hh) is None:
            format_12h_matin(hh)
            if format_12h_matin(hh) is None:
                format_12h_midi(hh)
                if format_12h_midi(hh) is None:
                    format_12h_minuit(hh)
                    if format_12h_minuit(hh) is None:
                        print("veuillez indiquer un bon format")
                    else:
                        print("12:{:02d}PM".format(mm))
                else:
                    print("{}:{:02d}AM".format(hh, mm))
            else:
                print("{}:{:02d}AM".format(hh, mm))
        else:
            print("{}:{:02d}PM".format((hh - 12), mm)) # caractère de remplissage 0, largeur 2 caractères

except:
    print("erreur")





    



