import time
import imageio as iio

from installizer.tools_pywin.pywin_keyboard import press_key
from installizer.tools_pywin.dico import CODE
from installizer.tools_pywin.screen import screenshot

from installizer.window_exploration.detection_boutons.traitement_fonctions import diff_pt, coord_rect, in_rectangle
from window_exploration.detection_boutons.detection_coins_image import liste_coins

from installizer.id_image import id


def liste_rectangles(img, taille=9):
    """
    Retourne la liste des rectangles se trouvant sur une image.

    taille = largeur/hauteur de la zone cherchée, relative au coin 
    """
    list_rect = []
    list_coins = liste_coins(img)
    for couple in list_coins:
        i, j = couple
        for a in range(-taille, taille+1):
            for b in range(-taille, taille+1):
                if diff_pt(img, i+a, j+b):
                    if list_rect == []:
                        list_rect.append(coord_rect(img, i+a, j+b))
                    else:
                        k = 0
                        stop = False
                        while k < len(list_rect) and not(stop):
                            marge = 1
                            if in_rectangle(i+a, j+b, list_rect[k], marge):
                                stop = True
                            k += 1
                        if not(stop):
                            list_rect.append(coord_rect(img, i+a, j+b))
    return list_rect


def initiate(list_id_window, path1, path1_bis, path_diff_initiale, max_ite):
    """
    En faisant des différences de screen entre 2 fenetres successives, 
    on peut trouver l'ensemble des rectangles/boutons de la fenetre.

    La difficulté est de trouver quel bouton est obtenu lorsque l'on presse 
    un certain nombre de fois la touche tab.

    Cet algorithme vise à appuyer un certain nombre de fois sur tab 
    jusqu'à trouver une configuration où les 2 prochains boutons sont 
    identifiables (on connait leur position).

    Cela n'est pas toujours possible (cas d'un seul bouton, ou installer qui
    met en surbrillance plusieurs boutons à la fois)
    """
    ind = 1

    while (ind <= max_ite):

        screenshot(path1)
        image_ref = iio.imread(path1)

        press_key(CODE["tab"])
        time.sleep(0.7)

        screenshot(path1_bis)
        image = iio.imread(path1_bis)

        diff = image - image_ref
        iio.imwrite(path_diff_initiale, diff)

        list_rect = liste_rectangles(diff)

        if len(list_rect) == 0:  # un seul bouton (on ne sait pas ses coordonnées)
            print("unique bouton")
            list_id_window.append(id(path1))
            return []

        elif len(list_rect) >= 3:
            pass  # plus de 3 boutons est une situation complexe, on ne peut rien savoir

        elif len(list_rect) == 1:
            pass  # un bouton manque à l'appel, situation anormale, on ne peut rien savoir

        else:
            rect = list_rect[0]  # [i1,j1,i2,j2]
            px = diff[rect[0]][rect[1]+5][0]
            if px != 52:
                rect = list_rect[1]
                list_rect = [rect, list_rect[0]]
                px = diff[rect[0]][rect[1]+5][0]
            if px == 52:    # cette valeur fonctionne que pour un installer type windows
                list_id_window.append(id(path1))
                list_id_window.append(id(path1_bis))
                return list_rect
        ind += 1
