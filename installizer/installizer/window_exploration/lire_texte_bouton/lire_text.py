import numpy as np
from PIL import Image

from installizer.window_exploration.lire_texte_bouton.tools.text_from_image import text_from_image


def text_from_list_buttons(path1, path1_bis, pre_path_button, list_rect, offset):

    ind = 1
    path = path1_bis
    image = Image.open(path).convert('L')
    m = np.array(image)

    for rect in list_rect:  # [i1,j1,i2,j2]

        if ind == 2:
            path = path1
            image = Image.open(path).convert('L')
            m = np.array(image)

        m_rect = np.array(m[rect[0]-offset:rect[2]+offset,
                            rect[1]-offset:rect[3]+offset])

        name = 'boutton'+str(ind)
        extension = '.png'
        Image.fromarray(m_rect).save(pre_path_button+name+extension)
        text_from_image(pre_path_button, name, extension,
                        'data_boutton'+str(ind))
        ind += 1
