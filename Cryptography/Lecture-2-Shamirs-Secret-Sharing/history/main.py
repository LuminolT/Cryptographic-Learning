from binascii import hexlify
from shamir import *

def main():
    k, n = 3, 5
    p = 1e9 + 7
    shares = shamir.enc(123, k, n)
    for idx, share in shares:
        print("Index #%d: %s" % (idx, hexlify(share.encode())))
    print(shamir.dec(shares[0:3], k))
    ## TODO
    ## How the shamir secret sharing works?

if __name__ == '__main__':
    main()