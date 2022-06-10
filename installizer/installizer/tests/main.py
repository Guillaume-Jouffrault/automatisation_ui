from installizer.tools_pywin.window_name import window_name
from installizer.graphe import Graphe
from installizer.fenetre import Fenetre
import time

from installizer.tools_pywin.pywin_keyboard import press_key
from installizer.tools_pywin.dico import CODE

n = 1
nmax = 4
DURATION_LAUNCH_EXE = 20

EXE = "C:\\Users\\lhs\\Documents\\logiciels\\putty-64bit-0.76-installer.msi"
PATH = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\actual.bmp'
PATH_DOT = 'c:\\Users\\lhs\\Documents\\installizer\\installizer\\output.dot'

G = Graphe(EXE, PATH)

W = G.start(DURATION_LAUNCH_EXE)   # W = CONCRETE_WINDOW = id of actual window
# met en route l'exe et return id fenetre
print(W)

new_fen = G.explore()
W = new_fen.id
print(W)

W = G.next(W, "CLIC")  # met à jour le graphe et return W
print(W)

W = G.next(W, "CLIC")
print(W)

W = G.next(W, "TAB")
print(W)

# W = G.next(W, "CLIC")
# print(W)

time.sleep(2)
G.close()


G.print_graph(PATH_DOT)
