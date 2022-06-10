from installizer.window_exploration.exploration import exploration

from installizer.fenetre import Fenetre

from installizer.tools_pywin.screen import screenshot

import subprocess

from installizer.tools_pywin.dico import CODE
from installizer.tools_pywin.pywin_keyboard import press_key
from installizer.tools_pywin.close_window import close_window

from installizer.shortest_path import shortest_path

from installizer.create_dot import create_dot
import time

from installizer.id_image import id
from installizer.window_exploration.lire_texte_bouton.lire_text import text_from_list_buttons
from installizer.window_exploration.analyse_texte_bouton.analyse_texte import id_bouttons, l_back, l_cancel, l_next

# AbstractApp
# AbstractWindow
# AbstractEvenmt

pre_path1 = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\'
file_name1 = 'reference.bmp'
path1 = pre_path1 + file_name1
file_name1_bis = 'reference_bis.bmp'
path1_bis = pre_path1 + file_name1_bis
pre_path_button = 'c:\\Users\\lhs\\Documents\\images\\algo\\boutons\\'
offset = 3


class Graphe:
    """
    la classe AbstractApp
    """

    def __init__(self, exe, path):
        """ 
        self.graph : dictionnaire = evenement+str(id_fen) -> fen
        self.exe : nom de l'executable à installer
        self.path : ***********************************
        self.list_id_window_buttons : liste des id de l'ensemble des bouttons *****a confirmer******
        """
        self.graph = {}
        self.exe = exe
        self.path = path
        self.list_id_window_buttons = []

    def start(self, DURATION_LAUNCH_EXE):
        """
        lance l'executable et accede à la premiere fenetre 
        """
        subprocess.Popen(self.exe, shell=True)
        time.sleep(DURATION_LAUNCH_EXE)
        screenshot(self.path)
        return id(self.path)

    def close(self):
        close_window()

    def explore(self, analysis):
        """
        quand on arrive dans une nouvelle fenetre :
        test si la fenetre a déjà été découverte
        si elle ne l'a pas été : on lance l'algo d'explo 
        et on crée des objs fen pour chaque boutton
        """
        list_rect, new_fen = exploration(self)
        if not analysis:
            return new_fen
        else:
            text_from_list_buttons(
                path1, path1_bis, pre_path_button, list_rect, offset)
            nb_rect = len(list_rect)
            m = id_bouttons(nb_rect, pre_path_button, l_next, l_cancel, l_back)
            if len(m[0]) > 0:
                i = m[0][0]
            elif len(m[3]) > 0:
                i = m[3][0]
            elif len(m[2]) > 0:
                i = m[2][0]
            elif len(m[1]) > 0:
                i = m[1][0]
            else:
                raise Exception("Boutons not corresponding to any label")
            best_fen = new_fen
            for _ in range(i):
                press_key(CODE['tab'])
                time.sleep(0.7)
                best_fen = self.graph["TAB"+str(best_fen.id)]
            return best_fen

    def next(self, W, evenmt):
        """
        clique sur le bouton présent sur la fenetre W
        """
        if evenmt == "CLIC":
            time.sleep(1)
            press_key(CODE['enter'])
            time.sleep(0.7)
            screenshot(self.path)
            id_fen = id(self.path)
            new_fen = Fenetre(id_fen, 0, 0)  # check this behavior
            self.graph[evenmt+str(W)] = new_fen
            return id_fen
        if evenmt == "TAB":
            press_key(CODE['tab'])
            time.sleep(0.7)
            screenshot(self.path)
            return id(self.path)

    def move(self, fen, fen2):
        """
        retourne la liste des évenements pour aller de fen jusqu'à fen'
        """
        return shortest_path(self.graph, fen, fen2)

    def apply(self, W, list_evenmt):
        """
        applique la liste des évènements (eg next next cancel ...)
        list_evenmt est une liste de couples (fen,evenmt)
        retourne la fen sur laquelle on arrive
        """
        assert len(list_evenmt) >= 1, "list_evenmt est une liste vide"
        assert W == list_evenmt[0][0].id, "cant apply because start is not matching W"
        for fen, evenmt in list_evenmt:
            if evenmt == 'TAB':
                press_key(CODE['tab'])
            elif evenmt == 'CLIC':
                press_key(CODE['enter'])
        return list_evenmt[-1][0]

    def print_graph(self, path):
        create_dot(self.graph, path)
