import re

from window_exploration.analyse_texte_bouton.distance_levenshtein import distance


def is_letter(symbole):
    v = ord(symbole)
    return (v >= 65 and v <= 90) or (v >= 97 and v <= 122)


def valeur_mot(mot, taux_erreurs=1):
    i = 0
    n = len(mot)
    res = ""
    while(i < 3 and not(is_letter(mot[i]))):
        i += 1
    nb_erreurs = 0
    while(i < n):
        if is_letter(mot[i]):
            v = ord(mot[i])
            if v >= 65 and v <= 90:
                res += chr(v+32)
            else:
                res += mot[i]
            i += 1
        elif nb_erreurs < taux_erreurs:
            nb_erreurs += 1
            i += 1
        else:
            i = n
    return res

    # 65 90
    # 97 122

    # ord()  # char to ascii
    # chr()  # ascii to char


def valeur_boutton(path, l_next, l_cancel, l_back):

    file = open(path, 'r')
    contenu = file.read()
    file.close()

    lines = contenu.split('\n')
    nb_lines = len(lines)

    mots = re.split(' |\n', contenu)
    nb_mots = len(mots)
    print(mots)

    if nb_lines >= 2 or nb_mots >= 3:
        return 3  # others
    else:
        mot = lines[0]
        mot = valeur_mot(mot)
        for s in l_next:
            if distance(mot, s) <= 1:
                return 0  # next
        for s in l_cancel:
            if distance(mot, s) <= 1:
                return 1  # cancel
        for s in l_back:
            if distance(mot, s) <= 1:
                return 2  # back
        return 3  # others


def id_bouttons(nb_rect, pre_path, l_next, l_cancel, l_back):
    m = [[], [], [], []]
    for i in range(nb_rect):
        path = pre_path+'data_boutton'+str(i+1)+'.txt'
        id = valeur_boutton(path, l_next, l_cancel, l_back)
        m[id].append(i)
    return m


l_next = ["next", "ok", "install", "finish"]  # classe 0
l_cancel = ["cancel", "stop"]  # classe 1
l_back = ["back", "previous"]  # classe 2
l_others = []  # classe 3

# pre_path = 'c:\\Users\\lhs\\Documents\\images\\algo_succes\\boutons\\'
# name = 'data.txt'
# path = pre_path+name

# nb_rect = 5
# m = id_bouttons(nb_rect, pre_path, l_next, l_cancel, l_back)
# print(m)
