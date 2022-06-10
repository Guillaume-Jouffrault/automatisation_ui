from window_exploration.detection_boutons.initialisation import initiate
from installizer.window_exploration.detection_boutons.traitement import traitement

from window_exploration.lire_texte_bouton.lire_text import text_from_list_buttons

from window_exploration.analyse_texte_bouton.analyse_texte import l_back, l_cancel, l_next, id_bouttons

from installizer.tools_pywin.pywin_keyboard import press_key
from installizer.tools_pywin.dico import CODE

from installizer.fenetre import Fenetre


def exploration(graph):

    # -----------------------------------

    pre_path1 = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\'
    file_name1 = 'reference.bmp'
    path1 = pre_path1 + file_name1
    file_name1_bis = 'reference_bis.bmp'
    path1_bis = pre_path1 + file_name1_bis

    pre_path2 = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\'
    file_name2 = 'actual.bmp'
    path2 = pre_path2 + file_name2

    pre_path_diff = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\'
    path_diff_initiale = pre_path_diff+'diff_initiale'+'.bmp'

    max_ite = 13

    # -----------------------------------

    list_id_window = []

    list_rect = initiate(list_id_window, path1,
                         path1_bis, path_diff_initiale, max_ite)

    assert list_rect is not None, "L'initialisation n'a pas aboutie"
    un_seul_bouton = (list_rect == [])

    # print("liste_initiale : ", end="")
    # print(list_rect)
    # print(45*"-")

    # -----------------------------------

    if un_seul_bouton:
        print("un seul bouton")
        # return [[0], [], [], []]
        return []

    if not(un_seul_bouton):
        ind = traitement(list_id_window, list_rect,
                         path1, path2, pre_path_diff, max_ite)
        assert ind is not None, "Le traitement n'a pas abouti"

        number_of_buttons = len(list_id_window)
        button_number = 0
        for id in list_id_window:
            fen_actuelle = Fenetre(id, button_number, number_of_buttons)
            evenmt = "TAB"
            key = fen_actuelle.get_key(evenmt)

            if button_number == number_of_buttons-1:
                ind_fen_prochaine = 0
            else:
                ind_fen_prochaine = button_number+1
            id_fen_prochaine = list_id_window[ind_fen_prochaine]
            fen_prochaine = Fenetre(
                id_fen_prochaine, ind_fen_prochaine, number_of_buttons)

            graph.graph[key] = fen_prochaine
            button_number += 1

        new_id = list_id_window[0]
        new_fen = Fenetre(new_id, 0, number_of_buttons)
        return list_rect, new_fen

        # -----------------------------------
        # print(45*"$")
        # print("nombre de boutons : "+str(len(list_rect)))
        # print(list_rect)
        # ---------------------------------------------
        # text_from_list_buttons(
        #     path1, path1_bis, pre_path_button, list_rect, offset)

        # nb_bouttons = len(list_rect)
        # m = id_bouttons(nb_bouttons, pre_path_button, l_next, l_cancel, l_back)

        # return m
        # ---------------------------------------------
