from installizer.tools_pywin.window_name import window_name
from installizer.graphe import Graphe
from installizer.fenetre import Fenetre
import time

from window_exploration.exploration import exploration

n = 1
nmax = 4
DURATION_LAUNCH_EXE = 6

EXE = "C:\\Users\\lhs\\Documents\\logiciels\\putty-64bit-0.76-installer.msi"
#EXE = "C:\\Users\\lhs\\Documents\\logiciels\\smartorg"
PATH = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\actual.bmp'
PATH_DOT = 'c:\\Users\\lhs\\Documents\\installizer\\installizer\\output.dot'

G = Graphe(EXE, PATH)
W = G.start(DURATION_LAUNCH_EXE)   # W = CONCRETE_WINDOW = id of actual window
W_NAME_INIT = window_name()
ANALYSIS = True

print(23*"\n"+55*"&")

list_id_fen_clicked = []
finish = False

while (not(finish)):
    W_name = window_name()
    if W_name != W_NAME_INIT:
        W = G.start(DURATION_LAUNCH_EXE)
    else:
        print(0)
        W_key = "TAB"+str(W)
        print(45*"-")
        print(W_key)
        print(45*"-")
        if W_key not in G.graph:
            print("1,victorieux")
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # il faut se rendre au point d'initialisation de l'exploration
            new_fen = G.explore(ANALYSIS)
            W = new_fen.id
            list_id_fen_clicked.append(W)
            W = G.next(W, "CLIC")
        else:
            print(1)
            if W not in list_id_fen_clicked:
                print("2,victorieux")
                list_id_fen_clicked.append(W)
                W = G.next(W, "CLIC")
            else:
                print(2)
                found = False
                W_to_voisin = W
                fen_voisin = G.graph["TAB"+str(W_to_voisin)]
                while (fen_voisin.id != W):
                    if not(found) and fen_voisin.id not in list_id_fen_clicked:
                        found = True
                        new_fen = fen_voisin
                        new_W = fen_voisin.id
                    W_to_voisin = fen_voisin.id
                    fen_voisin = G.graph["TAB"+str(W_to_voisin)]
                fenW = fen_voisin
                if found:
                    print("3,victorieux")
                    list_id_fen_clicked.append(new_W)
                    list_evenmt = G.move(fenW, new_fen)
                    new_fen = G.apply(W, list_evenmt)
                    W = G.next(new_W, "CLIC")
                else:
                    print(3)
                    found = False
                    for key in G.graph:
                        fen = G.graph[key]
                        list_evenmt = G.move(fenW, fen)  # [(fen,evenmt)]
                        if not(found) and (fen.id not in list_id_fen_clicked) and len(list_evenmt) >= 1:
                            found = True
                            list_id_fen_clicked.append(fen.id)
                            new_fen = G.apply(W, list_evenmt)
                            W = G.next(new_W, "CLIC")
                    if found:
                        print("4,victorieux")
                    if not(found):
                        print(4)
                        for key in G.graph:
                            fen = G.graph[key]
                            if not(found) and (fen.id not in list_id_fen_clicked):
                                found = True
                                W = G.start(DURATION_LAUNCH_EXE)
                                fen_start_voisin = G.graph["TAB"+str(W)]
                                fen_start = Fenetre(
                                    W, 0, fen_start_voisin.number_of_buttons)

                                list_evenmt = G.move(fen_start, fen)
                                new_fen = G.apply(W, list_evenmt)
                                list_id_fen_clicked.append(fen.id)
                                W = G.next(new_W, "CLIC")
                    if found:
                        print("5,victorieux")
                    else:
                        print(5)
                        finish = True

    print(list_id_fen_clicked)
    G.print_graph(PATH_DOT)

# gerer le cas où une fenetre est ouverte hors de l'installer
