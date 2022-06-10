import cv2 as cv
import numpy as np


def zoom(img, facteur=8):
    n, p = np.shape(img)[:2]
    return cv.resize(img, (facteur*p, facteur*n), interpolation=cv.INTER_NEAREST)

# pre_path = 'c:\\Users\\lhs\\Documents\\images\\'
# name = 'screen_buttons'  # name = 'screen_vm.png'
# extension = '.png'
# path = pre_path+name+extension

# img = cv.imread(path)
# zoomed = zoom(img, 10)
# cv.imwrite(pre_path+'screen_zoom.png', zoomed)
