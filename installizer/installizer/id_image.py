# import hashlib

# def id(path):
#     with open(path, "rb") as img:
#         img_byte = img.read()
#         result = hashlib.sha256(img_byte)
#         hash = result.hexdigest()
#         hash = int(hash, 16)
#         return hash

from PIL import Image
import imagehash


def id(path):
    hash = imagehash.dhash(Image.open(path))
    return str(hash)
