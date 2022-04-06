import binascii
from Crypto.Cipher import AES
from cxc_toolkit import integer

def byte_xor(a: bytes, b: bytes) -> bytes:
    '''
    :return: xor result of a and b
    '''
    if len(a) > len(b):
        return bytes([x ^ y for x, y in zip(a[:len(b)], b)])
    else:
        return bytes([x ^ y for x, y in zip(a, b[:len(a)])])

def to_int(byte):
    """
    Convert bytes to int

    :type byte: bytes
    :rtype: int
    """
    s = 0
    for i, number in enumerate(byte):
        s = s * 256 + number
    return s


def byte_add(byte, addtions):
    """
    Add int to bytes

    :type byte: bytes
    :type addtions: int
    :rtype: bytes
    """
    return integer.to_bytes(to_int(byte) + addtions, bytes_size=len(byte))

def msg_block_generator(msg, padding=False):
        while len(msg) >= 16:
            yield msg[:16]
            msg = msg[16:]
        if len(msg) > 0:
            if not padding:
                yield msg
                return

            reminder = 16 - len(msg)
            msg = msg + bytes([reminder]) * reminder
            yield msg
        else:
            yield b'16' * 16


def cipher_block_generator(cipher):
    while len(cipher):
        yield cipher[:16]
        cipher = cipher[16:]

class CBC:

    def encrypt(msg, key, iv):
        cipher = AES.new(key, AES.MODE_ECB)
        cipher_block = iv
        ciphertext = iv
        for msg_block in msg_block_generator(msg, padding=True):
            cipher_block = cipher.encrypt(byte_xor(cipher_block, msg_block))
            ciphertext += cipher_block
        return ciphertext


    def decrypt(cipher_text, key):
        cipher = AES.new(key, AES.MODE_ECB)
        iv, cipher_text = cipher_text[:16], cipher_text[16:]
        msg = b''
        for cipher_block in cipher_block_generator(cipher_text):
            msg_block = byte_xor(cipher.decrypt(cipher_block), iv)
            iv = cipher_block
            msg += msg_block
        if msg[-16:] == b'\x16' * 16:
            return msg[:-16]
        pad_bytes = msg[-1]
        reminder = len(msg) - pad_bytes
        if msg[reminder:] == bytes([pad_bytes]) * pad_bytes:
            return msg[:reminder]
        else:
            print('Cipher text is invalid')


class CTR:

    def encrypt(msg, key, iv):
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = b''
        for i, msg_block in enumerate(msg_block_generator(msg, padding=False)):
            cipher_block = cipher.encrypt(byte_add(iv, i))
            cipher_block = byte_xor(msg_block, cipher_block)
            ciphertext += cipher_block
        return ciphertext

    def decrypt(cipher_text, key):
        iv, cipher_text = cipher_text[:16], cipher_text[16:]
        cipher = AES.new(key, AES.MODE_ECB)
        msg = b''
        for i, cipher_block in enumerate(cipher_block_generator(cipher_text)):
            iv_encrypted = cipher.encrypt(byte_add(iv, i))
            msg_block = byte_xor(cipher_block, iv_encrypted)
            msg += msg_block
        return msg
