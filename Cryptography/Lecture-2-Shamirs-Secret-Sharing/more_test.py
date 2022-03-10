## https://pycryptodome.readthedocs.io/en/latest/src/protocol/ss.html
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir

key = get_random_bytes(16)
shares = Shamir.split(2, 5, key)
for idx, share in shares:
    print("Index #%d: %s" % (idx, hexlify(share)))

shares = []
for x in range(3):
    in_str = input("Enter index and share separated by comma: ")
    idx, share = [ s.strip() for s in in_str.split(",") ]
    shares.append((idx, unhexlify(share)))
key = Shamir.combine(shares)