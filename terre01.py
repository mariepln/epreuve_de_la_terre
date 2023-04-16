# -*- coding: utf-8 -*-

#variable intégrée

file_path = __file__

file_name = file_path.split("/")[-1]

print(file_name)

#OU, appel au module OS pour afficher nom fichier en cours d'exec

#import os

#print(os.path.basename(__file__))

