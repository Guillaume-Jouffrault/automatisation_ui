# g = {}
# g['aa'] = ['A', 'B', 'C']
# g['bb'] = ['A']
# g['cc'] = ['A', 'B']
# g[10] = "test"

# print(g[10])
# print(g['aa'])

# print(g)

import hashlib
import imagehash
from PIL import Image


l = []

# for i in range(1, 6):
#     pre_path = 'c:\\Users\\lhs\\Documents\\images\\algo_succes\\boutons\\'
#     path = pre_path+'boutton'+str(i)+'_filtered_zoomed'+'.png'
#     img = Image.open(path)

#     hash = id(img)
#     # print(hash)
#     l.append(hash)


def f(path):
    img = Image.open(path)
    hash = id(img)
    return hash

# i = 1
# pre_path = 'c:\\Users\\lhs\\Documents\\images\\algo_succes\\boutons\\'
# path = pre_path+'boutton'+str(i)+'_filtered_zoomed'+'.png'


pre_path = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\'

name = 'reference'
path = pre_path+name+'.bmp'
hash1 = f(path)


def id(path):
    with open(path, "rb") as img:
        img_byte = img.read()
        result = hashlib.sha256(img_byte)
        print("!!!!!!!!!!!!")
        print(result.hexdigest())
        print("!!!!!!!!!!!!")


name = 'reference_bis'
path = pre_path+name+'.bmp'
hash2 = f(path)
print(hash2-hash1)

# g = {}
# i = 1
# for x in l:
#     print(x-l[0])
#     g[x] = i
#     i += 1

print(45*"-")
