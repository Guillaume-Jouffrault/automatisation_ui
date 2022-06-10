import cv2
import numpy as np


def filtre_des_coins(l, taille_zone):
    """
    Un bouton correspond généralement à 4 zones dans chacune desquelles
    on retrouve plusieurs coins.
    Cette fonction vise à ne conserver qu'un seul coin pour chaque zone de coins.

    l = liste des coins (obtenue par la fonction liste_coins).
    taille_zone = largeur/hauteur d'une zone de coin.
    """
    i = 0
    while i < len(l):
        j = 0
        while j < len(l):
            if j != i:
                if abs(int(l[i][0])-int(l[j][0])) < taille_zone:
                    if abs(int(l[i][1])-int(l[j][1])) < taille_zone:
                        l = np.delete(l, j, 0)
                    else:
                        l[j][0] = l[i][0]
                        if (i < j and l[i][1] > l[j][1]) or (i > j and l[i][1] < l[j][1]):
                            tmp = l[i][1]
                            l[i][1] = l[j][1]
                            l[j][1] = tmp
                        j += 1
                else:
                    j += 1
            else:
                j += 1
        i += 1
    return l


def liste_coins(img, gray=False):
    """
    retourne la liste des coins d'une image, c'est-à-dire les points de l'image
    où les valeurs des pixels varient fortement 
    (par ex, un pixel noir entouré de pixels blanc est un coin).

    Cela permet un gain de temps car on ne parcourt pas la totalité de l'image
    mais seulement les zones où sont situées les coins.

    L'algorithme utilisé est le "Harris corner detector".

    gray = booléen qui vaut vrai si l'image est en noir et blanc.
    """

    if not(gray):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = img

    img_gray = np.float32(img_gray)

    dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)

    mask = np.zeros_like(img_gray)
    mask[dst > 0.01*dst.max()] = 255

    liste_coins = np.argwhere(mask)

    return filtre_des_coins(liste_coins, 13)
