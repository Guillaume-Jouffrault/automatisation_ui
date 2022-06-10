import time
import cv2 as cv

from installizer.tools_pywin.pywin_keyboard import press_key
from installizer.tools_pywin.dico import CODE
from installizer.tools_pywin.screen import screenshot
from installizer.window_exploration.detection_boutons.traitement_fonctions import rect_location

from installizer.id_image import id


def traitement(list_id_window, list_rect, path1, path2, pre_path_diff, max_ite):

    image_ref = cv.imread(path1)

    ind = 2

    while (ind <= max_ite):

        # print(10*"*"+str(ind)+10*"*")

        press_key(CODE["tab"])
        time.sleep(0.7)

        screenshot(path2)
        image = cv.imread(path2)

        diff = image - image_ref

        diff = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

        ret, thresh = cv.threshold(diff, 1, 255, cv.THRESH_BINARY)
        diff = thresh

        finish = rect_location(diff, list_rect)  # ajoute rect a list_rect

        if finish:
            return ind

        if not(finish):  # we discovered one new button
            list_id_window.append(id(path2))
            # print(list_rect[-1])
            # print("\n")

        cv.imwrite(pre_path_diff+'diff'+str(ind)+'.bmp', diff)
        ind += 1
