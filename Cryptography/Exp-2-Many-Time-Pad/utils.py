def byte_xor(a: bytes, b: bytes) -> bytes:
    '''
    :return: xor result of a and b
    '''
    if len(a) > len(b):
        return bytes([x ^ y for x, y in zip(a[:len(b)], b)])
    else:
        return bytes([x ^ y for x, y in zip(a, b[:len(a)])])