import numpy as np
import matplotlib.pyplot as plt
from shamir import *
from binascii import hexlify

# img = plt.imread('cat.png')
# plt.imshow(img)
# plt.show()

s = 'TEST_STRING'.encode()

print("Original secret:", hexlify(s))

l = Shamir.split(3, 5, '12345'.encode())

for idx, item in l:
    print("Share {}: {}".format(str(idx), hexlify(item)))

shares = l[1:4]

secret = Shamir.combine(shares)


print(f'Secret is : {secret.decode()}')