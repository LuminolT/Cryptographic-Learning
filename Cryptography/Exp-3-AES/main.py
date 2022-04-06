from binascii import unhexlify
from utils import *

def main():
    keys = []
    cipher_texts = []
    with open('infos.txt', encoding='utf-8') as file:
        content = file.read().split('\n')
    for i in range(1, 16, 4):
        keys.append(unhexlify(content[i]))
        cipher_texts.append(unhexlify(content[i+2]))

    print(CBC.decrypt(cipher_texts[0], keys[0]))
    print(CBC.decrypt(cipher_texts[1], keys[1]))
    print(CTR.decrypt(cipher_texts[2], keys[2]))
    print(CTR.decrypt(cipher_texts[3], keys[3]))

if __name__ == '__main__':
    main()