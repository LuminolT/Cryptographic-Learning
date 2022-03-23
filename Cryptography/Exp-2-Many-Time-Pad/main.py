from binascii import unhexlify
from string import ascii_letters
from math import sqrt
import utils

def main():
    cipher_texts = []
    with open('cipher_text.txt', encoding='utf-8') as file:
        content = file.read().split('\n')
    for i in range(1, 21, 2):
        cipher_texts.append(unhexlify(content[i]))

    with open('dest_text.txt', encoding='utf-8') as file:
        content = file.read()
    dest_text = unhexlify(content)

    letters = ascii_letters.encode('ascii')     ## ASCII letters

    key = [0] * 1024

    for ct_a in cipher_texts:
        possible_pos = [0] * len(ct_a)
        for ct_b in cipher_texts:
            if ct_a == ct_b:
                continue
            guess_str = utils.byte_xor(ct_a, ct_b)
            for idx, guess_char in enumerate(guess_str):
                if guess_char not in letters and guess_char != 0:
                    continue
                possible_pos[idx] += 1

        threshold = len(cipher_texts) - sqrt(len(cipher_texts))   ## Magic threshold

        for i in range(len(ct_a)):
            if possible_pos[i] > threshold:
                key[i] = ct_a[i] ^ 0x20

    print(utils.byte_xor(dest_text, key))


if __name__ == '__main__':
    main()