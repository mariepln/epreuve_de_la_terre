# -*- coding: utf-8 -*-

#12 to 24

import sys

try:
    heure_argument = sys.argv[1]
    hh_arg, mm_arg = heure_argument.split(":")
    hh = int(hh_arg)
    mm = int(mm_arg[:-2])
    if heure_argument.endswith("AM"):
        format24 = "AM"
    elif heure_argument.endswith("PM"):
        format24 = "PM"
    else:
        raise ValueError("Format d'heure invalide")

    def format_24h_soir(hh):
        if 1 <= hh <= 11 and heure_argument.endswith("PM"):
            heure24 = hh + 12
            return heure24
        return None


    def format_24h_matin(hh):
        if 1 <= hh <= 11 and heure_argument.endswith("AM"):
            return hh
        return None

    def format_24h_minuit(hh, mm):
        if hh == 12 and heure_argument.endswith("AM"):
            return "00:{:02d}".format(mm)
        return None
    
    def format_24h_midi(hh):
        if hh == 12 and heure_argument.endswith("PM"):
            return hh
        return None

    if mm > 59:
        print("les minutes de dépassent pas 59...")
    else:
        if format_24h_soir(hh) is None:
            format_24h_matin(hh)
            if format_24h_matin(hh) is None:
                format_24h_minuit(hh, mm)
                if format_24h_minuit(hh, mm) is None:
                    format_24h_midi(hh)
                    if format_24h_midi(hh) is None:
                        print("Veuillez indiquer un bon format d'heure")
                    else:
                        print("{}:{:02d}".format(hh, mm))
                else:
                    print("00:{:02d}".format(mm))
            else:
                print("{}:{:02d}".format(hh, mm))
        else:
            print("{}:{:02d}".format(hh + 12, mm))

except IndexError:
    print("Erreur")
except ValueError:
    print("Format d'heure invalide")
