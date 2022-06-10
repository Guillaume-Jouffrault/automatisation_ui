import numpy as np
from window_exploration.detection_boutons.detection_coins_image import liste_coins


def diff_pt(diff, i, j, gray=False):
    if gray:
        return diff[i][j] >= 1
    else:
        return not(np.array_equal(diff[i][j], [0, 0, 0]))


def coord_rect(diff, i, j, gray=False):
    n, p = np.shape(diff)[0:2]

    h = 1
    finish = False
    while i+h < n and not(finish):
        if i+h < n and diff_pt(diff, i+h, j, gray):
            h += 1
        elif i+h+1 < n and diff_pt(diff, i+h+1, j, gray):
            h += 2
        else:
            finish = True

    w = 1
    finish = False
    while j+w < p and not(finish):
        if j+w < p and diff_pt(diff, i, j+w, gray):
            w += 1
        elif j+w+1 < p and diff_pt(diff, i, j+w+1, gray):
            w += 2
        else:
            finish = True

    # +-1 car les bords sont arrondis (1px en moins)
    return [i, j, i+h-1, j+w-1]


def in_rectangle(i, j, rect, marge=1):
    # on laisse une marge de 1px (ca peut differer)
    return (i >= rect[0]-marge and j >= rect[1]-marge and i <= rect[2]+marge and j <= rect[3]+marge)


def rect_location(diff, list_rect, width=9):
    list_PI = liste_coins(diff, True)
    for couple in list_PI:
        i, j = couple
        for a in range(-width, width+1):
            for b in range(-width, width+1):
                if diff_pt(diff, i+a, j+b, True):
                    ind = 0
                    while ind < len(list_rect) and not(in_rectangle(i+a, j+b, list_rect[ind])):
                        ind += 1
                    if ind == len(list_rect):
                        list_rect.append(coord_rect(diff, i+a, j+b, True))
                        return False
    return True
