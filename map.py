import re
import numpy as np

def divide(input_str, maps_number):
    #divise une string en plusieurs listes de mots de tailles à peu près égales
    main_words_list = [word.casefold() for word in re.findall(r'\w+', input_str)]
    return [main_words_list[i::maps_number] for i in range(maps_number)]

def modulo(input_str, dividing_number):
    # retourne le modulo de la somme ascii de chaque caractère d'une string
    sum_ascii = 0
    for char in input_str:
        sum_ascii+=ord(char)
    return sum_ascii%dividing_number

def map(words_list,reduces_number):
    #map les mots d'une liste en les plaçant dans une partie d'un dictionnaire, selon leur modulo
    # exemple : ['salutn', 'est', 'salutn', 'a', 'salutn', 'salutn'] -> {'0': {'est': 1}, '1': {'salutn': 4, 'a': 1}}
    dict={}
    for i in range(0,reduces_number):
        dict[str(i)]={}
    for word in words_list:
        reduce_index = str(modulo(word,reduces_number))
        if word in dict[reduce_index]:
            dict[reduce_index][word]+=1
        else:
            dict[reduce_index][word]=1
    return(dict)


def write_map_json(map_dict, filepath):
    #ecrit le contenu d'une liste mappée de mots dans un fichier json
    with open(filepath, 'w') as f:
        f.write(str(map_dict).replace("'",'"'))
    f.close()



