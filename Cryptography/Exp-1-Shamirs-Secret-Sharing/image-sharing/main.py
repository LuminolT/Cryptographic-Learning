from statistics import mode
import numpy as np
import matplotlib.pyplot as plt
from shamir import *
from binascii import hexlify

img = plt.imread('cat.jpg')
# plt.imshow(img)

def img_split(k, n, img: np.ndarray):
    a, b, c = img.shape
    l = []
    for i in range(n):
        l.append(np.zeros((a, b, c), np.dtype('int')))
    for i in range(a):
        for j in range(b):
            for kk in range(c):
                tmp_share = Shamir.split(k, n, int(img[i, j, kk]))
                for idx in range(n):
                    l[idx][i, j, kk] = bytes_to_long(tmp_share[idx][1])
    return l


# f, axarr = plt.subplots(3,3)

tmp_l = img_split(3, 5, img)
tmp_l.append(img)

print('imhere')

def show_images(images: list[np.ndarray]) -> None:
    n: int = len(images)
    f = plt.figure()
    for i in range(n):
        # Debug, plot figure
        f.add_subplot(1, n, i + 1)
        plt.imshow(images[i])

    plt.show(block=True)

show_images(tmp_l)

plt.show()




# l = Shamir.split(3, 5, 25)

# print(l)


# for idx, item in l:
#     print("Share {}: {}".format(str(idx), bytes_to_long(item)))

# secret = Shamir.combine(l[0:25])

# print(f'Secret is : {secret}')