
import pyocr
import pyocr.builders

from PIL import Image
import cv2 as cv

from installizer.window_exploration.lire_texte_bouton.tools.zoom import zoom

pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

tools = pyocr.get_available_tools()
# print(len(tools))

tool = tools[0]
#print("Tools: ", tool.get_name())
#print("Available languages: ", tool.get_available_languages())


def text_from_image(pre_path, name, extension, data_label):

    img = cv.imread(pre_path+name+extension)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img, 90, 255, cv.THRESH_BINARY)

    path = pre_path+name+'_filtered'+extension
    cv.imwrite(path, thresh)

    img = cv.imread(path)
    img = zoom(img)

    path = pre_path+name+'_filtered_zoomed'+extension
    cv.imwrite(path, img)

    img = Image.open(path)

    txt = tool.image_to_string(
        img,
        lang='eng',
        builder=pyocr.builders.TextBuilder()
    )

    # print("longueur du text :" + str(len(txt)))
    f = open(pre_path+data_label+".txt", "w")
    f.write(txt)
    f.close()


# pre_path = 'c:\\Users\\lhs\\Documents\\images\\'
# name = 'screen_buttons'  # name = 'screen_vm.png'
# extension = '.png'
# data_label = 'data'

# text_from_image(pre_path, name, extension, data_label)
