# l = [1, 2, 3]
# l.pop(-1)
# print(l)
# l.pop(-1)
# print(l)
# l.pop(-1)
# print(l)

# g = {}
# g[1] = 'a'
# g[2] = 'b'
# g[3] = 'c'
# g[4] = 'd'
# g[5] = 'e'
# print(g)
# print('a' in g)

# l = [1, 2, 3]
# l2 = list(map(lambda x: x*x, l))
# print(l2)

# l = [1, 2, 3]
# l.reverse()
# print(l)

# from subprocess import check_output

# cmd = "C:\\Users\\lhs\\Documents\\logiciels\\putty-64bit-0.76-installer.msi"
# output = check_output(cmd, shell=True)
# print(output)

# d = {}
# d[1] = 'a'
# d[2] = 'b'
# d[3] = 'c'
# d[4] = 'd'
# print(len(d))
# d[5] = 'e'
# print(len(d))

# from PIL import Image
# import imagehash
# PATH = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\test1.PNG'
# PATH2 = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\test2.PNG'

# hash = imagehash.dhash(Image.open(PATH))
# print(hash)
# print(str(hash))
# otherhash = imagehash.dhash(Image.open(PATH2))
# print(otherhash)
# print(hash == otherhash)
# print(hash - otherhash)

from PIL import Image
import imageio as iio
pre_path = 'c:\\Users\\lhs\\Documents\\images\\algo\\traitement\\'
file_name1 = 'diff_initiale.bmp'
file_name2 = 'diff2.bmp'
file_name3 = 'diff3.bmp'
file_name4 = 'diff4.bmp'

img = Image.open(pre_path+file_name1)
img.convert("L").save(pre_path+"g"+file_name1)

i1 = iio.imread(pre_path+"g"+file_name1)
i2 = iio.imread(pre_path+file_name2)
i3 = iio.imread(pre_path+file_name3)
i4 = iio.imread(pre_path+file_name4)

i = i1+i2+i3+i4

iio.imwrite(pre_path+"output.bmp", i)
